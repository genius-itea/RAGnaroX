#!/usr/bin/env bash
#SBATCH --partition=REPLACE
#SBATCH --job-name=ragas
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=REPLACE
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --error=logs/%x-%A_%a.err
#SBATCH --account=REPLACE 
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --time=48:00:00
#SBATCH --array=REPLACE  

set -euo pipefail

# --- Array job configuration ---
# Define list of input JSON files
DATA_JSON_FILES=(
  "/results/dataset.json"
  "/results/dataset2.json"
)

# Get the current array task ID (defaults to 0 if not running as array)
ARRAY_ID=${SLURM_ARRAY_TASK_ID:-0}

# Base port for llama.cpp server (each job uses a different port)
BASE_PORT=8000
PORT=$((BASE_PORT + ARRAY_ID))

# Select the appropriate input file based on array index
DATA_JSON="${DATA_JSON:-${DATA_JSON_FILES[$ARRAY_ID]}}"

# Extract the base filename without path and extension for the results
INPUT_FILENAME=$(basename "${DATA_JSON}" .json)
RESULTS_JSON="${RESULTS_JSON:-results/evaluation_${INPUT_FILENAME}.json}"

# Custom column mappings for your dataset format
QUESTION_COL="${QUESTION_COL:-user_input}"
ANSWER_COL="${ANSWER_COL:-response}"
CONTEXTS_COL="${CONTEXTS_COL:-retrieved_contexts}"
GROUND_TRUTH_COL="${GROUND_TRUTH_COL:-reference}"

# GGUF model path (downloaded if missing)
LLAMA_MODEL="${LLAMA_MODEL:-/PATH_TO_MODEL.gguf}"

# Optional: override to any GGUF
MODEL_URL="${MODEL_URL:-https://huggingface.co/unsloth/gpt-oss-20b-GGUF/resolve/main/gpt-oss-20b-Q6_K.gguf}"

# llama.cpp OpenAI-compatible server address
HOST="${HOST:-127.0.0.1}"
# PORT is now set in the array job configuration section
OPENAI_BASE_URL="http://${HOST}:${PORT}/v1"
OPENAI_API_KEY="${OPENAI_API_KEY:-llama}"                  # any non-empty string

# LLM "model" name label (client-side label only)
LLM_MODEL="${LLM_MODEL:-llama-local}"
EMB_MODEL="${EMB_MODEL:-sentence-transformers/all-MiniLM-L6-v2}"
BATCH_SIZE="${BATCH_SIZE:-}"

# If your cluster uses modules, enable CUDA for GPU offload
# Only use module command if it exists
if command -v module &> /dev/null; then
  module purge || true
  # Uncomment and adjust the CUDA module name based on your cluster
  module load cuda || echo "[WARN] Failed to load CUDA module, continuing anyway"
else
  echo "[INFO] 'module' command not found. Continuing without loading modules."
fi

mkdir -p logs results models

# --- Python env ---
python3 -m venv .ragas-venv
source .ragas-venv/bin/activate
python -m pip install --upgrade pip

# Ensure llama-cpp is GPU-enabled; fallback to CPU if build fails
set +e
# Suppress warnings with 2>/dev/null
python -m pip install "llama-cpp-python[cuda]" -q 2>/dev/null
if [[ $? -ne 0 ]]; then
  echo "[INFO] Installing CPU version of llama-cpp-python"
  python -m pip install llama-cpp-python -q 2>/dev/null
fi
set -e

echo "[INFO] Note: We're using the standalone llama-server binary with GPU support, not the Python bindings"

# Your project deps
if [[ -f requirements.txt ]]; then
  python -m pip install -r requirements.txt
fi

# --- Download model if needed ---
MODEL_DIR="$(dirname "${LLAMA_MODEL}")"
if [[ ! -d "${MODEL_DIR}" ]]; then
  mkdir -p "${MODEL_DIR}"
fi

if [[ ! -f "${LLAMA_MODEL}" ]]; then
  # Check if the model is being downloaded by another job to avoid concurrent downloads
  if [[ -f "${LLAMA_MODEL}.lock" ]]; then
    echo "[INFO] Another job is already downloading the model. Waiting..."
    # Wait for the lock to disappear
    while [[ -f "${LLAMA_MODEL}.lock" ]]; do
      sleep 10
    done
    echo "[INFO] Lock released, continuing..."
  else
    # Create a lock file
    touch "${LLAMA_MODEL}.lock"
    echo "[INFO] Downloading GGUF to ${LLAMA_MODEL}"
    
    # Optional HF token header
    HDR=()
    if [[ -n "${HF_TOKEN:-}" ]]; then
      HDR=(-H "Authorization: Bearer ${HF_TOKEN}")
    fi

    tmpfile="${LLAMA_MODEL}.part"

    set +e
    # header flags must come before the URL
    curl -L "${HDR[@]}" -o "${tmpfile}" "${MODEL_URL}"
    ec=$?
    set -e

    # Remove the lock regardless of outcome
    rm -f "${LLAMA_MODEL}.lock"

    if [[ $ec -ne 0 ]]; then
      echo "[ERROR] Model download failed (curl exit ${ec})." >&2
      exit 1
    fi

    mv -f "${tmpfile}" "${LLAMA_MODEL}"
    echo "[INFO] Model download completed."
  fi
fi

# --- Start llama.cpp server ---
echo "[INFO] Starting llama.cpp server..."

# Build or check for llama-server binary
if [[ ! -f "./build/bin/llama-server" ]]; then
  echo "[INFO] llama-server binary not found, checking if we need to build it..."

  # Check if llama.cpp is cloned
  if [[ ! -d "./llama.cpp" ]]; then
    echo "[INFO] Cloning llama.cpp repository..."
    git clone https://github.com/ggerganov/llama.cpp.git
    cd llama.cpp
  else
    cd llama.cpp
  fi

  # Build with CUDA support
  echo "[INFO] Building llama.cpp with CUDA support..."
  (rm -Rf build; mkdir -p build)
  cd build
  cmake .. -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES="75;86;89"
  cmake --build . --config Release
  cd ../..

  # Set the binary path to the newly built one
  LLAMA_SERVER="./llama.cpp/build/bin/server"
else
  LLAMA_SERVER="./build/bin/llama-server"
fi

# Check if server binary exists
if [[ ! -f "${LLAMA_SERVER}" ]]; then
  echo "[ERROR] llama-server binary not found at ${LLAMA_SERVER}" >&2
  echo "[ERROR] Trying alternative locations..."

  # Try common alternative locations
  for alt_path in "./llama.cpp/build/bin/server" "./llama.cpp/build/bin/llama-server" "/usr/local/bin/llama-server"; do
    if [[ -f "${alt_path}" ]]; then
      echo "[INFO] Found llama-server at ${alt_path}"
      LLAMA_SERVER="${alt_path}"
      break
    fi
  done

  # If still not found, exit
  if [[ ! -f "${LLAMA_SERVER}" ]]; then
    echo "[ERROR] Could not find llama-server binary. Please build llama.cpp first or set LLAMA_SERVER env var." >&2
    exit 1
  fi
fi

# Uncomment to enable CUDA modules if needed
#module load cuda/11.8

# Verify CUDA is available
if command -v nvidia-smi &> /dev/null; then
  echo "[INFO] CUDA GPU detected:"
  nvidia-smi
else
  echo "[WARN] No CUDA GPU detected with nvidia-smi. Server might run in CPU-only mode."
fi

# Launch llama.cpp server with the GGUF model
echo "[INFO] Starting llama.cpp server in background on port ${PORT}..."
export LD_LIBRARY_PATH="$(pwd)/build/bin"

# Get the GPU ID based on array task ID for better GPU isolation
# This assigns one GPU per job (modulo the total number of available GPUs)
NUM_GPUS=$(nvidia-smi --list-gpus | wc -l)
if [[ $NUM_GPUS -gt 0 ]]; then
  GPU_ID=$((ARRAY_ID % NUM_GPUS))
  export CUDA_VISIBLE_DEVICES=$GPU_ID
  echo "[INFO] Using GPU $GPU_ID for this job"
else
  echo "[WARN] No GPUs detected, using CPU mode"
  export CUDA_VISIBLE_DEVICES=""
fi

nvidia-smi

LLAMA_LOG="logs/llama-server-${ARRAY_ID}.log"

${LLAMA_SERVER} \
  --model "${LLAMA_MODEL}" \
  --alias "${LLM_MODEL}" \
  --host "${HOST}" \
  --port "${PORT}" \
  --n-gpu-layers 999 \
  -c 20480 \
  -b 8192 \
  --no-mmap \
  --slots \
  -fa \
  --override-tensor 'blk\.([0-9]*[0246789])\.ffn_.*_exps.*=CPU' \
  > ${LLAMA_LOG} 2>&1 &

# Capture PID and ensure it's running in background
SERVER_PID=$!
disown $SERVER_PID
echo "[INFO] llama.cpp server started with PID: ${SERVER_PID}"

# Log GPU status after model is loaded
sleep 2
echo "[INFO] GPU status after model loading (GPU ${GPU_ID}):"
nvidia-smi

# Immediate check for CUDA errors in log
sleep 2
if grep -i "cuda" logs/llama-server.log | grep -i "error\|fail\|unable"; then
  echo "[ERROR] CUDA initialization issues detected:"
  grep -i "cuda" logs/llama-server.log
  echo "Continuing anyway, but server might be running in CPU-only mode."
fi

# Wait for server to initialize
MAX_WAIT=300
WAIT_INTERVAL=2
ELAPSED=0
while true; do
  if grep -qE "server is listening on" "${LLAMA_LOG}"; then
    echo "[INFO] llama.cpp server is ready (PID: ${SERVER_PID})"
    break
  fi
  sleep $WAIT_INTERVAL
  ELAPSED=$((ELAPSED + WAIT_INTERVAL))
  if [[ $ELAPSED -ge $MAX_WAIT ]]; then
    echo "[ERROR] llama.cpp server did not start HTTP server within $MAX_WAIT seconds."
    kill $SERVER_PID
    exit 1
  fi
  echo "[INFO] Waiting for llama.cpp server to start..."
done

# --- Run RAGAS evaluation ---
echo "[INFO] Starting RAGAS evaluation..."

# Pass correct column mappings to evaluate_ragas.py
SCRIPT_PATH="$(dirname "$0")/evaluate_ragas.py"
if [[ ! -f "${SCRIPT_PATH}" ]]; then
  SCRIPT_PATH="./evaluate_ragas.py"
  if [[ ! -f "${SCRIPT_PATH}" ]]; then
    echo "[ERROR] Could not find evaluate_ragas.py script" >&2
    exit 1
  fi
fi

echo "[INFO] Using evaluation script at: ${SCRIPT_PATH}"

# Make sure the script is executable
chmod +x "${SCRIPT_PATH}"

# Build command with proper column mappings
python "${SCRIPT_PATH}" \
  --data "${DATA_JSON}" \
  --q-col "${QUESTION_COL}" \
  --a-col "${ANSWER_COL}" \
  --c-col "${CONTEXTS_COL}" \
  --gt-col "${GROUND_TRUTH_COL}" \
  --llm-model "${LLM_MODEL}" \
  --openai-base-url "${OPENAI_BASE_URL}" \
  --openai-api-key "${OPENAI_API_KEY}" \
  --emb-model "${EMB_MODEL}" \
  --out "${RESULTS_JSON}" \
  ${BATCH_SIZE:+--batch-size ${BATCH_SIZE}}

# Check if evaluation was successful
if [[ $? -ne 0 ]]; then
  echo "[ERROR] RAGAS evaluation failed for ${DATA_JSON}" >&2
  # Don't exit, still need to clean up the server
else
  echo "[INFO] Evaluation completed successfully for ${DATA_JSON}!"
fi

# Cleanup: Stop the llama.cpp server
echo "[INFO] Stopping llama.cpp server on port ${PORT}..."
kill $SERVER_PID

echo "[INFO] Evaluation complete! Results saved to ${RESULTS_JSON}"
echo "[INFO] Job ${ARRAY_ID} finished processing ${DATA_JSON}"

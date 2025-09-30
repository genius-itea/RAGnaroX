#!/usr/bin/env python3
import argparse, json, os, sys
from pathlib import Path
from typing import List, Dict, Any

import pandas as pd
from datasets import Dataset

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)

# Use LangChain wrappers so we can plug any OpenAI-compatible server (llama.cpp)
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings


def coerce_contexts(col):
    # Ensure contexts is List[str]
    if isinstance(col, list):
        return [str(x) for x in col]
    if isinstance(col, str):
        return [col]
    if pd.isna(col):
        return []
    return [str(col)]


def load_dataset(json_path: Path,
                 q_col: str, a_col: str, c_col: str, gt_col: str) -> Dataset:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        # allow {"data":[...]} wrapper
        data = data.get("data", [])

    if not isinstance(data, list):
        raise ValueError("JSON must be a list of objects or {\"data\": [...]}")

    df = pd.DataFrame(data)

    missing = [col for col in [q_col, a_col, c_col] if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in dataset: {missing}")

    # ground_truth may be absent for reference-free eval; we’ll fill with empty
    if gt_col not in df.columns:
        df[gt_col] = ""

    # normalize column names and types
    df = df.rename(
        columns={
            q_col: "question",
            a_col: "answer",
            c_col: "contexts",
            gt_col: "ground_truth",
        }
    )

    df["question"] = df["question"].astype(str)
    df["answer"] = df["answer"].astype(str)
    df["ground_truth"] = df["ground_truth"].astype(str)
    df["contexts"] = df["contexts"].apply(coerce_contexts)

    return Dataset.from_pandas(df[["question", "answer", "contexts", "ground_truth"]])


def make_llm(model: str, base_url: str | None, api_key: str | None):
    """
    Wrap llama.cpp's OpenAI-compatible server (or any OpenAI-compatible) via LangChain.
    """
    # These env vars are respected by langchain-openai:
    if base_url:
        os.environ["OPENAI_BASE_URL"] = base_url  # e.g. http://127.0.0.1:8000/v1
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key    # llama.cpp ignores the value but needs it set

    chat = ChatOpenAI(
        model=model,
        temperature=0.0,
        max_tokens=512,
        timeout=180,
    )
    return LangchainLLMWrapper(chat)


def make_embeddings(model_name: str):
    """
    Use local sentence-transformers via LangChain’s HuggingFaceEmbeddings.
    """
    emb = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={"device": "cpu"})
    return LangchainEmbeddingsWrapper(emb)


def main():
    p = argparse.ArgumentParser(description="Run RAGAS evaluation on a JSON dataset.")
    p.add_argument("--data", required=True, type=Path, help="Path to dataset JSON")
    p.add_argument("--q-col", default="question")
    p.add_argument("--a-col", default="answer")
    p.add_argument("--c-col", default="contexts")
    p.add_argument("--gt-col", default="ground_truth")
    p.add_argument("--llm-model", default="gpt-4o-mini-compat")  # any label; llama.cpp can alias
    p.add_argument("--openai-base-url", default=os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:8000/v1"))
    p.add_argument("--openai-api-key", default=os.getenv("OPENAI_API_KEY", "llama"))
    p.add_argument("--emb-model", default="sentence-transformers/all-MiniLM-L6-v2")
    p.add_argument("--out", default="ragas_results.json")
    p.add_argument("--batch-size", type=int, default=1)
    args = p.parse_args()

    ds = load_dataset(args.data, args.q_col, args.a_col, args.c_col, args.gt_col)

    evaluator_llm = make_llm(args.llm_model, args.openai_base_url, args.openai_api_key)
    evaluator_embeddings = make_embeddings(args.emb_model)

    # Choose metrics; you can drop context_recall if you don't have complete ground_truth
    metrics = [context_precision, context_recall, faithfulness, answer_relevancy]

    # Run eval
    result = evaluate(
        ds,
        metrics=metrics,
        llm=evaluator_llm,
        embeddings=evaluator_embeddings,
        batch_size=args.batch_size,
    )

    print(result)
    
    # Save results to JSON file
    result_dict = {}
    for metric in result:
        result_dict[metric] = float(result[metric])
    
    # Add dataset statistics
    result_dict["dataset_info"] = {
        "num_samples": len(ds),
        "input_file": str(args.data)
    }
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.out) if os.path.dirname(args.out) else ".", exist_ok=True)
    
    # Save results to JSON file
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result_dict, f, indent=2)
    
    print(f"Evaluation results saved to {args.out}")

if __name__ == "__main__":
    sys.exit(main())

#!/bin/bash

mkdir -p data/models

cd data/models

if [ ! -f Qwen3-4B-Thinking-2507-Q8_0.gguf ]; then
	wget https://huggingface.co/unsloth/Qwen3-4B-Thinking-2507-GGUF/resolve/main/Qwen3-4B-Thinking-2507-Q8_0.gguf
fi

if [ ! -f Qwen3-4B-Instruct-2507-Q8_0.gguf ]; then
	wget https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF/resolve/main/Qwen3-4B-Instruct-2507-Q8_0.gguf
fi

if [ ! -f multilingual-e5-large-instruct-q8_0.gguf ]; then
	wget https://huggingface.co/KeyurRamoliya/multilingual-e5-large-instruct-GGUF/resolve/main/multilingual-e5-large-instruct-q8_0.gguf
fi

if [ ! -f bge-reranker-v2-m3-Q8_0.gguf ]; then
	wget https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF/resolve/main/bge-reranker-v2-m3-Q8_0.gguf
fi

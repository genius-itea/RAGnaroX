# RAGnaroX: Replication Package and Results

## Overview

This document provides the complete replication package for RAGnaroX, including model configurations, evaluation methodology, datasets, and experimental results.

## 1. Model Architecture and Components

### 1.1 Embedding Models

- **multilingual-e5-large**: [HuggingFace Link](https://huggingface.co/intfloat/multilingual-e5-large)
  - Parameters: 560M
  - Format: instruct-q8_0

### 1.2 Reranking Models

- **bge-reranker-v2-m3-q8**: [HuggingFace Link](https://huggingface.co/BAAI/bge-reranker-v2-m3)
  - Parameters: 568M (quantized)

### 1.3 Generator Models

- **Qwen3-14B-Instruct**: [HuggingFace Link](https://huggingface.co/lm-kit/qwen-3-14b-instruct-gguf)
- **Qwen3-8B-Instruct**: [HuggingFace Link](https://huggingface.co/lm-kit/qwen-3-8b-instruct-gguf)
- **Qwen3-4B-Instruct**: [HuggingFace Link](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF)
- **Gemma-3n-E2B-it**: [HuggingFace Link](https://huggingface.co/unsloth/gemma-3n-E2B-it-GGUF)
- **Phi-4-mini-instruct**: [HuggingFace Link](https://huggingface.co/Mungert/Phi-4-mini-instruct-GGUF)
- **Mistral-7B-Instruct-v0.3**: Q8_0 format

## 2. Evaluation Framework: RAGAS

We used [RAGAS](https://github.com/explodinggradients/ragas) (Retrieval Augmented Generation Assessment), a comprehensive framework for evaluating RAG systems, as described in the paper: [Es et al. 2023](https://arxiv.org/abs/2309.15217).

### 2.1 Evaluation Metrics

RAGAS provides four key metrics to assess different aspects of RAG performance:

- **Context Precision**: Measures the retriever's ability to rank relevant chunks higher than irrelevant ones
  - [Documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/)
- **Context Recall**: Evaluates how well the retrieval system captures all relevant information
  - [Documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/)
- **Faithfulness**: Assesses whether the generated answer is grounded in the retrieved context
  - [Documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)
- **Answer Relevancy**: Measures how well the generated answer addresses the original question
  - [Documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/)

### 2.2 Evaluator Model Selection

RAGAS allows us to systematically assess the quality of generated responses by comparing them against reference answers using various metrics. For the evaluation model, we executed a test run with models of different sizes:

| Model           | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| --------------- | ----------------: | -------------: | -----------: | ---------------: |
| qwen-30B        |            0.9007 |         0.9234 |       0.8595 |           0.8014 |
| gpt-os-20B (B1) |            0.9044 |         0.9417 |       0.8327 |           0.7846 |
| gpt-os-20B (B2) |            0.9044 |         0.9416 |       0.8331 |           0.7846 |
| gpt-oss-120B    |            0.8947 |         0.9228 |       0.8233 |           0.8086 |

**Statistical Analysis:**

| Metric            | Max    | Min    | Range  |
| ----------------- | ------ | ------ | ------ |
| Context Precision | 0.9044 | 0.8947 | 0.0097 |
| Context Recall    | 0.9417 | 0.9228 | 0.0189 |
| Faithfulness      | 0.8595 | 0.8233 | 0.0362 |
| Answer Relevancy  | 0.8086 | 0.7846 | 0.0240 |

> **Selected Model:** **gpt-os-20B** was chosen for further evaluation due to its optimal balance between performance and computational efficiency.

## 3. Experimental Setup

### 3.1 Hardware Configuration

- **Primary Setup**: 4x RTX 4090 GPUs (24GB VRAM each)
- **Secondary Setup**: 8x L40S GPUs (48GB VRAM each)

### 3.2 Evaluation Datasets

For each dataset, we randomly selected a subset of 1000 Q-A pairs for evaluation (400 pairs for MLQA due to corpus size limitations).

#### 3.2.1 Single-Hop Dataset: SQuAD v1.1

- **Source**: Stanford Question Answering Dataset
- **Website**: [SQuAD Explorer](https://rajpurkar.github.io/SQuAD-explorer/)
- **Paper**: [Rajpurkar et al. 2016](https://arxiv.org/abs/1606.05250)
- **Sample Size**: 1,000 Q-A pairs
- **Task Type**: Single-hop factual questions

#### 3.2.2 Multi-Hop Dataset: MultiHop-RAG

- **Description**: Dataset for Diverse, Explainable Multi-hop Question Answering
- **Repository**: [GitHub](https://github.com/yixuantt/MultiHop-RAG)
- **Paper**: [Tang et al. 2024](https://arxiv.org/abs/2401.15391)
- **Sample Size**: 1,000 Q-A pairs
- **Task Type**: Multi-hop reasoning questions

#### 3.2.3 Multi-Language Dataset: MLQA v1

- **Source**: MultiLingual Question Answering (Meta)
- **Languages**: 7 languages (Arabic, German, Spanish, Hindi, Vietnamese, Thai, English)
- **Repository**: [GitHub](https://github.com/facebookresearch/MLQA)
- **Paper**: [Lewis et al. 2020](https://aclanthology.org/2020.acl-main.653/)
- **Sample Size**: 400 Q-A pairs

#### 3.2.4 Domain-Specific Dataset: CASABLANCA

- **Source**: [CASABLANCA Documentation](https://docs.casablanca.at/)
- **Generation Method**: Q-A pairs generated with RAGAS and validated by human annotators

## 4. Performance Monitoring and Metrics

### 4.1 Hardware Performance Tracing

To quantitatively assess computational resource utilization during evaluation runs, we implemented a systematic hardware performance tracing protocol. System-level metrics were sampled at regular intervals using a custom shell script that recorded the following parameters:

#### 4.1.1 Monitoring Parameters

**Temporal Data:**

- **Timestamp**: Exact time of each measurement (ISO 8601 format)

**CPU Metrics:**

- **CPU Utilization (%)**: Measured using `mpstat` (variable: `cpu_pct`)

**Memory Metrics:**

- **System RAM Usage (MB)**: Absolute memory consumption (variable: `ram_used_mb`)
- **System RAM Percentage (%)**: Relative memory usage (variable: `ram_pct`)
  - Derived from `/proc/meminfo`

**GPU Metrics:**

- **GPU VRAM Usage (MB)**: Aggregated across all GPUs (variable: `vram_used_mb`)
- **GPU VRAM Percentage (%)**: Relative GPU memory usage (variable: `vram_pct`)
- **Total GPU Power Draw (W)**: Energy consumption across all GPUs (variable: `total_gpu_power_w`)
  - All GPU metrics collected via `nvidia-smi`


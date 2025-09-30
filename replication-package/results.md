# RAGnaroX Evaluation Results

This document presents comprehensive evaluation results for the RAGnaroX system across multiple datasets and configurations. The evaluation uses RAGAS metrics including Context Precision, Context Recall, Faithfulness, and Answer Relevancy.

## 1. Single-Hop Dataset (SQuAD v1.1)

**Configuration**: 5 chunks retrieved per query

### Model Comparison

| GenerationModel | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| --------------- | ----------------: | -------------: | -----------: | ---------------: |
| **qwen4B**      |            0.8973 |         0.9416 |       0.8588 |           0.8168 |
| **qwen8B**      |            0.8981 |         0.9416 |       0.8364 |           0.7865 |
| **qwen14B**     |            0.9044 |         0.9417 |       0.8327 |           0.7846 |
| **phi4mini**    |            0.8995 |         0.9416 |       0.7192 |           0.7764 |
| **mistral**     |            0.9030 |         0.9417 |       0.7963 |           0.7705 |
| **gemma**       |            0.8998 |         0.9416 |       0.7183 |           0.7722 |

Impact of different response token limits on performance:

| Max Tokens | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ---------- | ----------------: | -------------: | -----------: | ---------------: |
| **300**    |            0.9033 |         0.9350 |       0.8506 |           0.8180 |
| **400**    |            0.8934 |         0.9293 |       0.8556 |           0.8247 |
| **500**    |            0.8661 |         0.9276 |       0.8483 |           0.8148 |

---

## 2. Multi-Hop Dataset (MultiHop-RAG)

**Configuration**: 4 chunks retrieved per query

### Model Performance

| Model        | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------ | ----------------: | -------------: | -----------: | ---------------: |
| **qwen4B**   |            0.4133 |         0.5182 |       0.6341 |           0.6790 |
| **qwen8B**   |            0.4187 |         0.5146 |       0.6874 |           0.6328 |
| **qwen14B**  |            0.4174 |         0.5453 |       0.7039 |           0.6407 |
| **phi4mini** |            0.4159 |         0.5141 |       0.4583 |           0.6612 |
| **mistral**  |            0.4152 |         0.5193 |       0.4654 |           0.6568 |
| **gemma**    |            0.4102 |         0.5056 |       0.4067 |           0.5056 |

### Retrieval Metrics

| Metric     |  Value |
| ---------- | -----: |
| **Hits@4** | 0.5690 |
| **MAP@4**  | 0.5072 |
| **MRR@4**  | 0.5158 |

see [./results/0_cross_dataset_performance_comparison.ipynb](./results/0_cross_dataset_performance_comparison.ipynb) for comparative analysis between single-hop and multi-hop performance.

## 3. Multi-Language Dataset (MLQA v1)

Cross-lingual evaluation using Qwen models across different language pairs.

### 3.1 Monolingual Performance

#### English-English (EN-EN)

| Model       | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ----------- | ----------------: | -------------: | -----------: | ---------------: |
| **qwen14B** |            0.8552 |         0.9040 |       0.8325 |           0.7306 |
| **qwen4B**  |            0.8591 |         0.9037 |       0.8076 |           0.7486 |

#### Spanish-Spanish (ES-ES)

| Model       | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ----------- | ----------------: | -------------: | -----------: | ---------------: |
| **qwen14B** |            0.8255 |         0.8715 |       0.7745 |           0.5282 |
| **qwen4B**  |            0.8193 |         0.8719 |       0.7966 |           0.5754 |

#### German-German (DE-DE)

| Model       | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ----------- | ----------------: | -------------: | -----------: | ---------------: |
| **qwen14B** |            0.7383 |         0.7749 |       0.7674 |           0.4126 |
| **qwen4B**  |            0.7351 |         0.7735 |       0.7320 |           0.4369 |

### 3.2 Cross-Lingual Performance

#### German ↔ English

| Language Pair | Model   | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------- | ------- | ----------------: | -------------: | -----------: | ---------------: |
| **DE→EN**     | qwen14B |            0.6366 |         0.7332 |       0.7251 |           0.7051 |
| **DE→EN**     | qwen4B  |            0.6383 |         0.7320 |       0.7098 |           0.6525 |
| **EN→DE**     | qwen14B |            0.5855 |         0.6968 |       0.7385 |           0.4127 |
| **EN→DE**     | qwen4B  |            0.5916 |         0.6958 |       0.6960 |           0.4263 |

#### Spanish ↔ English

| Language Pair | Model   | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------- | ------- | ----------------: | -------------: | -----------: | ---------------: |
| **ES→EN**     | qwen14B |            0.6999 |         0.8144 |       0.7489 |           0.6859 |
| **ES→EN**     | qwen4B  |            0.7161 |         0.8149 |       0.7305 |           0.6910 |
| **EN→ES**     | qwen14B |            0.6384 |         0.7113 |       0.7375 |           0.5416 |
| **EN→ES**     | qwen4B  |            0.6362 |         0.7120 |       0.7258 |           0.5240 |

#### German ↔ Spanish

| Language Pair | Model   | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------- | ------- | ----------------: | -------------: | -----------: | ---------------: |
| **ES→DE**     | qwen14B |            0.5152 |         0.7176 |       0.6976 |           0.4452 |
| **ES→DE**     | qwen4B  |            0.5181 |         0.7267 |       0.6473 |           0.4354 |
| **DE→ES**     | qwen14B |            0.4968 |         0.6368 |       0.7149 |           0.5218 |
| **DE→ES**     | qwen4B  |            0.5040 |         0.6250 |       0.6134 |           0.4660 |

### 3.3 Extended Model Evaluation

#### German-German (DE-DE)

| Model         | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------- | ----------------: | -------------: | -----------: | ---------------: |
| **gemma**     |            0.7385 |         0.7755 |       0.6839 |           0.4563 |
| **phi4mini**  |            0.7326 |         0.7728 |       0.5915 |           0.3983 |
| **granite8B** |            0.7412 |         0.7769 |       0.7130 |           0.4199 |

#### German-English (DE-EN)

| Model         | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------- | ----------------: | -------------: | -----------: | ---------------: |
| **qwen4B**    |            0.6383 |         0.7320 |       0.7098 |           0.6525 |
| **qwen14B**   |            0.6366 |         0.7332 |       0.7251 |           0.7051 |
| **qwen30B**   |            0.6383 |         0.7320 |       0.7098 |           0.6525 |
| **gemma**     |            0.6342 |         0.7306 |       0.6200 |           0.6896 |
| **phi4mini**  |            0.6411 |         0.7332 |       0.5165 |           0.6157 |
| **granite8B** |            0.6361 |         0.7352 |       0.6733 |           0.7002 |

#### English-German (EN-DE)

| Model         | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------- | ----------------: | -------------: | -----------: | ---------------: |
| **gemma**     |            0.5870 |         0.6941 |       0.6551 |           0.4422 |
| **phi4mini**  |            0.5859 |         0.6960 |       0.4669 |           0.3920 |
| **granite8B** |            0.5870 |         0.6960 |       0.6384 |           0.4133 |

#### English-English (EN-EN)

| Model         | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------- | ----------------: | -------------: | -----------: | ---------------: |
| **gemma**     |            0.8594 |         0.9069 |       0.8093 |           0.6963 |
| **phi4mini**  |            0.8628 |         0.9067 |       0.7218 |           0.7172 |
| **granite8B** |            0.8578 |         0.9067 |       0.7940 |           0.7426 |

---

## 4. Real-World Use Case: CASABLANCA

**Configuration**: 10 chunks retrieved per query (hotel management documentation)

### System Comparison

| System                      | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| --------------------------- | ----------------: | -------------: | -----------: | ---------------: |
| **RAGnaroX (10-docs)**      |            0.7055 |         0.8290 |       0.8363 |           0.5706 |
| **CASABLANCA gpt-4.1-mini** |            0.6885 |         0.9011 |       0.8286 |           0.5445 |
| **CASABLANCA gpt-4o**       |            0.6975 |         0.8915 |       0.9468 |           0.5606 |

### Document Quality Impact

Impact of LLM-based document refactoring on performance:

| Document Version   | Context Precision | Context Recall | Faithfulness | Answer Relevancy |
| ------------------ | ----------------: | -------------: | -----------: | ---------------: |
| **Original**       |            0.5625 |         0.6234 |       0.6886 |           0.5324 |
| **LLM Refactored** |            0.6014 |         0.6356 |       0.7036 |           0.5457 |

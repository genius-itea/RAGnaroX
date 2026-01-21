# Introduction

Please use the following resources to learn more about the project:

- [Demonstration Video](https://www.youtube.com/watch?v=cDxfuEbcoM4)
- [Replication Package](./replication-package/)
  - [Benchmark Datasets](./replication-package/datasets/)
  - [All Results](./replication-package/results.md)
  - [Replication Instructions](./replication-package/setup.md)
  - [RAG Auto Answer Generation Script](./replication-package/answer_generation.ipynb)
  - [Evaluation Script with RAGAS of generated answers](./replication-package/evaluation_with_ragas.ipynb)
  -  [RAG Results](./replication-package/rag_executions/)

## RAG Sources

- GitLab (included)
- Hugging Face (https://huggingface.co/datasets/rajpurkar/squad)
- Casablanca Documentation (https://docs.casablanca.at/)

# Requirements

- OS: Ubuntu 25.04+
- RAM: 64GB RAM
- NVIDIA RTX 4090
- Docker 28.1.1+ (nvidia-container-toolkit)

# Setup

Run setup.sh to download the models.

# Run Docker Compose

```sh
docker compose -p ragnarox up
```

Docker Compose will take several minutes to start all services.

# Access

## Gitlab

- URL: http://localhost:10088/
- User: root
- Password: ragnarox

## RAGnaroX Frontend

- URL: http://localhost:10000/

# 3 — Advanced RAG

Retrieval-Augmented Generation systems — from naive chunking to production-grade pipelines.

## Topics Covered

- Embedding models: dense vs sparse, OpenAI, Cohere, local models
- Vector databases: Chroma, Pinecone, pgvector
- Chunking strategies: fixed, recursive, semantic, sliding window
- Retrieval techniques: similarity search, MMR, hybrid BM25 + dense
- Re-ranking: cross-encoders, Cohere Rerank
- Advanced patterns: HyDE, multi-query, RAG-fusion, parent-child chunks
- Evaluation: RAGAS, context recall, faithfulness scores

## Projects

| Project | Description |
|---------|-------------|
| `basic-rag` | Naive chunk → embed → retrieve → generate |
| `hybrid-rag` | BM25 + dense retrieval with re-ranking |
| `eval-pipeline` | RAGAS evaluation on a test set |

## Setup

```bash
pip install chromadb langchain anthropic sentence-transformers ragas
```

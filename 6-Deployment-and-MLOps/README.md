# 6 — Deployment & MLOps

Deploying, serving, and maintaining AI applications in production.

## Topics Covered

- Containerisation: Docker, multi-stage builds for ML workloads
- API serving: FastAPI, async endpoints, streaming responses
- Model serving: vLLM, Ollama, AWS Bedrock, Azure OpenAI
- CI/CD: GitHub Actions, automated eval gates, model regression tests
- Infrastructure: Kubernetes basics, HPA for LLM services
- Monitoring: latency, error rate, token usage, drift detection
- Feature stores and experiment tracking: MLflow, DVC

## Projects

| Project | Description |
|---------|-------------|
| `llm-api-server` | FastAPI app serving LLM completions with streaming |
| `docker-ml-pipeline` | Containerised training and inference pipeline |
| `github-actions-eval` | CI workflow that runs evals on every PR |

## Setup

```bash
pip install fastapi uvicorn docker mlflow
```

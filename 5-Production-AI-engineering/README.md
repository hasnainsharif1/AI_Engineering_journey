# 5 — Production AI Engineering

Patterns and practices for shipping AI features that are reliable, observable, and cost-efficient.

## Topics Covered

- Prompt management: versioning, A/B testing, prompt registries
- Caching: semantic caching, prompt caching (Anthropic)
- Observability: tracing LLM calls, Langfuse, OpenTelemetry
- Cost optimisation: model routing, batching, caching strategy
- Guardrails: input/output validation, PII redaction, content filters
- Fallback chains: primary → fallback → cached response
- Async + streaming: SSE, WebSocket, partial rendering

## Projects

| Project | Description |
|---------|-------------|
| `prompt-registry` | Version-controlled prompt store with eval harness |
| `llm-gateway` | Router with cost tracking and fallback logic |
| `observability-demo` | End-to-end tracing with Langfuse |

## Setup

```bash
pip install anthropic langfuse opentelemetry-sdk fastapi uvicorn
```

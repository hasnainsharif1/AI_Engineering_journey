# 0 — Python for AI Engineering

Foundational Python skills applied to real AI/ML engineering workflows.

## Topics Covered

- Async programming with `asyncio` and `httpx`
- Pydantic v2 data validation and serialisation
- Abstract base classes, Protocols, and TypedDicts
- Custom decorators and context managers
- Pandas + NumPy data processing
- Loguru structured logging
- CLI tools with Typer and Rich

## Projects

| Project | Description |
|---------|-------------|
| [`async-data-hub`](./async-data-hub/) | Async pipeline that fetches, validates, and analyses live data from multiple APIs |

## Setup

```bash
cd async-data-hub
uv sync
uv run python main.py run
```

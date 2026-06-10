# async-data-hub

An async data fetching and processing pipeline built with modern Python.

## What it does

Concurrently fetches data from three public APIs, validates it with Pydantic v2, runs NumPy/Pandas statistical analysis, and prints a Rich summary table to the terminal.

## Tech Stack

| Library | Purpose |
|---------|---------|
| `httpx` | Async HTTP client |
| `pydantic v2` | Data validation and serialisation |
| `pandas` + `numpy` | Statistical analysis |
| `loguru` | Structured logging |
| `tenacity` | Automatic retries |
| `typer` + `rich` | CLI and terminal output |

## Project Structure

```
async-data-hub/
├── src/datahub/        # Core library
│   ├── fetchers/       # One fetcher per API source
│   ├── processor.py    # Pandas/NumPy analysis
│   ├── pipeline.py     # asyncio.gather orchestration
│   ├── decorators.py   # @timer, @log_call, tenacity retry
│   ├── context.py      # Context managers
│   └── logger.py       # Loguru setup
├── tests/              # pytest-asyncio test suite
└── main.py             # CLI entry point
```

## Quickstart

```bash
uv sync
cp .env .env.local  # add your WEATHER_API_KEY
uv run python main.py run
uv run pytest
```

logger.py:
    https://loguru.readthedocs.io/en/stable/overview.html#features

model.py:
    1. https://docs.python.org/3/library/dataclasses.html
    2. https://pydantic.dev/docs/validation/latest/concepts/models/
    3. For validaion:
        {@field_validator("age")
        @classmethod
        def check_age(cls, value):
            if value < 18:
                raise ValueError("Age must be 18+")
            return value}
   4.  Pydantic is a widely used Python library for data validation and settings management

base.py:
    ABC(abstract base classes): means parents class set rules which child classes must follow.

decorator.py:
    https://tenacity.readthedocs.io/en/latest/
    https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples

Activate and deactivate environment:
    # create
    python -m venv .venv

    # activate
    .venv\Scripts\activate

    # deactivate
    deactivate
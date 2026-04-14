# Contributing

## Development Setup

```bash
git clone https://github.com/ladislav-lettovsky/AI-RAG-Business-Report-Analyst.git
cd AI-RAG-Business-Report-Analyst
```

Install dependencies using `uv`:

```bash
uv sync
uv pip install -e ".[dev]"
```

Create a `.env` file from the example:

```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Project Layout

| Directory | Purpose |
|-----------|---------|
| `src/rag_analyst/` | Main package source code |
| `src/rag_analyst/reporting/` | JSON and terminal output formatters |
| `tests/` | Pytest test suite |
| `data/` | PDF document for RAG pipeline |
| `results/` | Generated JSON results (git-ignored) |
| `.github/workflows/` | CI configuration |

## Branch Conventions

- `main` — production-ready code
- `feature/*` — new features
- `fix/*` — bug fixes
- `docs/*` — documentation changes

## Running Tests

```bash
# Run all tests (ingest tests only without API key)
pytest -v --tb=short

# Run with coverage
pytest -v --tb=short --cov=rag_analyst

# Run only ingest tests (no API key needed)
pytest tests/test_ingest.py -v
```

## Test Suite Overview

| File | Coverage | API Key Required |
|------|----------|-----------------|
| `test_ingest.py` | PDF loading, chunking, token size | No |
| `test_retrieval.py` | Vector store, similarity search, first-chunk injection | Yes |
| `test_response.py` | Raw LLM, engineered, RAG responses | Yes |
| `test_evaluation.py` | GPT-4o evaluation scoring | Yes |

## Key Architecture Rules

1. **Configuration from environment** — All settings come from env vars via `config.py`. No hardcoded API keys.
2. **Logging over printing** — Use `logging` for debug output; `print` only in `runner.py` for user-facing CLI output.
3. **Verbatim business logic** — Response functions, prompts, and evaluation logic match the original notebook exactly.
4. **Lazy client initialization** — OpenAI and LangChain clients are initialized on first use, not at import time.

## CI

GitHub Actions runs on every push and PR to `main`. CI executes `pytest -v --tb=short`, which runs the ingest tests (no API key needed). Tests requiring an API key are automatically skipped in CI.

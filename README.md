# sb-oct

## Installation

1. Clone the repo.
2. Run `uv sync` to install dependencies.

## Usage

- Via the CLI entrypoint: `uv run sb_oct`
- With the dev environment: `uv run --env-file .env sb_oct`
- Via the Python module: `uv run python -m sb_oct`

## Environment Variables

`.env.example` is the template. Copy it to `.env` for development:

```bash
cp .env.example .env
```

- `LOG_LEVEL` (default: `INFO`): console log level. Set to `DEBUG` in `.env` for verbose console output.
- `LOG_FILE` (default: `app.log`): path to the log file.

`uv run --env-file .env` loads the dev environment explicitly (no auto-loading).

## Testing

- Run tests: `uv run pytest`
- Run tests with coverage: `uv run pytest --cov`

## Documentation

- Preview docs locally: `uv run python scripts/serve_docs.py`
- Build static docs: `uv run mkdocs build`

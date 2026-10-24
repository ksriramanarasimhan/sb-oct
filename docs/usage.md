# Usage

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

## Running

Via the CLI entrypoint:

```bash
uv run sb_oct                          # production defaults
uv run --env-file .env sb_oct          # dev settings
```

Or as a Python module:

```bash
uv run python -m sb_oct
```

## Environment Variables

| Variable    | Default    | Description                          |
|-------------|------------|--------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level (DEBUG, INFO, …)   |
| `LOG_FILE`  | `app.log`  | Path to the log file                 |

Copy `.env.example` to `.env` for development defaults, then run with `uv run --env-file .env`.

## Log Format

Both the console and the log file show **only the message**, with no timestamp, level or source location:

```text
Hello from sb_oct!
```

Unhandled exceptions caught by `@logger.catch` still log a full traceback below the message.

The format is set by `LOG_FORMAT` in `src/sb_oct/app.py` and uses [loguru's `format` fields](https://loguru.readthedocs.io/en/stable/api/logger.html). To add the timestamp and level back, for example:

```python
LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
```

!!! note
    Without timestamps and levels, `app.log` can't be ordered in time or filtered by severity. `LOG_LEVEL` still controls which messages reach the console.

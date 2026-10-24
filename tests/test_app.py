import os
from pathlib import Path

from loguru import logger

from sb_oct.app import configure_logging, main


def test_main_logs_greeting(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hello from sb_oct!" in captured.err


def test_main_logs_message_only(capfd):
    main()
    captured = capfd.readouterr()
    assert captured.err == "Hello from sb_oct!\n"


def test_log_file_contains_message_only():
    main()
    logger.remove()  # close the file handler so the content is flushed
    assert Path(os.environ["LOG_FILE"]).read_text() == "Hello from sb_oct!\n"


def test_caught_exception_still_logs_traceback(capfd):
    configure_logging()
    logger.catch(lambda: 1 / 0)()
    captured = capfd.readouterr()
    assert "Traceback" in captured.err
    assert "ZeroDivisionError" in captured.err

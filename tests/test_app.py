from sb_oct.app import main


def test_main_logs_greeting(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hello from sb_oct!" in captured.err


def test_main_logs_message_only(capfd):
    main()
    captured = capfd.readouterr()
    assert captured.err == "Hello from sb_oct!\n"

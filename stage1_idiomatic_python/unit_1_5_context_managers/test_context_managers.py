from context_managers import timer_context, suppress_errors
import time

def test_timer_context(capsys):
    with timer_context("data loading"):
        time.sleep(0.05)
    captured = capsys.readouterr()
    assert "data loading took" in captured.out

def test_timer_context_exception(capsys):
    try:
        with timer_context("data loading but err"):
            time.sleep(0.05)
            int("not a number")
    except Exception as e:
        assert isinstance(e, ValueError)
    captured = capsys.readouterr()
    assert "data loading but err took" in captured.out

def test_suppress_errors(capsys):
    try:
        with suppress_errors(TypeError, ValueError):
            int("not a number")
    except Exception as e:
        print(e.__class__)
    captured = capsys.readouterr()
    assert "ValueError" not in captured.out

    try:
        with suppress_errors(TypeError, ValueError):
            1 / 0
    except Exception as e:
        print(e.__class__)
    captured = capsys.readouterr()
    assert "ZeroDivisionError" in captured.out
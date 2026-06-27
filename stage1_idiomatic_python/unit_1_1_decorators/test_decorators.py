import time
from decorators import timer
from typing import Any


def test_timer_returns_correct_value() -> None:
    @timer
    def add(a: int, b: int) -> int:
        return a + b
    
    assert add(123, 234) == 357


def test_timer_prints_elapsed_time(capsys: Any) -> None:
    @timer
    def sleep_function() -> None:
        time.sleep(0.02)
    
    sleep_function()
    captured = capsys.readouterr()

    assert "sleep_function took" in captured.out
    assert captured.out.endswith("s\n")


def test_timer_preserves_function_name() -> None:
    @timer
    def business_logic() -> None:
        """This is a very important business logic."""
        pass

    assert business_logic.__name__ == "business_logic"
    assert business_logic.__doc__ == "This is a very important business logic."


def test_timer_handles_args_and_kwargs() -> None:
    @timer
    def mix_cal(a: int, b: int, multiply: bool = False) -> int:
        if multiply:
            return a * b
        return a + b
    
    assert mix_cal(123, 234) == 357
    assert mix_cal(10, 10, multiply=True) == 100

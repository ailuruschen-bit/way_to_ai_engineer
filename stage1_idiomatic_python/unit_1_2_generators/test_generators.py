from generators import fibonacci, running_average
from typing import Generator


def test_fibonacci() -> None:
    gen:Generator[int, None, None] = fibonacci(7)
    assert list(gen) == [0, 1, 1, 2, 3, 5, 8]


def test_running_average() -> None:
    gen:Generator[float, float, None] = running_average()
    next(gen)
    assert gen.send(10) == 10.0
    assert gen.send(20) == 15.0
    assert gen.send(30) == 20.0
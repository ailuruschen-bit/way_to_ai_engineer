# Unit 1.2 — Generators & yield
# Write your solution here.
from typing import Generator


def fibonacci(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def running_average() -> Generator[float, float, None]:
    total = 0.0
    num_count = 0
    while True:
        current = yield 0.0 if num_count == 0 else total / num_count
        num_count += 1
        total += current
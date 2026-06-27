# Unit 1.5 — Context managers
# Write your solution here.
import time
from contextlib import contextmanager
from typing import Generator


@contextmanager
def timer_context(label: str) -> Generator[None, None, None]:
    try:
        start = time.perf_counter()
        yield

    finally:
        elapsed = time.perf_counter() - start
        print(f"{label} took {elapsed:.6f}s")


@contextmanager
def suppress_errors(*exceptions: type[Exception]) -> Generator[None, None, None]:
    try:
        yield

    except Exception as e:
        if not isinstance(e, exceptions):
            raise
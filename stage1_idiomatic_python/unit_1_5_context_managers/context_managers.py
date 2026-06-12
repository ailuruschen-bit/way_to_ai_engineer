# Unit 1.5 — Context managers
# Write your solution here.
from contextlib import contextmanager
import time

@contextmanager
def timer_context(label: str):
    try:
        start = time.perf_counter()
        yield

    finally:
        elapsed = time.perf_counter() - start
        print(f"{label} took {elapsed:.6f}s")


@contextmanager
def suppress_errors(*exceptions):
    try:
        yield

    except Exception as e:
        if not isinstance(e, exceptions):
            raise
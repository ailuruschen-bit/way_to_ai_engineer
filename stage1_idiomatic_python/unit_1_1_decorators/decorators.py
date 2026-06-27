# Unit 1.1 — Decorators
# Write your solution here.
import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar


P = ParamSpec('P')
R = TypeVar('R')


def timer(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        print(f"{func.__name__} took {elapsed:.6f}s")

        return result
    
    return wrapper
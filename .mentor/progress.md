# .mentor/progress.md

## Current position

Stage 1, Unit 1.4 (type hints + mypy --strict) - NEXT.

## Completed

- 1.1 decorators - done - timer decorator, `*args/**kwargs`, `functools.wraps`, `perf_counter`
- 1.2 generators - done - fibonacci (tuple-swap, lazy), `running_average` via `send()`
- 1.3 async/asyncio - done - coroutine vs thread model, `await`, `asyncio.sleep`, `create_task`, `gather`, order preservation, concurrency timing test
- 1.5 context managers - done - `timer_context` + `suppress_errors` via `@contextmanager`

## Next task brief (give me this, then wait)

Start Stage 1, Unit 1.4: type hints + mypy --strict.

First, inspect the current mypy errors across completed Stage 1 units. Then teach:

- Python type hints are mostly static documentation for tools, not runtime enforcement.
- `Any` is an escape hatch and should be rare.
- Generics such as `list[int]`, `dict[str, int]`, `Callable`, `Iterator`, `Generator`, and `ContextManager`.
- Why mypy strict catches ambiguous APIs earlier than tests.

Task should focus on adding correct annotations to previous unit functions and tests without changing behavior. Make me predict at least two mypy failures before running.

## Backlog

- 1.6 comprehensions & functional tools
- 1.7 packaging, project structure, testing

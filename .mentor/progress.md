# .mentor/progress.md

## Current position

Stage 1, Unit 1.3 (async/asyncio) - IN PROGRESS, not yet started by me.

## Completed

- 1.1 decorators - done - timer decorator, `*args/**kwargs`, `functools.wraps`, `perf_counter`
- 1.2 generators - done - fibonacci (tuple-swap, lazy), `running_average` via `send()`
- 1.5 context managers - done - `timer_context` + `suppress_errors` via `@contextmanager`

## Next task brief (give me this, then wait)

Implement in `stage1_idiomatic_python/unit_1_3_async/async_basics.py`:

1. `async fetch_simulated(url: str, delay: float) -> str`
   - await `asyncio.sleep`
   - return `f"response from {url}"`
2. `async fetch_all(urls: list[str]) -> list[str]`
   - fetch all concurrently via `asyncio.gather`
   - use `delay=0.1` for each URL
   - total time should be about 0.1s, not `n * 0.1s`
   - preserve input order in the returned list
3. Add a `main()` run via `asyncio.run`.
4. Add tests with `pytest-asyncio` (`uv add --dev pytest-asyncio`).

## Backlog

- 1.4 type hints + mypy --strict
- 1.6 comprehensions & functional tools
- 1.7 packaging, project structure, testing

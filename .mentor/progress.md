# .mentor/progress.md

## Current position

Stage 1, Unit 1.7 (packaging, project structure, testing) - NEXT.

## Completed

- 1.1 decorators - done - timer decorator, `*args/**kwargs`, `functools.wraps`, `perf_counter`
- 1.2 generators - done - fibonacci (tuple-swap, lazy), `running_average` via `send()`
- 1.3 async/asyncio - done - coroutine vs thread model, `await`, `asyncio.sleep`, `create_task`, `gather`, order preservation, concurrency timing test
- 1.4 type hints + mypy --strict - done - `Callable`, `ParamSpec`, `TypeVar`, `Generator[Y, S, R]`, `type[Exception]`, strict mypy cleanup across completed units
- 1.5 context managers - done - `timer_context` + `suppress_errors` via `@contextmanager`
- 1.6 comprehensions & functional tools - done - list/set comprehensions, generator expressions, `sorted(..., key=...)`, `defaultdict` aggregation, typed records with `TypedDict`, empty collection vs `None` contracts

## Next task brief (give me this, then wait)

Start Stage 1, Unit 1.7: packaging, project structure, testing.

Teach Python project layout from a Java/Spring background:

- import resolution vs Java packages
- why `src/` layout exists
- `__init__.py`
- module vs package
- test layout and import style
- CLI entry points basics
- why project structure matters before LLM/RAG code grows

Task should focus on moving one small utility into an importable package under `src/`, adding tests that import it as package code, and keeping `uv run pytest` / `uv run mypy .` green.

## Backlog

- Stage 1 gate quiz after Unit 1.7

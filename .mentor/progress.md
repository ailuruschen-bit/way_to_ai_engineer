# .mentor/progress.md

## Current position

Stage 1, Unit 1.6 (comprehensions & functional tools) - NEXT.

## Completed

- 1.1 decorators - done - timer decorator, `*args/**kwargs`, `functools.wraps`, `perf_counter`
- 1.2 generators - done - fibonacci (tuple-swap, lazy), `running_average` via `send()`
- 1.3 async/asyncio - done - coroutine vs thread model, `await`, `asyncio.sleep`, `create_task`, `gather`, order preservation, concurrency timing test
- 1.4 type hints + mypy --strict - done - `Callable`, `ParamSpec`, `TypeVar`, `Generator[Y, S, R]`, `type[Exception]`, strict mypy cleanup across completed units
- 1.5 context managers - done - `timer_context` + `suppress_errors` via `@contextmanager`

## Next task brief (give me this, then wait)

Start Stage 1, Unit 1.6: comprehensions & functional tools.

Teach Python's expression-oriented data transformation style from a Java/Spring background:

- list/dict/set comprehensions vs explicit loops
- generator expressions vs list comprehensions
- `sorted(..., key=...)`
- `enumerate`, `zip`, `any`, `all`
- when a normal loop is clearer than a comprehension

Task should focus on transforming small collections of records without Java-style temporary mutation or `range(len(...))` indexing.

## Backlog

- 1.7 packaging, project structure, testing

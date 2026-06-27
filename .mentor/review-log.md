# .mentor/review-log.md

## Open patterns (flag if they recur)

- Java-style redundant temp variables (1.1 `end_time`, 1.2 `third`) - improving.
- Dead code in try/except (1.5 `raise e`; `finally: ...`) - watch next exception code.
- Output-prediction precision - improving after Unit 1.3; keep forcing predictions before running.
- Loose tests before review (1.3 checked substring instead of exact list) - watch next unit.
- Import/style cleanup after behavior works (1.3 import order, blank lines, trailing space) - minor but recurring-review quality issue.
- Initial type annotations as guesses (1.4 used invalid `function`, lowercase `any`, and instance-vs-class confusion) - improved after explanation.

## Resolved

- `functools.wraps` necessity - understood fully, including stacked decorators.
- Async basics - understands coroutine vs thread distinction, await/yield behavior, `asyncio.sleep`, and `asyncio.gather` order preservation.
- Unit 1.4 strict mypy cleanup - can explain `ParamSpec`, `TypeVar`, `Generator[Y, S, R]`, and `type[Exception]`.

## English notes

- Generally clear. Tighten article use, tense, and technical nouns in Zenn prose.
- Unit 1.3 correction examples: "same order" not "seam order"; "close to" not "closed to"; "external operation" is clearer than "external task".
- Unit 1.4 note: "The error I fixed in this unit are" should be "The errors I fixed in this unit are" or "The error I fixed in this unit is".

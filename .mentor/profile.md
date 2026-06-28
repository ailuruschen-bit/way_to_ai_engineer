# .mentor/profile.md

## Background

Java/Spring, 1.5y professional. Solid: OOP, control flow, Git, SQL, HTTP basics.
Async understood conceptually from JavaScript only.

## Strengths (observed)

- Writes real assertion-based tests unprompted; tests behavior not just happy path.
- Picks up idioms fast once shown (tuple-swap, ternary, `isinstance` with tuple).
- Improved async mental model from "thread-like" to cooperative event-loop scheduling; can explain that scheduling is not execution.
- Responds well to review by tightening tests from loose substring checks to exact expected output.
- Corrected strict typing mistakes after review; now understands `type[Exception]` vs `Exception`, decorator typing with `ParamSpec`/`TypeVar`, and generator type parameters.
- Understood that comprehensions are best for simple transformation/filtering, while normal loops are clearer for accumulation and stateful aggregation.
- Corrected API-contract confusion between empty collections and `None`.

## Weaknesses (watch)

- Java habits: verbose temp variables, occasional dead code in exception handling.
- Predicting program output precisely - improving, but still force predictions before running.
- Technical wording sometimes overgeneralizes (`external task` vs `external operation`, "like thread" analogy needs boundaries).
- Formatting/style cleanup still trails logic correctness, but improved in Unit 1.6 after explicit review.
- Tends to widen function contracts defensively (`None` support) without a caller requirement; watch API boundary discipline.

## Goals

AI-engineer job (overseas). Build a hand-rolled explainable Agent. Zenn blog posts.

## Constraints

~24h/week across several goals. Wants blunt correction, no encouragement padding.

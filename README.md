# Way to AI Engineer

This repository is a public learning portfolio for becoming an AI application engineer who can build RAG, function calling, and agent systems from first principles, then explain the engineering trade-offs clearly enough for overseas interviews and technical writing.

## Skills Demonstrated

| Stage | Portfolio output | Concepts demonstrated |
| --- | --- | --- |
| Stage 1: Idiomatic Python | Small units with tests and Zenn-ready READMEs | decorators, generators, async/asyncio, context managers, strict typing, comprehensions, packaging, pytest |
| Stage 2: Engineering for LLM work | Minimal LLM client and resilient service code | async HTTP, retries, structured errors, logging, configuration, API boundaries |
| Stage 3: RAG from scratch | Explainable retrieval pipeline | chunking, embeddings, cosine similarity, vector storage, prompt assembly, evaluation basics |
| Stage 4: Function Calling and Agents | Hand-built explainable agent | tool schemas, function dispatch, reasoning loop, planning, self-checking, failure modes |
| Stage 5: Productionization | Production-minded capstone hardening | cost control, token budgets, observability, AWS deployment, monitoring, evaluation |

## Curriculum

| Stage | Focus | Evidence expected |
| --- | --- | --- |
| 1 | Python fluency for AI engineering | Tested Python units with strict mypy and clear unit READMEs |
| 2 | Reliable LLM application foundations | Raw HTTP client, error model, retry strategy, logging, and typed interfaces |
| 3 | RAG fundamentals before frameworks | Manual retrieval implementation followed by a framework comparison |
| 4 | Tool use and agents from first principles | Manual tool-calling loop and explainable agent capstone |
| 5 | Production readiness | Cost, evaluation, monitoring, deployment, and operational documentation |

## Setup

```bash
uv sync
```

## Quality Checks

```bash
uv run pytest
uv run mypy .
```

## Learning Journal

The current mentor state, completed units, and next task are tracked in [.mentor/progress.md](.mentor/progress.md).

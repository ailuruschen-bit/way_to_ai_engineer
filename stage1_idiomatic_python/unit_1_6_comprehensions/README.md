# Unit 1.6 — Understanding Comprehensions

## List comprehension vs normal loop

List comprehensions provide a concise way to build a new list from an iterable.

Instead of writing

```python
result = []

for item in items:
    if condition(item):
        result.append(transform(item))
```

we can simply write

```python
result = [
    transform(item)
    for item in items
    if condition(item)
]
```

A list comprehension should be viewed as a **mapping + filtering** operation.

Whenever each input element independently produces at most one output element, a comprehension is usually the cleanest solution.

---

## Dict and set comprehensions

Python also provides comprehensions for dictionaries and sets.

Dictionary comprehension

```python
{
    order["user"]: order["total"]
    for order in orders
}
```

creates key-value pairs.

Set comprehension

```python
{
    order["user"]
    for order in orders
}
```

automatically removes duplicated values.

However, dictionary comprehensions are **not suitable for accumulation**.

If multiple items generate the same key, the last value simply overwrites the previous one.

For aggregation tasks such as counting or summing values, a normal loop with `defaultdict` is much clearer.

---

## Generator expression vs list comprehension

A generator expression looks almost identical to a list comprehension.

```python
(x * 2 for x in nums)
```

instead of

```python
[x * 2 for x in nums]
```

The difference is that a list comprehension immediately creates an entire list in memory, while a generator expression produces values one by one.

Generator expressions are useful when:

* processing very large datasets,
* passing values directly into functions like `sum()` or `any()`,
* or avoiding unnecessary memory allocation.

---

## `sorted(..., key=...)`

The `key` parameter tells Python how to compare each element.

For example,

```python
sorted(
    totals.items(),
    key=lambda item: item[1],
    reverse=True,
)
```

sorts dictionary items by their values instead of their keys.

The original objects are never modified.

Instead, Python computes a temporary key for every element and sorts according to those keys.

---

## `enumerate`, `zip`, `any`, and `all`

These are small but extremely useful functional tools.

`enumerate()` attaches an index while iterating.

```python
for index, value in enumerate(values):
    ...
```

`zip()` iterates over multiple iterables simultaneously.

```python
for name, score in zip(names, scores):
    ...
```

`any()` returns `True` if at least one element is truthy.

```python
any(score >= 90 for score in scores)
```

`all()` returns `True` only if every element is truthy.

```python
all(order["paid"] for order in orders)
```

These functions often replace manual loops with simpler and more expressive code.

---

## When a normal loop is clearer than a comprehension

Not every loop should become a comprehension.

During this exercise I originally tried to calculate user totals with a dictionary comprehension.

```python
{
    order["user"]: order["total"]
    for order in orders
}
```

This looked elegant, but repeated users overwrote previous values instead of accumulating them.

The correct solution was

```python
totals = defaultdict(int)

for order in orders:
    if order["paid"]:
        totals[order["user"]] += order["total"]
```

The lesson is simple:

Comprehensions are excellent for **building** collections.

Normal loops are often better for **maintaining state**, such as accumulation, grouping, counting, or updating existing objects.

Readability should always be preferred over writing fewer lines.

---

## One bug I fixed: individual order total vs aggregated paid total

One bug in my implementation came from misunderstanding the business requirement.

At first, I filtered orders whose individual total exceeded the minimum value.

```python
{
    order["user"]
    for order in orders
    if order["total"] >= minimum
}
```

This was incorrect.

The requirement was to compare the **sum of all paid orders** for each user.

The correct approach was:

1. Aggregate every paid order by user.
2. Compare the aggregated total with the threshold.

This reminded me that writing correct code starts with understanding the data model rather than choosing the right syntax.

---

## `[]` vs `None` in function contracts

An empty list and `None` represent different meanings.

```python
orders: list[Order]
```

means the caller must always provide a list.

The list may simply be empty.

```python
[]
```

means

> "There are no orders."

while

```python
None
```

usually means

> "No value was provided."

or

> "The data does not exist."

These are different states.

If a function accepts

```python
list[Order] | None
```

it must explicitly handle the `None` case.

Otherwise, iterating over `None`

```python
for order in orders:
```

raises

```text
TypeError: 'NoneType' object is not iterable
```

Unless `None` carries meaningful business semantics, it is often better to require an empty collection instead.

This makes the function contract simpler and avoids unnecessary `None` checks throughout the code.

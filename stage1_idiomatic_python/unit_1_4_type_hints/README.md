# Unit 1.4 — Understanding Type Hints

## What Python type hints do and do not do

Python is a **dynamically typed** language, so the types of variables and function signatures are not enforced at compile time.

Type hints were introduced to describe the expected types of values, making code easier for both developers and static analysis tools to understand.

Type hints **do not affect program execution**. The Python interpreter ignores them during runtime. Instead, they are used by IDEs and static type checkers such as **mypy**, **pyright**, and **Pylance** to detect potential type errors before execution.

---

## Why `Any` is dangerous

`Any` disables type checking.

Once a value is annotated as `Any`, every operation on it is considered valid by the type checker.

```python
value: Any = ...
value.foo()
value + 1
value[100]
```

Although these operations may fail at runtime, static type checkers will not report any errors.

Using `Any` is equivalent to telling the type checker:

> "Trust me. I know what I'm doing."

Therefore, `Any` should only be used when the real type cannot reasonably be expressed.

---

## Why decorators need `ParamSpec` and `TypeVar`

Functions are first-class objects in Python, and their type is represented by `Callable`.

```python
Callable[[int, str], bool]
```

means

```text
(int, str) -> bool
```

Decorators are special because they receive a function and usually return another function with **exactly the same signature**.

The decorator does not know:

* the parameter types,
* the number of parameters,
* or the return type.

However, it must preserve all of them.

### `TypeVar`

`TypeVar` represents **a single type**.

It is Python's equivalent of a generic type parameter in languages like Java.

```python
from typing import TypeVar

T = TypeVar("T")

def identity(x: T) -> T:
    return x
```

Here, `T` may become `int`, `str`, `list[int]`, or any other type.

### `ParamSpec`

`TypeVar` cannot describe an entire function signature.

For decorators, we also need to preserve the parameter list, including:

* parameter types,
* parameter order,
* positional-only parameters,
* keyword-only parameters,
* `*args`,
* and `**kwargs`.

This is exactly what `ParamSpec` is designed for.

```python
from typing import Callable, TypeVar, ParamSpec
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")

def timer(func: Callable[P, R]) -> Callable[P, R]:

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        ...

    return wrapper
```

`P.args` and `P.kwargs` are **not ordinary tuple and dict types**.

Instead, they are special typing objects that preserve the entire calling convention of the original function.

`TypeVar` represents **one type**, while `ParamSpec` represents **one function signature**.

---

## Generator[Y, S, R]

A generator function usually returns a value of type:

```python
Generator[Y, S, R]
```

where

* **Y** — the type produced by `yield`
* **S** — the type accepted by `send()`
* **R** — the value returned by `return`

The return value is **not yielded**.

Instead, Python stores it inside the `value` attribute of the `StopIteration` exception.

```python
def gen():
    yield 1
    return "finished"
```

Internally, this is conceptually equivalent to

```python
yield 1
raise StopIteration("finished")
```

although generators should never raise `StopIteration` directly.

---

## Difference between `Exception` and `type[Exception]`

```python
Exception
```

means

> an exception instance.

```python
def handle(exc: Exception):
    ...
```

For example,

```python
ValueError("invalid input")
```

is an `Exception`.

---

```python
type[Exception]
```

means

> an exception class.

```python
def register(exc_type: type[Exception]):
    ...
```

For example,

```python
ValueError
RuntimeError
FileNotFoundError
```

are all valid values.

In short,

```text
Exception        -> object
type[Exception]  -> class
```

---

## One mypy error that taught me something

One of my first mypy errors involved `Optional`.

At first, I thought

```python
def foo(x: Optional[int]):
    ...
```

meant that the argument itself was optional and could simply be omitted.

Later, I learned that `Optional[int]` is just another way of writing

```python
int | None
```

It means the value can either be an `int` or `None`; it does **not** mean the parameter can be omitted.

If I actually want an optional parameter, I need to provide a default value:

```python
def foo(x: int | None = None):
    ...
```

This mistake also helped me understand another concept.

When a value is annotated as `int | None`, type checkers cannot assume it is always an `int`.

```python
def square(x: int | None) -> int:
    return x * x
```

mypy correctly reports an error because `x` might still be `None`.

The proper solution is to narrow the type first:

```python
def square(x: int | None) -> int:
    if x is None:
        return 0

    return x * x
```

This taught me that type hints describe **all possible types** a value may have, and it is my responsibility to eliminate impossible cases before using the value as a more specific type.

# Unit 1.5 — Understanding Context Managers

## What is a Context Manager?

A context manager is an object that works with the `with` statement.

It allows code to be executed automatically before entering a block and after leaving it.

This mechanism is commonly used for resource management, such as:

* Opening and closing files
* Acquiring and releasing locks
* Managing database connections
* Creating temporary environments

The most important guarantee is:

> The cleanup code will always run when leaving the `with` block, even if an exception occurs.

---

## How Does a Context Manager Work?

A context manager must implement two methods:

```python
__enter__(self)
__exit__(self, exc_type, exc_val, exc_tb)
```

Example:

```python
class MyContext:

    def __enter__(self):
        print("Before entering the with block.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("After leaving the with block.")
```

Usage:

```python
with MyContext():
    print("Doing my job...")
```

Output:

```text
Before entering the with block.
Doing my job...
After leaving the with block.
```

Python executes the methods in the following order:

```text
__enter__()
↓
with block
↓
__exit__()
```

---

## The Return Value of `__enter__`

The value returned by `__enter__()` is assigned to the variable after the `as` keyword.

```python
class MyContext:

    def __enter__(self):
        print("Entering...")
        return "resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Leaving...")
```

Usage:

```python
with MyContext() as resource:
    print(resource)
```

Output:

```text
Entering...
resource
Leaving...
```

This is exactly how file objects work:

```python
with open("test.txt") as file:
    print(file.read())
```

Internally:

```python
file = open("test.txt").__enter__()
```

---

## Exception Handling

The `__exit__()` method is always executed when the `with` block ends.

This is true whether the block finishes normally or raises an exception.

```python
with MyContext():
    int("error")
```

Output:

```text
Before entering the with block.
After leaving the with block.
ValueError ...
```

The cleanup code still runs.

---

## The Arguments of `__exit__`

```python
def __exit__(
    self,
    exc_type,
    exc_val,
    exc_tb
):
    ...
```

Arguments:

```text
exc_type   -> Exception class
exc_val    -> Exception instance
exc_tb     -> Traceback object
```

Example:

```python
class MyContext:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type:
            print(f"Exception: {exc_type.__name__}")
            print(exc_val)
```

Without an exception:

```python
exc_type = None
exc_val = None
exc_tb = None
```

---

## Suppressing Exceptions

A less-known feature is that `__exit__()` can suppress exceptions.

If it returns:

```python
True
```

Python considers the exception handled and will not re-raise it.

```python
class MyContext:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exception handled.")
        return True
```

Usage:

```python
with MyContext():
    int("error")

print("Program continues...")
```

Output:

```text
Exception handled.
Program continues...
```

The exception disappears.

Returning:

```python
False
```

or returning nothing lets the exception continue propagating normally.

---

## Creating a Context Manager with a Generator

Writing a class every time can be verbose.

Python provides:

```python
contextlib.contextmanager
```

which allows a generator to be converted into a context manager.

```python
from contextlib import contextmanager

@contextmanager
def my_context():

    print("Before entering the with block.")

    yield

    print("After leaving the with block.")
```

Usage:

```python
with my_context():
    print("Doing my job...")
```

Output:

```text
Before entering the with block.
Doing my job...
After leaving the with block.
```

---

## Why Does `yield` Work Here?

The code before `yield` behaves like:

```python
__enter__()
```

The code after `yield` behaves like:

```python
__exit__()
```

Conceptually:

```python
@contextmanager
def my_context():

    # __enter__()
    setup()

    yield resource

    # __exit__()
    cleanup()
```

The `contextmanager` decorator converts the generator into a real context manager object behind the scenes.

This is a great example of combining:

* Decorators
* Generators
* Context Managers

into a single abstraction.

---

## Handling Exceptions in Generator-Based Context Managers

When using `@contextmanager`, exception handling must be implemented manually.

```python
from contextlib import contextmanager

@contextmanager
def my_context():

    print("Before entering.")

    try:
        yield

    except Exception as e:
        print(f"Exception: {e}")
        raise

    finally:
        print("After leaving.")
```

The `finally` block ensures cleanup always runs.

This is similar to implementing cleanup logic inside `__exit__()`.

---

## Real-World Example: File Management

Without a context manager:

```python
file = open("test.txt")

try:
    content = file.read()
finally:
    file.close()
```

With a context manager:

```python
with open("test.txt") as file:
    content = file.read()
```

The second version is shorter, safer, and easier to maintain.

This is exactly why context managers exist.

---

## Key Takeaways

A context manager:

* Executes setup code before entering a block.
* Executes cleanup code after leaving a block.
* Guarantees cleanup even if exceptions occur.
* Can inspect or suppress exceptions.
* Is usually implemented using `__enter__()` and `__exit__()`.
* Can also be created using `@contextmanager` and a generator.

The most important idea is:

> A context manager is not primarily about the `with` statement. It is about guaranteeing that resources are properly cleaned up, regardless of how the block exits.

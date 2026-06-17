# Unit 1.1 — Understanding Decorators

## What is a Decorator?

A decorator allows a function to gain additional behavior without modifying its original implementation.

You can think of a decorator as a mechanism that wraps a function with another function, enabling extra logic to run before or after the original function is executed.

Common use cases include:

* Logging
* Authentication
* Performance measurement
* Caching
* Retry mechanisms

The original function remains focused on its own responsibility, while the decorator handles cross-cutting concerns around it.

---

## How Does a Decorator Work?

A decorator is simply a higher-order function.

It receives a function as an argument and returns another function.

```python
def customize_decorator(func):
    ...
    return new_func
```

After decoration, the original function name no longer refers to the original function object. Instead, it points to the new function returned by the decorator.

As a result, when you call the decorated function, you are actually calling the wrapper function behind the scenes.

---

## Syntax Sugar

Python provides a convenient syntax for applying decorators.

```python
@customize_decorator
def original_func(p1, p2):
    ...
```

This is equivalent to:

```python
def original_func(p1, p2):
    ...

original_func = customize_decorator(original_func)
```

The `@` syntax is simply syntactic sugar that makes the code cleaner and easier to read.

---

## Creating a Custom Decorator

Since a decorator is just a function that receives another function and returns a new one, we can define our own decorator easily.

A basic implementation looks like this:

```python
def customize_decorator(func):
    def wrapper():
        do_something_before()

        func()

        do_something_after()

    return wrapper
```

The wrapper function adds behavior before and after the original function execution.

---

## Preserving Parameters and Return Values

The previous implementation has a limitation: it only works for functions without parameters and return values.

To make the decorator universal, we need to forward all positional and keyword arguments and return the original result.

```python
def customize_decorator(func):
    def wrapper(*args, **kwargs):
        do_something_before()

        result = func(*args, **kwargs)

        do_something_after()

        return result

    return wrapper
```

Here:

* `*args` collects positional arguments.
* `**kwargs` collects keyword arguments.

This allows the decorator to work with almost any function signature.

---

## The Metadata Problem

After decoration, something unexpected happens.

```python
@customize_decorator
def original_func(p1, p2):
    """my own function"""
    ...

print(original_func.__name__)
print(original_func.__doc__)
```

Output:

```python
wrapper
the wrapper function
```

Why?

Because `original_func` now refers to the wrapper function returned by the decorator.

The original function object still exists, but its metadata is no longer directly accessible through the original name.

---

## functools.wraps

Python provides `functools.wraps` to solve this problem.

`wraps` copies important metadata from the original function to the wrapper function.

```python
from functools import wraps

def customize_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        do_something_before()

        result = func(*args, **kwargs)

        do_something_after()

        return result

    return wrapper
```

Now:

```python
@customize_decorator
def original_func():
    """my own function"""
    pass

print(original_func.__name__)
print(original_func.__doc__)
```

Output:

```python
original_func
my own function
```

The wrapper still executes, but it now preserves the identity of the original function.

---

## Key Takeaways

A decorator is fundamentally a higher-order function that:

1. Receives a function as an argument.
2. Creates a wrapper function.
3. Returns the wrapper function.
4. Replaces the original function reference with the wrapper.

The `@decorator` syntax is merely syntactic sugar for function reassignment.

To build production-ready decorators:

* Use `*args` and `**kwargs` to preserve flexibility.
* Return the original function's result.
* Use `functools.wraps` to preserve metadata.

Once you understand that a decorator is simply "a function that creates another function around an existing one," the concept becomes much less mysterious.

## Parameterized Decorators

So far, all decorators we have seen look like this:

```python
@customize_decorator
def original_func():
    ...
```

In this case, the decorator itself receives the function directly:

```python
original_func = customize_decorator(original_func)
```

However, in real projects, decorators often need their own configuration.

For example:

```python
@retry(times=3)
def fetch_data():
    ...
```

At first glance, it may look like `retry` is the decorator.

Actually, it is not.

The real decorator is the return value of:

```python
retry(times=3)
```

The code above is equivalent to:

```python
def fetch_data():
    ...

fetch_data = retry(times=3)(fetch_data)
```

This process can be divided into two steps:

### Step 1

Call:

```python
retry(times=3)
```

This creates and returns a decorator.

### Step 2

Python automatically applies that decorator:

```python
decorator(fetch_data)
```

which returns the wrapper function.

Finally:

```python
fetch_data = wrapper
```

As a result, a parameterized decorator usually requires three nested functions:

```python
def retry(times):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass

        return wrapper

    return decorator
```

Each layer has a different responsibility:

| Function      | Responsibility                                       |
| ------------- | ---------------------------------------------------- |
| `retry()`     | Receives decorator arguments                         |
| `decorator()` | Receives the target function                         |
| `wrapper()`   | Executes additional logic around the target function |

For this reason, parameterized decorators are often described as **decorator factories**.

They do not decorate functions directly.

Instead, they create and return decorators that will later be applied to functions.

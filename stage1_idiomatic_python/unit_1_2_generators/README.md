# Unit 1.2 — Understanding Generators

## What is a Generator?

A generator makes it possible to execute a function step by step.

Unlike a normal function, which executes from start to finish in a single call, a generator can pause its execution, return a value, and continue later from exactly where it stopped.

This allows values to be produced one by one instead of all at once.

In addition, after each pause, the caller can send a new value back into the generator to influence its future execution.

---

## How Does It Work?

To understand generators, you first need to understand iterators.

An iterator is an object that implements two methods:

```python
__iter__()
__next__()
```

`next(iterator)` calls the iterator's `__next__()` method and returns the next value.

`iter(iterator)` simply returns the iterator itself.

```python
it = iter([1, 2, 3])

print(next(it))
print(next(it))
```

A generator is actually a special type of iterator.

```python
from collections.abc import Iterator

def gen():
    yield 1

g = gen()

print(isinstance(g, Iterator))
# True
```

The difference is that we do not implement `__next__()` ourselves.

Instead, Python automatically creates an iterator object from a function containing the `yield` keyword.

---

## The `yield` Keyword

A normal function executes until it reaches `return`.

```python
def normal():
    print("A")
    print("B")
    return 1
```

Calling it executes the entire function immediately.

```python
normal()
```

Output:

```text
A
B
```

A generator behaves differently.

```python
def gen():
    print("A")
    yield 1

    print("B")
    yield 2
```

Execution pauses whenever a `yield` statement is reached.

```python
g = gen()

next(g)
```

Output:

```text
A
```

Return value:

```python
1
```

The function is now suspended.

Calling `next(g)` again resumes execution from the line immediately after the previous `yield`.

```python
next(g)
```

Output:

```text
B
```

Return value:

```python
2
```

When the function reaches the end, Python raises:

```python
StopIteration
```

---

## Using a Generator with `next()`

```python
def gen_number():
    yield 1
    yield 2
    yield 3

gen = gen_number()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
1
2
3
```

The next call raises:

```text
StopIteration
```

---

## Infinite Generators

One major advantage of generators is that they can represent infinite sequences.

```python
def gen_number_infinite():
    n = 1

    while True:
        yield n
        n += 1
```

Usage:

```python
gen = gen_number_infinite()

for _ in range(100):
    print(next(gen))
```

Output:

```text
1 ... 100
```

The generator itself can continue forever.

---

## Sending Values into a Generator

Generators support two-way communication.

The `send()` method resumes execution and provides a value to the suspended `yield` expression.

```python
def gen_last(begin=None):

    prev = None
    current = begin

    while True:

        temp = current

        current = yield prev

        prev = temp
```

Usage:

```python
gen = gen_last("start")

print(next(gen))
```

Output:

```text
None
```

The first step must use `next()` (or `send(None)`).

This is because execution has not yet reached the first `yield`, so there is no suspended expression available to receive a value.

After that:

```python
print(gen.send("second"))
```

Output:

```text
start
```

Then:

```python
print(gen.send("third"))
```

Output:

```text
second
```

The value sent by `send()` becomes the result of the suspended `yield` expression.

```python
current = yield prev
```

can be viewed as:

```text
yield prev
↓ pause
receive value from send(...)
↓ resume
assign value to current
```

---

## Using a Generator as an Iterable

Because a generator is an iterator, it can be used anywhere an iterable is accepted.

```python
def gen_number(n):
    for i in range(n):
        yield i + 1
```

Convert to a list:

```python
gen = gen_number(10)

print(list(gen))
```

Output:

```text
[1, 2, ..., 10]
```

Or iterate directly:

```python
for i in gen_number(10):
    print(i)
```

Output:

```text
1 ... 10
```

---

## Generator vs Collection

Collections such as lists store all data in memory before being used.

```python
numbers = [1, 2, 3, 4, 5]
```

A generator stores only its execution state.

It produces values only when requested.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

This behavior is called **lazy evaluation**.

---

## Memory Efficiency

Imagine reading a file containing ten million lines.

A list approach:

```python
lines = file.readlines()
```

loads everything into memory.

A generator approach:

```python
for line in file:
    process(line)
```

loads only one line at a time.

This is one of the most common real-world uses of generators.

---

## Infinite Sequences

Since generators calculate values on demand, they can represent sequences that would be impossible to store entirely in memory.

For example:

```python
def fibonacci():

    a = 0
    b = 1

    while True:
        yield a

        a, b = b, a + b
```

Usage:

```python
fib = fibonacci()

for _ in range(10):
    print(next(fib))
```

Output:

```text
0
1
1
2
3
5
8
13
21
34
```

There is no practical way to create a list containing every Fibonacci number.

A generator solves this problem naturally.

---

## Key Takeaways

A generator is:

* A special type of iterator.
* Created using the `yield` keyword.
* Able to pause and resume function execution.
* Capable of producing values lazily.
* Suitable for large datasets and infinite sequences.

The most important thing to remember is:

> A generator is not just a container of values. It is a paused function whose execution state is preserved between iterations.

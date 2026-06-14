# Unit 1.3 — Understanding Asyncio

## What Is a Coroutine?

A coroutine is an execution flow that allows a program to avoid blocking while waiting for long-running operations to complete.

In Python's asyncio framework, there is a central manager called the **Event Loop**. The event loop decides when execution should switch between coroutines and when suspended coroutines should resume.

Although multiple coroutines may appear to run at the same time, they are actually executed one at a time within a single thread. We call them *coroutines* because each coroutine maintains its own independent execution state while waiting for external work to finish.

The most important idea is that a coroutine is not a separate thread. It is simply an execution flow managed by the event loop, which intelligently changes the execution order to improve efficiency.

---

## The `await` Keyword

The `await` keyword is a signal to the event loop.

It tells the event loop:

> "The code after this point cannot continue until the awaited operation finishes."

However, reaching an `await` statement does **not** necessarily mean that execution will immediately switch to another coroutine.

The event loop only schedules other coroutines when the current coroutine actually enters a waiting state, typically while waiting for an external operation such as network I/O, file I/O, or a timer.

The most important point is that coroutine switching happens when the coroutine begins waiting for an external task, not simply because the code encounters the `await` keyword.

---

## `asyncio.sleep()`

`asyncio.sleep()` is one of the operations that genuinely allows the event loop to switch to other coroutines.

When a coroutine executes:

```python
await asyncio.sleep(1)
```

it tells the event loop:

> "Suspend this coroutine for one second and allow other coroutines to run."

The coroutine will remain suspended until:

1. The specified time has passed.
2. The event loop becomes available to resume it.

The most important point is that even after the sleep duration expires, the coroutine does not interrupt another running coroutine. It will only resume when the event loop schedules it again.

---

## Coroutines vs Threads

Coroutines are managed entirely within a single thread.

The event loop controls when execution switches between coroutines, giving the programmer predictable and cooperative scheduling.

Threads, on the other hand, are managed by the operating system.

Multiple threads may run:

* Concurrently through rapid context switching on a single CPU core.
* In parallel on different CPU cores.

Unlike coroutine scheduling, thread scheduling is controlled by the operating system rather than by your program.

---

## `asyncio.gather()`

`asyncio.gather()` accepts multiple coroutine objects or task objects and waits for all of them to complete.

If coroutine objects are provided, `gather()` automatically wraps them into tasks before scheduling them.

The most important feature of `gather()` is that the returned result list always preserves the order of the input arguments, regardless of the order in which the tasks actually finish.

---

## Example: Understanding Task Scheduling

```python
async def fetch_simulated(url: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"response from {url}"


async def fetch_all(urls: list[str]) -> list[str]:
    tasks = [
        asyncio.create_task(
            fetch_simulated(url, 0.1)
        )
        for url in urls
    ]

    result = await asyncio.gather(*tasks)
    return result


async def main() -> None:
    urls = [
        "www.url_001.com",
        "www.url_002.com",
        "www.url_003.com",
        "www.url_004.com",
        "www.url_005.com",
        "www.url_006.com",
    ]

    print(await fetch_all(urls))
```

In this example, I use `asyncio.create_task()` to register all coroutine tasks before passing them to `asyncio.gather()`.

For this particular program, there is no practical difference between creating the tasks before `gather()` and passing coroutine objects directly to `gather()`, because `gather()` will automatically wrap coroutine objects into tasks.

When `create_task()` is called, the coroutines are registered with the event loop and become runnable tasks.

At this moment, however, they do not immediately begin executing because the current coroutine still owns the control flow and the event loop has not regained control yet.

Execution then reaches:

```python
await asyncio.gather(*tasks)
```

At this point, control is returned to the event loop. The event loop can now start executing the scheduled tasks.

Inside each task, the statement:

```python
await asyncio.sleep(...)
```

causes the coroutine to suspend itself and yield control back to the event loop. This allows other ready coroutines to run while the current coroutine is waiting.

After the sleep duration expires, the coroutine becomes ready to run again. However, it does not interrupt a currently running coroutine. Instead, it waits until the event loop schedules it again.

Finally, `asyncio.gather()` waits for all tasks to complete and returns their results in the same order as the input task list, regardless of the order in which the tasks actually finished.

The most important point is that `create_task()` only schedules a coroutine for execution. Scheduling is not execution. A scheduled coroutine can only begin running after control is returned to the event loop.

## Timing Test

The test checks that fetching six URLs finishes in less than `0.25` seconds. If the calls were executed sequentially, six sleeps of `0.1` seconds would take about `0.6` seconds. Finishing under `0.25` seconds shows that the sleep periods overlap through asyncio concurrency.

---

## Key Takeaways

1. Coroutines are not threads. They are execution flows managed by the event loop.
2. `await` does not automatically cause a coroutine switch.
3. A coroutine switch occurs when the current coroutine actually enters a waiting state.
4. `asyncio.sleep()` is a typical operation that yields control back to the event loop.
5. `create_task()` schedules a coroutine but does not immediately execute it.
6. Scheduled tasks can only run after the event loop regains control.
7. `asyncio.gather()` returns results in the order of the input tasks, not in the order they finish.

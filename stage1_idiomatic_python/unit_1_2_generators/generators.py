# Unit 1.2 — Generators & yield
# Write your solution here.
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def running_average():
    total = 0
    num_count = 0
    while True:
        current = yield 0 if num_count == 0 else total / num_count
        num_count += 1
        total += current
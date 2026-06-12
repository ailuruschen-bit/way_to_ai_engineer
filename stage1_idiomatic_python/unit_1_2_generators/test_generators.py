from generators import fibonacci, running_average

def test_fibonacci():
    gen = fibonacci(7)
    assert list(gen) == [0, 1, 1, 2, 3, 5, 8]

def test_running_average():
    gen = running_average()
    next(gen)
    assert gen.send(10) == 10.0
    assert gen.send(20) == 15.0
    assert gen.send(30) == 20.0
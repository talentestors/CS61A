def apply_twice(f, x):
    """
    >>> apply_twice(square, 3)
    81
    """
    return f(f(x))

def square(x):
    """
    >>> square(10)
    100
    """
    return x * x

def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> add_three(5)
    8
    >>> add_three(6)
    9
    """
    def adder(k):
        return k + n
    return adder


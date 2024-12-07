from ucb import trace
from functools import cache

@cache
def fib_cache(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_cache(n - 2) + fib_cache(n - 1)

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


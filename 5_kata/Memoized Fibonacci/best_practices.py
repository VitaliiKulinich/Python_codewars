# 1 _____________
def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci_1(n):
    if n in [0, 1]:
        return n
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)

# 2 _____________

from functools import lru_cache

@lru_cache(None)
def fibonacci_2(n):
    if n in [0, 1]:
        return n
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)
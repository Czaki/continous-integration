from functools import lru_cache


@lru_cache
def fibonacci(num: int) -> int:
    if num < 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

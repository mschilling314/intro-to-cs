def count(a: int) -> int:
    c = 0
    for _ in range(a):
        c += 1
    return c


def sum(*args: int) -> int:
    c = 0
    for arg in args:
        c += count(arg)
    return c

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


def iterate(func_to_call, *args):
    return func_to_call(*args)


print(iterate(sum, 5,6,7))
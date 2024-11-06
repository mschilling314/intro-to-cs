def sum(a:int, b:int, *args: int) -> int:
    c = a + b
    for arg in args:
        c += arg
    return c

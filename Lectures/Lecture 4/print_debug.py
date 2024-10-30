def f1():
    print("In f1")


def f2(val):
    print(f"val is {val}")
    return 2*val

if __name__=="__main__":
    f1()
    v1 = f2(5)
    v2 = f2("Lol")


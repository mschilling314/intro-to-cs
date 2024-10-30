def f1():
    raise Exception("I just don't feel like it.")


def f2():
    f1()

def f3():
    f2()

def f4():
    f3()

def f5():
    f4()

if __name__=="__main__":
    f5()
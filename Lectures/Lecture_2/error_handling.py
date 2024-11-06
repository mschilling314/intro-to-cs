try:
    a = "Hello"
    b = 5
    print(a + b)
except Exception as e:
    print(f"Oh noes, you got the error:\n {e}!")
finally:
    print("Now we can move on with our lives!")
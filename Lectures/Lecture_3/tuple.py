# Declaring a tuple
tuple_ints = (3, 4, 5)

# Accessing a value
print(f" This is the value at index 1: {tuple_ints[1]}")

# Changing a value doesn't work
try:
    tuple_ints[1] = 7
    print(f" This is the list after we change the value at index 1 to 7: {tuple_ints}")
except Exception as e:
    print(f"The error is {e}")
    

# Iterating over a tuple using length
x = len(tuple_ints)
for i in range(x):
    print(f"The value at index {i} is {tuple_ints[i]}")

# Iterating over a tuple using for-each
for num in tuple_ints:
    print(num)

# Lookup
if 5 in tuple_ints:
    print("YAY!!!")
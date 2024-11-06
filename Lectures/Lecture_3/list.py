# Declaring a list
list_ints = [3, 4, 5]

# Accessing a value
print(f" This is the value at index 1: {list_ints[1]}")

# Changing a value
list_ints[1] = 7
print(f" This is the list after we change the value at index 1 to 7: {list_ints}")

# Adding a value
list_ints.append(8)
list_ints.insert(1, 12)
print(f"After append: {list_ints}")
print(*list_ints)

# Iterating over a list using length
x = len(list_ints)
for i in range(x):
    print(f"The value at index {i} is {list_ints[i]}")

# Iterating over a list using for-each
for num in list_ints:
    print(num)

# Lookup
if 5 in list_ints:
    print("YAY!!!")

# Negative indexing
print(list_ints[-1])

# Removing a value
del list_ints[1]
last_val = list_ints.pop()
print(list_ints)
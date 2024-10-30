# Declaring a dict
animals = {"bird": "an animal that has feathers and wings", "dog": "a good boy", "cat": "cute, but usually wants to be left alone"}

# Accessing a value
print(f" This is the value of the key dog: {animals["dog"]}\n")

# Changing a value
animals["bird"] = ["an animal that has feathers and wings", "sing like a canary"]
print(f" This is the dict after we change the value of bird: {animals}\n")

# Adding a value
animals["snake"] = "I really hate these"
print(f"After adding snake: {animals}\n")

# Removing a value
del animals["snake"]
dog = animals.pop("dog")
print(f"After removing snake and dog: {animals}\n")

# Iterating over a dict using keys
for k in animals.keys():
    print(f"The value of {k} is {animals[k]}")
print()

# Iterating over a dict
for k, v in animals.items():
    print(f"The value of key {k} is value {v}")
def pick_word(i: int) -> str:
    result = ""
    if i == 0:
        result += "Hello"
    elif i == 1:
       result +=  "Goodbye"
    else:
        result += "World"
    return result

print(pick_word(0))
print(pick_word(1))
print(pick_word(2))
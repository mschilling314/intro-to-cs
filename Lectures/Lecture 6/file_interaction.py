file = open(file="./Lectures/Lecture 6/fun.txt", mode="r")
print(file.readlines())
file.close()

file2 = open(file="./Lectures/Lecture 6/fun.txt", mode="a")
file2.write(f"\n\nI was here.")
file2.close()
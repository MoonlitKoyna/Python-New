file = open("example.txt", "r")
print(file.read())
file.close()

file = open("example.txt", "r")
print("\n Read in parts  \n")
print(file.read(5))
file.close()

file = open("example.txt", "a")
file.write(" \n Hello this is koyna!")
file.close()
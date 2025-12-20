file = open("Example.txt", "r")
print(file.read())
file.close()

file = open("Example.txt", "r")
print("\n Reading")
print(file.read(7))
file.close()

file = open("Example.txt", "a")
file.write(" \n Hiiii this is Koyna!")
file.close()

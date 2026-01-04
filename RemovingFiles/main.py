import os
print("Checking if 'Example.txt' exists:")
if os.path.exists("Example.txt"):
    os.remove("Example.txt")
    print("'Example.txt' has been deleted.")
else:
    print("'Example.txt' does not exist.")

my_file = open("My_File.txt", "w")
my_file.write("Hello, World!")
my_file.close()
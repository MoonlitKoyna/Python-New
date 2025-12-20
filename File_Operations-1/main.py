with open("example.txt","w") as file:
    file.write("Hello I am Koyna!")
file.close()

with open("example.txt","r") as file:
    data = file.readlines()
    print("Words in the files are:")
    for line in data:
        word = line.split()
        print(word)
file.close()
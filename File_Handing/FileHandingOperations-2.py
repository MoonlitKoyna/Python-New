firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file:")

f2 = open(secondfile,"r")
data= f2.read()
f2.close()

f1= open(firstfile,"a")
f1.write(data)
f1.close()

print("Content of", secondfile, "has been added to the", firstfile)
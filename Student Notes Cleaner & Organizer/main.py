# So here we are reading the contents of the file in parts
file = open("raw_notes.txt", "r")
print(file.read())
file.close()

file = open("raw_notes.txt", "r")
print("\n Reading in parts\n")
print(file.read(50))
file.close()

#And here we are printing the odd lines of the file
main = open("raw_notes.txt", "r")
file = open("OddLines.txt", "w")

cont = main.readlines()
print("\n Printing odd lines of the file\n")
type(cont)
for i in range(1, len(cont)+1):
    if (i%2!=0):
        file.write(cont[i-1])
    else:
        pass

file= open("OddLines.txt", "r")
cont1 = file.read()

print(cont1)

main.close()
file.close()
#
# Now we are removing the repeated lines from the file
outputfile = open("removed_lines.txt", "w")
inputfile = open("raw_notes.txt", "r")
print("\n Removing repeated lines from the file\n")
lines_seen_so_far = set()
print("Removing repeated lines..")
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)
inputfile.close()
outputfile.close()

#At last we are merging the two files created above into a single file so that the user can have both the odd lines and the cleaned lines in a single file
with open("OddLines.txt") as fp:
    data1 = fp.read()
with open("removed_lines.txt") as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2

with open ("MergedFile.txt", "w") as fp:
    fp.write(data1)
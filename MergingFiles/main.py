with open("File1.txt") as fp:
    data1 = fp.read()
with open("File2.txt") as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2

with open ("MergedFile.txt", "w") as fp:
    fp.write(data1)
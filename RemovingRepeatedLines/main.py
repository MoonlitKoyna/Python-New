outputfile = open("output.txt", "w")
inputfile = open("Repeated.txt", "r")

lines_seen_so_far = set()
print("Removing repeated lines..")
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)
inputfile.close()
outputfile.close()

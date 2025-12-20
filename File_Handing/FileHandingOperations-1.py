file_open= open("codingal.txt","r")
print("File in read mode-")
print(file_open.read())
file_open.close()

file_write= open("condingal.txt","w")
file_write.write("File in write mode-")
file_write.write("Hi! This is koyna. I'm 16 years old!")
file_write.close()

file_append= open("codingal.txt","a")
file_append.write("\n File in append mode-")
file_append.write("This is appended text.")
file_append.close()
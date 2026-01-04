import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%^&*()"

all_characters = lowercase + uppercase + digits + special

length = int(input("Enter password length: "))

password = ""
for i in range(length):
    password += random.choice(all_characters)

print("Your generated password is:", password)
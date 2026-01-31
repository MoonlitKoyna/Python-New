number = int(input("Enter a number to check if it's prime or not:"))
print()

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a two-digit prime number")
else:
    print(number, "is not a prime number")
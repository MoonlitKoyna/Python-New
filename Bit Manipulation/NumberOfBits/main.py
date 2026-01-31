def isEvenOdd(n):
    #XOR method to check if a number is even or odd
    if (n^1==n+1):
        return True;
    else:
        return False;

number = int(input("Enter a number: "))

if isEvenOdd(number):
    print(number, "is Even")
else:
    print(number, "is Odd")
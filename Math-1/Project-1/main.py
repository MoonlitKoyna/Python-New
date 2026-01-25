def check_armstrong(number):
    digits = len(str(number))
    result = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        result += digit ** digits
        temp //= 10

    if number == result:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")


# Function to print factors of a number
def print_factors(number):
    print("Factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)


# Function to convert Roman numeral to Integer
def roman_to_integer(romanInput):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    for i in range(len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i + 1]]:
            result -= roman[romanInput[i]]
        else:
            result += roman[romanInput[i]]

    result += roman[romanInput[-1]]
    return result


# Main Program
print("Number Utility Program")
print("1. Check Armstrong Number")
print("2. Find Factors of a Number")
print("3. Convert Roman Number to Integer")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    num = int(input("Enter a number: "))
    check_armstrong(num)

elif choice == 2:
    num = int(input("Enter a number: "))
    print_factors(num)

elif choice == 3:
    roman = input("Enter a Roman numeral: ")
    print("Integer equivalent:", roman_to_integer(roman))

else:
    print("Invalid choice")

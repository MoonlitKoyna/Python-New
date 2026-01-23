# Armstrong Number
number = int(input("Enter a number: "))
digits = len(str(number))

result = 0
temp = number

while temp > 0:
    digit = temp % 10
    result = result + digit ** digits
    temp = temp // 10

if number == result:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")


# Factors of a Number
number = int(input("Enter a number to find factors: "))
print("Factors are:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)


# Roman Number to Integer
roman = input("Enter a Roman numeral: ")

roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

total = 0

for i in range(len(roman) - 1):
    if roman_values[roman[i]] < roman_values[roman[i + 1]]:
        total = total - roman_values[roman[i]]
    else:
        total = total + roman_values[roman[i]]

total = total + roman_values[roman[-1]]

print("Integer value:", total)

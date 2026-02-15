def reverseBits(number):
    result = 0

    while number > 0:
        bit = number & 1          
        result = result << 1      
        result = result | bit   
        number = number >> 1      

    return result


num = int(input("Enter a number: "))
print("Number after reversing bits:", reverseBits(num))

def mul_once(a, b):
    return a * b

def mul_loop(a, b):
    result = 0
    for i in range(b):
        result = result + a
    return result


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

ans1 = mul_once(a, b)
ans2 = mul_loop(a, b)

print("1 iteration result:", ans1)
print("N iteration result:", ans2)

def print_pairs(n):
    steps = 0

    for i in range(n):
        for j in range(n):
            steps+=1
    return steps

def single_loop(n):
    steps=0
    for i in range(n):
        steps+=1
    return steps

print("n\tO(n)\tO(n^2)")
print("-"*25)

for n in [0,5,10,20]:
    linear_steps= single_loop(n)
    quadratic_steps= print_pairs(n)
    print(f"{n}\t{linear_steps}\t{quadratic_steps}")
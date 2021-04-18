x = int(input("INPUT : "))
space = x

for i in range(x):
    space -= 1
    print(" " * space, "*" * ((i * 2) + 1))
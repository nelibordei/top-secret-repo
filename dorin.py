a = int(input("Insert a number: "))
x = 0
y = 0
while (a != 0):
    b = a % 10
    a = a // 10
    if b % 2 == 0:
        x += 1
    else:
        y += 1

print(f"in numarul dat sunt {x} cifre pare si {y} cifre impare")

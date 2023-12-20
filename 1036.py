from math import sqrt

a = float(input())
b = float(input())
c = float(input())

delta = pow(b,2) - 4*a*c

if a == 0:
    print("Impossivel calcular")
elif delta <= 0:
    print("Impossivel calcular")
else:
    r1 = (-b + sqrt(delta)) / (2 * a)
    r2 = (-b - sqrt(delta)) / (2 * a)

    print(f'R1 = {r1:.5f}' '\n'
        f'R2 = {r2:.5f}')
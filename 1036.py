from math import sqrt

while True:
    try:
        a = float(input())
        b = float(input())
        c = float(input())
        break # se a conversão for bem-sucedida, sai do loop
    except ValueError:
        print("Por favor, insira um número real válido")

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
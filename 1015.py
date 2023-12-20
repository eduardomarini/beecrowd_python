from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

delta_x = x2 - x1
delta_y = y2 - y1

distancia = sqrt(pow(delta_x, 2) + pow(delta_y, 2))

print(f'{distancia:.4f}')

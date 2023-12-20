a = float(input())
b = float(input())
c = float(input())

tri_ret = (a * c) / 2
area_cir = 3.14159 * pow(c,2)
area_tra = (a + b) * c / 2
area_qua = b * b
area_ret = a * b

print(f'TRIANGULO: {tri_ret:.3f}' '\n'
      f'CIRCULO: {area_cir:.3f}' '\n'
      f'TRAPEZIO: {area_tra:.3f}' '\n'
      f'QUADRADO: {area_qua:.3f}' '\n'
      f'RETANGULO: {area_ret:.3f}' '\n'
      )

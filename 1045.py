a = float(input())
b = float(input())
c = float(input())

a_2 = a*a
b_2 = b*b
c_2 = c*c

if a >= b + c or b >= a + c or c >= a + b:
    print("NAO FORMA TRIANGULO")
elif a_2 == b_2 + c_2 or b_2 == a_2 + c_2 or c_2 == a_2 + b_2:
    print("TRIANGULO RETANGULO")
elif a_2 > b_2 + c_2 or b_2 > a_2 + c_2 or c_2 > a_2 + b_2:
    print("TRIANGULO OBTUSANGULO")
elif a_2 < b_2 + c_2 and b_2 < a_2 + c_2 and c_2 < a_2 + b_2:
    print("TRIANGULO ACUTANGULO")

if a == b and a == c:
    print("TRIANGULO EQUILATERO")
elif a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")


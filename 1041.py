x, y = input().split(" ")
x = float(x)
y = float(y)

if x == 0:
    if y == 0:
        print("Origem")
    else:
        print("Eixo Y")
elif y == 0:
    if x == 0:
        print("Origem")
    else:
        print("Eixo X")    
elif x == 0 and y == 0:
    print("Origem")
elif x >= 0 and y >= 0:
    print("Q1")
elif x <= 0 and y >= 0:
    print("Q2")
elif x <= 0 and y <= 0:
    print("Q3")
elif x >=0 and y <= 0:
    print("Q4")
    

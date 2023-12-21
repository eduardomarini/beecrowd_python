a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

if a < b and a < c and b < c:
    print(a, '\n', b, '\n', c, '\n', '\n',
          a, '\n', b, '\n', c, '\n')
elif a < b and a < c and c < b:
    print(a, '\n', c, '\n', b, '\n', '\n',
          a, '\n', b, '\n', c, '\n')
elif b < a and b < c and a < c:
    print(b, '\n', a, '\n', c, '\n', '\n',
          a, '\n', b, '\n', c, '\n')
elif b < a and b < c and c < a:
    print(b, '\n', c, '\n', a, '\n', '\n',
          a, '\n', b, '\n', c, '\n')
elif c < a and c < b and a < b:
    print(c, '\n', a, '\n', b, '\n', '\n',
          a, '\n', b, '\n', c, '\n')
elif c < a and c < b and b < a:
    print(c, '\n', b, '\n', a, '\n', '\n',
          a, '\n', b, '\n', c, '\n')




    
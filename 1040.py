n1, n2, n3, n4 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    ne = input()
    ne = float(ne)
    print(f"Nota do exame: {ne:.1f}")
    nova_media = (ne + media) / 2
    if nova_media >= 5:
        print("Aluno aprovado.")
    elif nova_media <= 4.9:
        print("Aluno reprovado.")
    print(f"Media final: {nova_media:.1f}")

    
    

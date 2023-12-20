nome = str(input())
salario_fixo = float(input())
total_vendas = float(input())

total = (total_vendas * 0.15) + salario_fixo

print(f'TOTAL = R$ {total:.2f}')

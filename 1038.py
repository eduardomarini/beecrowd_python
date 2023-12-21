menu = [
            {"codigo" : 1, "nome" : "Cachorro quente", "valor" : 4.00},
            {"codigo" : 2, "nome" : "X-Salada", "valor" : 4.50},
            {"codigo" : 3, "nome" : "X-Bacon", "valor" : 5.00},
            {"codigo" : 4, "nome" : "Torrada simples", "valor" : 2.00},
            {"codigo" : 5, "nome" : "Refrigerante", "valor" : 1.50}
    ]
 

codigo, quantidade = input(). split(" ")
codigo = int(codigo)
quantidade = int(quantidade)

item_encontrado = None
for item in menu:
    if item["codigo"] == codigo:
        item_encontrado = item
        break
    
valor = item_encontrado["valor"]

if item_encontrado["codigo"] == codigo:
    total = quantidade * valor

print(f'Total: R$ {total:.2f}')





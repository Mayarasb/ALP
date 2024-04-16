lista2 = []
for i in range(5):
    v = int(input(f"Digite o valor {i+1}: "))
    lista2.append(v)

maior = max(lista2)
print(f"O maior valor digitado foi {maior} que está na posição {lista2.index(maior)}")
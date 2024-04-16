lista = []
lista2 = []
print("-----Lista 1-----")
for i in range(5):
    v = int(input(f"Digite o valor {i+1}:  "))
    lista.append(v)
print("-----Lista 2 -----")
for i in range(5):
    v = int(input(f"Digite o valor {i+1}: "))
    lista2.append(v)

print(lista + lista2)
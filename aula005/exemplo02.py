nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))

media = (nota1 + nota2)/2
print("Média: ", media)

if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")
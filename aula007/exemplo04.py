soma = 0
idade = 100
qnt = 0
while idade != 0:
    idade = int(input(f"Entre com a idade {qnt + 1}: "))
    if idade != 0:
        soma = soma + idade
        qnt = qnt + 1
media = soma / qnt
print(f"A média das {qnt} idades é {media:5.2f} anos.")

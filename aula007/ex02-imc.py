n = 0
soma_peso = 0
soma_altura = 0
maior_imc = 0
menor_imc = 100

imc = 0

for n in range(1, 6):
    peso = float(input(f"Digite o {n} Peso: "))
    altura = float(input(f"Digite a {n} altura: "))
    imc = peso / (altura * altura)
    soma_peso = soma_peso + peso
    soma_altura = soma_altura + altura

    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc

media_peso = soma_peso/5
media_altura = soma_altura/5

print("-------RESULTADOS-------")
print(f"Media dos pesos: {media_peso:5.2f}")
print(f"Media das alturas: {media_altura:5.2f}")
print(f"Maior Imc: {maior_imc:5.2f}")
print(f"menor imc: {menor_imc:5.2f}")






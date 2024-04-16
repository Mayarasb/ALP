from random import randint
resultados = [0]*13
frequencia = [0]*13
soma = 0
for i in range(30000):
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2
    resultados[soma] = resultados[soma] + 1

for i in range(2, 13):
    frequencia[i] = (resultados[i] / 30000)*100

for i in range(2, 13):
    print(f"{i} - {resultados[i]} - {frequencia[i]:6.2f}%")


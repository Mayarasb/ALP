primeiro_termo = 0
segundo_termo = 1
termo = int(input("Quer ver a sequência de Fibonacci até que termo: "))

print(primeiro_termo)

for i in range(1, termo-1):
    proximo_termo = primeiro_termo + segundo_termo
    print(proximo_termo)
    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo


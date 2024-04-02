n = int(input("Digite o valor de n: "))
soma = 0
for i in range(1, n + 1):
    e = (2 ** i)
    soma = soma + e
print(f"E =  {soma}")

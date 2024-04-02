n = int(input("Digite o valor de n: "))
soma = 0
i = 1
while i <= n:
    e = (2 ** i)
    soma = soma + e
    i = i + 1
print(f"E =  {soma}")

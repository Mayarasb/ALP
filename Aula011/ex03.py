idade_sobrenome = {}
for i in range (10):
    sobremone = input(f"Digite o {i} sobrenome: ")
    idade = input(f"Digite a {i}idade da pessoa: ")
    idade_sobrenome[sobremone] = idade

sobrenome_mais_velho = max(idade_sobrenome, key = idade_sobrenome.get)
print(f"O sobrenome da pessoa mais velha é: {sobrenome_mais_velho}")


ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nasc
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_anos * 52

print("Idadde em anos: ", idade_anos)
print("Idade em meses: ", idade_meses)
print("Idadde em dias: ", idade_dias)
print("Idade em semanas: ", idade_semanas)
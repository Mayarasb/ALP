nome = input("Digite seu nome completo: ")
nascimento = input("Digite a data nasc <DD/MM/AAAA ")
data = nascimento.split("/")
palavras = (nome.split())
pre_nome = palavras[0]
sobrenome = palavras[1]

print(f'Olá {pre_nome}, muito bonito seu sobrenome: {sobrenome}')
print(f"Você nasceu no dia {data[0]}, no mês {data[1]} do ano {data[2]}")
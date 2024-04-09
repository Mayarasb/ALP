data = input("Digite uma data <dd/mm/aaaa>: ")
nova_data = data.split("/")
dia = nova_data[0]
mes = nova_data[1]
ano = nova_data[2]

data_formatada = ano+mes+dia
print(f"Data formatada <AAAAMMDD> é: {data_formatada}")

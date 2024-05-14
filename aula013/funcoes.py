def valida_data(data):
    from datetime import datetime

    nova_data = data.split("/")
    dia = int(nova_data[0])
    mes = int(nova_data[1])
    ano = int(nova_data[2])

    if (dia <= 31 ) or not (1 <= mes <=12) or not (1800 <= ano <= 9999):
        print("Data inválida.")

    hoje = datetime.now().date()
    data_nasc = datetime(ano, mes, dia).date()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    if idade >= 18:
        return True
    else:
        return False

data = input("Digite sua data de nascimento: (dd/mm/aaaa)")
valida_data(data)

if valida_data(data) == False:
    print("Data inválida")
    valida_data(data)
else:
    print("eba")
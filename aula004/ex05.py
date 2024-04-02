deposito = float(input("Depósito: "))
juros = float(input("Taxa de juros: "))

rendimento = ((deposito * juros)/100)
valor_final = deposito + rendimento
print("Depósito: ", deposito)
print("Rendimento: ", rendimento)
print("Valor Final do Rendimento: ", valor_final)
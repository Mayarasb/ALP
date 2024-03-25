salario = float(input("Salário: "))
percentual = float(input("Percental do aumento: "))

aumento = ((salario * percentual)/100)
novo_salario = salario + aumento
print("Salario Antigo: ", salario)
print("Aumento: ", aumento)
print("Novo salário: ", novo_salario)
compra = float(input("Valor da Compra: "))

if compra <= 1000:
    desconto = 0.1
elif (compra >= 1001) and (compra <= 5000):
    desconto = 0.2
else:
    desconto = 0.3

valor_final = compra - (compra * desconto)

print("O desconto foi de: ", desconto)
print("O valor final foi de ", valor_final)



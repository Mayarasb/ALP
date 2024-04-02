preco_liquido = float(input("Preço líquido: "))
codigo_origem = float(input("Código: "))

if codigo_origem == 1:
    procedencia = "Sul"
    imposto = 0.11
    preco_final =  preco_liquido + (preco_liquido * imposto)

elif codigo_origem == 2:
    procedencia = "Norte"
    imposto = 0.13

elif codigo_origem == 3:
    procedencia = "Nordeste"
    imposto = 0.09

elif codigo_origem == 4:
    procedencia = "Centro-Oeste"
    imposto = 0.12

else:
    procedencia = "Sudeste"
    imposto = 0.18

preco_final =  preco_liquido + (preco_liquido * imposto)
print("Procedencia: ", procedencia)
print("Preço final: ", preco_final)


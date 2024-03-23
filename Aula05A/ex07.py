combustivel = input(" Informe (A) para Alcóol e (G) para Gasolina): ").upper()
qntlitros = float(input("Quantidade de litros : "))
if combustivel == "A":
    if qntlitros <= 20.0:
        desconto = qntlitros * 0.03
    else:
        desconto = qntlitros * 0.05
else:
    if qntlitros <= 20.0:
        desconto = qntlitros * 0.04
    else:
        desconto = qntlitros * 0.06

if combustivel == "A":
    valor = (qntlitros - desconto) * 1.9
else:
    valor = (qntlitros - desconto) * 2.5


print(f"O valor total foi de  {valor:.2f}")


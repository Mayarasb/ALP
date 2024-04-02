numero = int(input("Digite um número: "))
ctn = str
dzn = str
und = str

qntcentenas = int(numero / 100)
qntdezenas = int((numero - (qntcentenas * 100)) / 10)
qntunidades = (numero - (qntcentenas * 100) - (qntdezenas * 10))

if (qntcentenas >= 0) and (qntcentenas <= 1):
    ctn = "Centena"
else:
    ctn = "Centenas"

if (qntdezenas >= 0) and (qntdezenas <= 1):
    dzn = "Dezena"
else:
    dzn = "Dezenas"

if (qntunidades >= 0) and (qntunidades <= 1):
     und = "Unidade"
else:
    und = "Unidades"

print(numero, ":", qntcentenas, ctn,",", qntdezenas, dzn, "e", qntunidades, und)
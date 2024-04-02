ano = int(input("Digite um ano: "))
bissexto = False

if ano % 4 == 0:
    bissexto = True
    if (ano % 100 == 0) and (ano % 400 != 0):
        bissexto = False
else:
    bissexto = False

if (bissexto):
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO É BISSEXTO')




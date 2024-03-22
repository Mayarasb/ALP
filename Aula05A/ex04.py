from math import sqrt , pow

a = float(input("Digite o  valor de a: "))
b = float(input("Digite o  valor de b: "))
c = float(input("Digite o  valor de c: "))

if a == 0:
    print("Não é uma equação do segundo grau")
else:
    delta = pow(b, 2) - (4 * a * c)

    if delta < 0:
       print ("Não possui raizes reais")
    elif delta == 0:
        print("Possui apenas uma raiz")
        raiz = (-b) / (2 * a)
        print("Raiz : ", raiz)
    else:
        print("Possui duas raizes reais ")
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        print("Raiz 1 : ", raiz1)
        print("Raiz 2 : ", raiz2)






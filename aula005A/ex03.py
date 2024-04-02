l1 = int(input("Digite o primeiro lado do triângulo: "))
l2 = int(input("Digite o segundo lado do triângulo: "))
l3 = int(input("Digite o terceiro lado do triângulo: "))
if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("Pode formar um triangulo")
    if l1 == l2 == l3:
        print("Forma um triangulo equilátero")
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print("Forma um triangulo isósceles")
    elif l1 != l2 != l3:
        print("Forma um triangulo escaleno")
else:
    print("Não pode formar um triângulo")


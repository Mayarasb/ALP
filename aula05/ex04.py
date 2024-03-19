a = input("Digite o primeiro lado do triângulo: ")
b = input("Digite o segundo lado do triângulo: ")
c = input("Digite o terceiro lado do triângulo: ")
if (a + b > c) or (b + c > a) or (a + c > b):
    print("Pode formar um triangulo")
    if (a == b == c):
        print("Forma um triangulo equilátero")
    elif (a != b != c):git
        print("Forma um trangulo escaleno")
    else:
        print("Forma um triangulo isósceles")
else:
    print("Não pode forma um triângulo")
a = input("Digite o primeiro lado do triângulo: ")
b = input("Digite o segundo lado do triângulo: ")
c = input("Digite o terceiro lado do triângulo: ")
if (a < b + c) and (b < a + c) and (c < a + b):
    print("Pode formar um triangulo")
    if (a == b == c):
        print("Forma um triangulo equilátero")
    elif (a == b) or (a == c) or (b == c):
        print("Forma um triangulo isósceles")
    elif (a != b != c):
        print("Forma um trangulo escaleno")
else:
    print("Não pode formar um triângulo")
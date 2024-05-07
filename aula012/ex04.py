from math import pi,pow
def volumeEsfera(raio):
    return (4/3)*pi * pow(raio,3)

raio = float(input("Digite o raio da esfera: "))
print(f"O volume da esfera de raio {raio} é: {volumeEsfera(raio)}")


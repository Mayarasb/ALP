from math import sqrt, pow

x1 = float(input("Valor de X1: "))
y1 = float(input("Valor de Y1: "))
x2 = float(input("Valor de X2: "))
y2 = float(input("Valor de Y2: "))

dx = x2 - x1
dy = y2 - y1

distancia = sqrt(pow(dx, 2) + pow(dy, 2))

print(f"Distância : {distancia:.2f}")
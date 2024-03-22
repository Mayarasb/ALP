nota1 = float(input(" Digite sua primeira nota: "))
nota2 = float(input(" Digite sua segunda nota: "))
media_aproveitamento = str
media = (nota1 + nota2)/2
if 9.0 < media <= 10.0:
    media_aproveitamento = "A"
elif 7.5 < media <= 9.0:
    media_aproveitamento = "B"
elif 6.0 < media <= 7.5:
    media_aproveitamento = "C"
elif 4.0 < media <= 6.0:
    media_aproveitamento = "D"
else:
    media_aproveitamento = "E"

print("Nota 1:  ", nota1)
print("Nota 2:  ", nota2)
print("Média:   ", media)
print("Média de Aproveitamento: ", media_aproveitamento)

if (media_aproveitamento == "A") or (media_aproveitamento == "B") or (media_aproveitamento == "C"):
    print("APROVADO")
else:
    print("REPROVADO")

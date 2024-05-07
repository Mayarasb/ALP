from funcoes import segundos

hora = int(input("Hora: "))
min = int(input("Minutos: "))
seg = int(input("Segundos: "))

print(f" {hora}h, {min} min e {seg} segundos, correspondem a {segundos(hora,min,seg)} segundos")

degrau = float(input("Altura do degrau (cm): "))
altura = float(input("Altura dsejada (m): "))

escada = (degrau* 100) / (altura * 100)

print("Para atingir a altura de ", altura, "metros, será necessário subir", escada, "degraus de ", degrau, "cm")


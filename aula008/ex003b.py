frase = input("Digite uma frase: ")
a = frase.count("a")
e = frase.count("e")
i = frase.count("i")
o = frase.count("o")
u = frase.count("u")
vogais = a + e + i + o + u

print(f"Tem {vogais} vogais na frase: {frase}")
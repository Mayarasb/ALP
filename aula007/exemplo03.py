frase = input("Digite uma frase: ")
qnt = 0

for caracter in frase:
    if caracter in 'AEIOUaeiouáéíóàãü':
        qnt = qnt + 1
print(f"Na frase tem {qnt} vogais na frase.")

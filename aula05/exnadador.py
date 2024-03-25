idade = int(input("Digite sua idade: "))

if  5 <= idade <=7 :
    print("Categoria: Infantil")
elif 8 <= idade <= 10 :
    print("Categoria: Juvenil")
elif 11 <= idade <= 15 :
    print("Categoria: Adolescente")
elif 16 <= idade <= 30 :
    print("Categoria: Adulto")
else:
    print("Categoria: Senior")
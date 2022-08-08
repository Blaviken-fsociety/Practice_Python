#mayor que el anterior

valor = int(input("¿cuantos valores va a introducir? \n "))
if valor < 1:
    print("Error")
else:
    primero = int(input("escriba un numero: "))
    for i in range(valor - 1):
        numero = int(input(f"Escriba un numero mas grande que {primero}: "))
        if numero <= primero:
            print(f"{numero} no es mayor que {primero}")
        primero = numero
    print("Gracias por su colaboración")
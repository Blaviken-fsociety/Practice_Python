nombre_1 = "Madeleyne"
nombre_2 = "Pedro"
nombre_3 = "Juan"
nombre_4 = "Jesus"

# Lista de nombres
mi_lista_1 = ["Madeleyne", "Pedro", "Juan", "Jesus"]

# Lista de numeros
mi_lista_2 = [10, 25, 30, 40]

# Lista de nombres y numeros
mi_lista_3 = ["Madeleyne", 10,"Hola123"]

#--------------------------------------------------------

mi_lista = [] # Es una lista vacia

#--------------------------------------------------------

# a) Estáticas

frutas = ["Manzana", "Pera", "Uvas"]
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[-1])

print(len(frutas))

# B) Dinámicas

animales = []
cantidad = eval(input("¿Cuantos animales quieres?: "))

for i in range(cantidad):
    x = input("Dime un animal: ")
    animales.append(x)

print(animales)
#--------------------------------------------------------

i = 0
while i < cantidad:
    x = input("Dime un animal: ")
    animales.append(x)
    i += 1
    
print(animales)

#--------------------------------------------------------

frutas = ["Manzana", "Pera", "Uvas", "Manzana", "Pera", "Uvas", "Manzana", "Pera", "Uvas"]

for i in range(2):
    print(frutas[i])

i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1
animales = []
cantidad = eval(input("¿Cuantos animales quieres?: "))

for i in range(cantidad):
    x = input("Dime un animal: ")
    animales.append(x)

print(animales)
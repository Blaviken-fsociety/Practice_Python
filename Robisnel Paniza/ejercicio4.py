m4 = []
f4 = 10
c4 = 10

for i in range(f4):
    m4.append([])
    for j in range(c4):
        x = int(input(f"Ingrese el elemento matriz[{i}][{j}]: "))
        m4[i].append(x)

print("\nResultado:\n")
for i in range(f4):
    for j in range(c4):
        print(f"{m4[i][j]}", end=" ")
    print("")

mayor = m4[0][0]

for i in range(f4):
    for j in range(c4):
        if m4[i][j] > mayor:
            mayor = m4[i][j]
            puesto = f"[{i}][{j}]"
print(f"El número mayor es {mayor}")
print(f"Y su posición es {puesto}")

print("\nBy Robisnel Paniza\n")
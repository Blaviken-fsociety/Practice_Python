m2 = []

f2 = int(input("Ingrese la cantidad de filas: "))

for i in range(f2):
    m2.append([])
    for j in range(2):
        x = int(input(f"Ingrese el elemento fila {i} columna {j}: "))
        m2[i].append(x)

for i in range(f2):
    x = m2[i][0] + m2[i][1]
    m2[i].append(x)

print("\nResultado:\n")
for i in range(f2):
    for j in range(len(m2[0])):
        print(f"{m2[i][j]}", end=" ")
    print("")

print("\nBy Robisnel Paniza\n")
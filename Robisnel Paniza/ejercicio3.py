m3 = []

f3 = 5
c3 = 6

for i in range(f3):
    m3.append([])
    for j in range(c3):
        x = int(input(f"Ingrese el elemento matriz[{i}][{j}]: "))
        m3[i].append(x)

print("\nResultado:\n")
for i in range(f3):
    for j in range(c3):
        print(f"{m3[i][j]}", end=" ")
    print("")

acum = 0
for i in range(f3):
    for j in range(c3):
        acum = acum + m3[i][j]
print(f"La suma de los números almacendos es: {acum}")

print("\nBy Robisnel Paniza\n")
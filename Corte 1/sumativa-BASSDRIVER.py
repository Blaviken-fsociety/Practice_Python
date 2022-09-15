filas=int(input("Ingrese el numero de filas"))
columnas=int(input("Ingrese el numero de columnas"))
matriz=[]

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor=float(input ("Fila {}, Columna {}:".format(i+1,j+1)))
        matriz[i].append(valor)

print()

for columnas in matriz:
    print("[", end= "")

for elemento in columnas:
    print("{:8.2f}".format(elemento), end=" ")

    print("]")
print("")

con=0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if(i>j):
            print(matriz[i][j])
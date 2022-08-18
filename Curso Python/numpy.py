import numpy as np

#Crear matriz dinámica con numpy

filas=int(input("Ingrese la cantidad de Filas: "))
columnas=int(input("Ingrese la cantidad de Columnas: "))
m2 = np.zeros([filas, columnas])
for i in range(filas):
    for j in range(columnas):
        x=eval(input(f"Ingrese un elemento en la pos [{i}][{j}]: "))
        m2[i][j]= int(x)
print(m2)

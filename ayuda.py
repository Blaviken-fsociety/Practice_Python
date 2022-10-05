if __name__ == '__main__':

# Definir variables
    fila = int()

    columna = int()

    matriz = int()

    contadorceros = int()

    contadornegativos = int()

    contadorpositivos = int()

    contadorceros = 0

    contadornegativos = 0

    contadorpositivos = 0

# Definir tamaño de la matriz
print("Ingrese tamaño de la fila")

while True:# no hay 'repetir' en python

 fila = int(input())

 if fila<=0:

  print("No se puede realizar la operación")

 if fila>0: break

print("Ingrese tamaño de la columna")

while True:# no hay 'repetir' en python

 columna = int(input())

 if columna<=0:

  print("No se puede realizar la operación")

 if columna>0: break

matriz = [[int() for ind0 in range(columna)] for ind1 in range(fila)]

# Ingresar los elementos de la matriz
print("Ingrese elementos de la matriz")

for f in range(1,fila+1):

 for c in range(1,columna+1):

  print("Elemento ( ",f," .",c," ): ")

  matriz[f-1][c-1] = int(input())

# Recorrer matriz para encontrar ceros, positivos, y negativos
for f in range(1,fila+1):

 for c in range(1,columna+1):

  if matriz[f-1][c-1]==0:

   contadorceros = contadorceros+1

  if matriz[f-1][c-1]<0:

   contadornegativos = contadornegativos+1

  if matriz[f-1][c-1]>0:

   contadorpositivos = contadorpositivos+1

# Imprimer resultados
print("La matriz tiene ",contadorceros," ceros")
print("La matriz tiene ",contadornegativos," elementos negativos")

print("La matriz tiene ",contadorpositivos," elementos positivos")


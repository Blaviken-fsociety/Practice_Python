if __name__ == '__main__':

# Definir variables
    matriz = str()

    filas = int()

print("Ingrese Cantidad de estudiantes a registrar")

while True:# no hay 'repetir' en python

    filas = int(input())

    if filas<=0:

        print("Ingreso invalido")

    if filas>0: break

matriz = [[str() for ind0 in range(6)] for ind1 in range(filas)]

# Ingresar los elementos de la matriz
print("Ingrese datos de los estudiantes")

for f in range(1,filas+1):
# Ingreso de datos id, nombre, apellido, nota1, nota2, nota3
 
    print("Id del alumno: ",f, end="")

    matriz[f-1][0] = input()

    print("Nombre del alumno: ",f, end="")

    matriz[f-1][1] = input()

    print("Apellido del alumno: ",f, end="")

    matriz[f-1][2] = input()

    print("Nota1 del alumno: (0-5)",f, end="")

    while True:# no hay 'repetir' en python

        matriz[f-1][3] = input()

        nota = float(matriz[f-1][3])

        if (nota<0) or (nota>5):

            print("ingreso inválido, intente de nuevo")

        if (nota>=0) and (nota<=5): break

    print("Nota2 del alumno: (0-5) ",f, end="")

    while True:# no hay 'repetir' en python

        matriz[f-1][4] = input()

        nota = float(matriz[f-1][4])

        if (nota<0) or (nota>5):

            print("ingreso inválido, intente de nuevo ")

        if (nota>=0) and (nota<=5): break

    print("Nota3 del alumno:(0-5)",f, end="")

    while True:# no hay 'repetir' en python

        matriz[f-1][5] = input()

        nota = float(matriz[f-1][5])

        if (nota<0) or (nota>5):

            print("ingreso inválido, intente de nuevo ")

        if (nota>=0) and (nota<=5): break

# Recorrer matriz para encontrar ceros, positivos, y negativos
    for f in range(1,filas+1):
        print(" alumno ",f)

        print(" Id: ",matriz[f-1][0]," Nombre: ",matriz[f-1][1]," Apellido: ",matriz[f-1][2])

        nota1 = float(matriz[f-1][3])

        nota2 = float(matriz[f-1][4])

        nota3 = float(matriz[f-1][5])

        promedio = (nota1+nota2+nota3)/3

        if promedio<3:
# Mostrar si mensaje de aprobado o reprobado, el valor de promedio con dos decimales, y las tres notas
            print(" Alumno Reprobado"," Promedio: ",round(promedio*100)/100," Nota1: ",nota1," Nota2: ",nota2," Nota3: ",nota3)
        else:
            print(" Alumno Aprobado"," Promedio: ",round(promedio*100)/100," Nota1: ",nota1," Nota2: ",nota2," Nota3: ",nota3)
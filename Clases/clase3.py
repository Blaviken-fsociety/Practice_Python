
#Definir la cantidad de filas y columnas

m1 =[[-1,2,3],[4,-5,6],[7,8,9]]
print (m1)

print("m1[0][0]: ", m1[0][0]) #Primera posición
print("m1[2][2]: ", m1[2][2]) #Última posición
print("Sumatoria de de elementos columna 0: ", m1[0][0]+m1[1][0]+m1[2][0]) #Sumatoria de de elementos columna 0

#Somatoria de elementos de la matriz
print("filas: ", len(m1))
print("columnas: ", len(m1[1]))

acum=0
for i in range(len(m1)):
    for j in range(len(m1[0])):
        acum=acum+m1[i][j]
print("Sumatoria de elementos: ", acum)

#Elemento mayor y menor

mayor=m1[0][0]
menor=m1[0][0]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        if m1[i][j]>mayor:
            mayor= m1[i][j]
        if m1[i][j]<menor:
            menor= m1[i][j]
print ("El elemento mayor",mayor)
print ("El elemento menor",menor)

#Cantidad de numeros pos y nega

contpos=0
contneg=0
for i in range(len(m1)):
    for j in range(len(m1[0])):
        if m1[i][j]<0:
            contneg=contneg+1
        else:
            contpos=contpos+1
print("Los numero negativos son: ",contneg)
print("Los numero positivos son: ",contpos)

################################################################################################################
#Matriz dinámica
################################################################################################################

#1. definir filas y columnas
filas=int(input("Ingrese la cantidad de Filas: "))
columnas=int(input("Ingrese la cantidad de Columnas: "))

#2. crear listas
m2=[]

#3. llenar la lista
for i in range(filas):
    m2.append([])
    for j in range(columnas):
        valor=int(input(f"Ingrese un elemento en la pos [{i}][{j}]: "))
        m2[i].append(valor)
print("- - - - - - - - - - - - - - - - - -")
print(m2)
print("- - - - - - - - - - - - - - - - - -")
#Promedio de los elementos

acum2=0
cont=0
for i in range (len(m1)):
    for j in range(len(m1[0])):
        acum=acum+i
promedio=acum/m1[i][j]
print("El promedio de los elementos es: ",promedio)
print("- - - - - - - - - - - - - - - - - -")

#retorne la sumatoria de la diagonal principal de la matriz

sumato_prin=0
for i in range(len(m2)):
    for j in range(len(m2[0])):
        if j == i:
            sumato_prin=sumato_prin+m2[i][j]
print(f"Sumatoria de diagonal principal: {sumato_prin}")
print(" ")

#principal es mayor o no que la diagonal secundaria

sumato_secu=0
j=0
for i in range(len(m2)):
    sumato_secu=sumato_secu+m2[i][len(m2[0])- 1 -j]
    j=j+1
print(f"Sumatoria de diagonal secundaria: {sumato_secu}")
print(" ")
if sumato_prin > sumato_secu:
    print("La diagonal principal es mayor")
    print(" ")
elif sumato_prin < sumato_secu:
    print("La diagonal secundaria es mayor")
    print(" ")
else:
    print("Las dos diagonales tienen el mismo valor")
    print(" ")

################################################################
#Letras
################################################################

m_u = [["x"," "," "," ","x"], ["x"," "," "," ","x"], ["x"," "," "," ","x"], ["x"," "," "," ","x"], ["x","x","x","x","x"]]
m_o = [["x","x","x","x","x"], ["x"," "," "," ","x"], ["x"," "," "," ","x"], ["x"," "," "," ","x"], ["x","x","x","x","x"]]
m_l = [["x"," "," "," "," "], ["x"," "," "," "," "], ["x"," "," "," "," "], ["x"," "," "," "," "], ["x","x","x","x","x"]]
m_n = [["x"," "," "," ","x"], ["x","x"," "," ","x"], ["x"," ","x"," ","x"], ["x"," "," ","x","x"], ["x"," "," "," ","x"]]
m_c = [["x","x","x","x","x"], ["x"," "," "," "," "], ["x"," "," "," "," "], ["x"," "," "," "," "], ["x","x","x","x","x"]]
m_x = [["x"," "," "," ","x"], [" ","x"," ","x"," "], [" "," ","x"," "," "], [" ","x"," ","x"," "], ["x"," "," "," ","x"]]
m_z = [["x","x","x","x","x"], [" "," "," ","x"," "], [" "," ","x"," "," "], [" ","x"," "," "," "], ["x","x","x","x","x"]]

for i in range (len(m_u)):
    for j in range(len(m_u)):
        print(m_u[i][j],end=" ")
    print("")
print("============================================================")

for i in range (len(m_o)):
    for j in range(len(m_o)):
        print(m_o[i][j],end=" ")
    print("")

print("============================================================")

for i in range (len(m_l)):
    for j in range(len(m_l)):
        print(m_l[i][j],end=" ")
    print("")

print("============================================================")

for i in range (len(m_n)):
    for j in range(len(m_n)):
        print(m_n[i][j],end=" ")
    print("")

print("============================================================")

for i in range (len(m_c)):
    for j in range(len(m_c)):
        print(m_c[i][j],end=" ")
    print("")

print("============================================================")

for i in range (len(m_x)):
    for j in range(len(m_x)):
        print(m_x[i][j],end=" ")
    print("")

print("============================================================")

for i in range (len(m_z)):
    for j in range(len(m_z)):
        print(m_z[i][j],end=" ")
    print("")

print("============================================================",end=" ")

print("@By Blaviken-fsociety")
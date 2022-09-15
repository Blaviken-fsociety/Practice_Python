#Ejercicio 1
#Juan Pablo Conde
columnas=10
filas=int(input("Ingresa la cantidad de datos a registrar: "))
mventas=[]
for i in range(filas):
    mventas.append([])
    for j in range(columnas):
        if j==0:
            id=int(input("Digite la ID del producto: "))
            mventas[i].append(id)
        if j==1:
            dia=int(input("Digite el dia: "))
            mventas[i].append(dia)
        if j==2:
            mes=int(input("Digite el mes: "))
            mventas[i].append(mes)
        if j==3:
            año=int(input("Digite el año: "))
            mventas[i].append(año)
        if j==4:
            cc=eval(input("Digite el numero de documento del cliente: "))
            mventas[i].append(cc)
        if j==5:
            nombre=input("Ingrese el nombre del cliente: ")
            mventas[i].append(nombre)
        if j==6:
            producto=input("Ingrese el producto comprado: ")
            mventas[i].append(producto)
        if j==7:
            cantidad=int(input("Ingrese la cantidad de producto comprado: "))
            mventas[i].append(cantidad)
        if j==8:
            valoru=eval(input("Digite el valor unitario del producto que compro: "))
            mventas[i].append(valoru)
        if j==9:
            valort=cantidad*valoru
            mventas[i].append(valort)
print(mventas)

#calcule el total de ventas
i=0
acumuladort=0
while i < len(mventas):
    print(mventas[i][9])
    acumuladort = acumuladort + mventas[i][9]
    i=i+1
print("El total de ventas es igual a= ",acumuladort)

#calcule el producto mas vendido


#calcule promedio de ventas en un mes y año especificado
año=int(input("Ingrese año a buscar: "))
mes=int(input("Ingrese mes a buscar: "))

acumulador = 0
contador = 0

i = 0
while i < filas:

    if año==mventas[i][3] and mes == mventas[i][2]:
        acumulador = acumulador + mventas[i][9]
        contador = contador + 1
    i = i + 1
print("")

if contador != 0:
    promedio = round(acumulador / contador, 2)
    print(f"Promedio ventas de año {año} mes {mes}: {promedio}")
else:
    print("No hubo ventas en esa fecha...")
    print(f"Promedio ventas de año {año} mes {mes}: 0")

#año con mayores ventas
print("Años registrados:")
l_años = []
i = 0
while i < filas:
    if mventas[i][3] not in l_años:
        l_años.append(mventas[i][3])
    i = i + 1 

v_años = []
acumulador = 0
i = 0
while i < len(l_años):

    j = 0
    while j < filas:
        if l_años[i] == mventas[j][3]:
            acumulador = acumulador + mventas[j][9]
        j = j + 1
    v_años.append(acumulador)
    acumulador = 0
    i = i + 1

i = 0
while i < len(l_años):
    print(f"{i + 1}. {l_años[i]} (ventas ${v_años[i]})")
    i = i + 1

mayor_venta = v_años[0]
nombre_año = l_años[0]

i = 0
while i < len(v_años):
    if v_años[i] > mayor_venta:
        mayor_venta = v_años[i]
        nombre_año = l_años[i]
    i = i + 1

contador = 0
i = 0 
while i < len(v_años):
    if v_años[i] == mayor_venta:
        contador = contador + 1
    i = i + 1
print("")

if contador == 1:
    print("Año con más ventas:")
    print(f"{nombre_año} (ventas ${mayor_venta})")
else:
    print("¡Hay máximos iguales!")
    print("Años con mayor ventas: ")
    i = 0
    while i < len(v_años):
        if v_años[i] == mayor_venta:
            print(f"{l_años[i]} (ventas ${mayor_venta})")
        i = i + 1

#mes con mayores ingresos
print("Meses registrados:")

lista_meses = []

i = 0
while i < filas:
    if mventas[i][2] not in lista_meses:
        lista_meses.append(mventas[i][2])
    i = i + 1 

ventas_meses = []
acumulador = 0
i = 0
while i < len(lista_meses):

    j = 0
    while j < filas:
        if lista_meses[i] == mventas[j][2]:
            acumulador = acumulador + mventas[j][9]
        j = j + 1

    ventas_meses.append(acumulador)
    acumulador = 0
    i = i + 1

i = 0
while i < len(lista_meses):
    print(f"{i + 1}. {lista_meses[i]} (ventas ${ventas_meses[i]})")
    i = i + 1

mayor_venta = ventas_meses[0]
nombre_mes = lista_meses[0]

i = 0
while i < len(ventas_meses):
    if ventas_meses[i] > mayor_venta:
        mayor_venta = ventas_meses[i]
        nombre_mes = lista_meses[i]
    i = i + 1

contador = 0
i = 0 
while i < len(ventas_meses):
    if ventas_meses[i] == mayor_venta:
        contador = contador + 1
    i = i + 1
print("")

if contador == 1:
    print("Mes con más ventas:")
    print(f"{nombre_mes} (ventas ${mayor_venta})")
else:
    print("¡Hay máximos iguales!")
    print("Meses con mayor ventas: ")
    i = 0
    while i < len(ventas_meses):
        if ventas_meses[i] == mayor_venta:
            print(f"{l_años[i]} (ventas ${mayor_venta})")
        i = i + 1

#buscar un cliente por cedula
cc_buscar = int(input("Ingrese CC a buscar: "))

encontrado = False
i = 0
while i < filas:
    if cc_buscar == mventas[i][4]:
        encontrado = True

    i = i + 1
if encontrado == False:
    print("Cliente no encontrado...")
else:
    print("¡Cliente encontrado!")
    i = 0
    while i < filas:
        if cc_buscar == mventas[i][4]:
            print(f"Nombre: {mventas[i][5]}")
        i = i + 1
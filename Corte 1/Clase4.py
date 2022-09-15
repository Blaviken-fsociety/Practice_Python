colum=10
filas= int(input("ingrese la cantidad de ventas a registrar: "))
mventas=[]

for i in range(filas):
    mventas.append([])
    for j in range(colum):
            if j==0:
                id=int(input("Id: "))
                mventas[i].append(id)
            if j==1:
                dia=int(input("Dia (1, 2, 3, 4...: "))
                mventas[i].append(dia)
            if j==2:
                mes=int(input("Mes (1-12): "))
                mventas[i].append(mes)
            if j==3:
                año=int(input("Año: "))
                mventas[i].append(año)
            if j ==4:
                cedula=eval(input("No. Identificación: "))
                mventas[i].append(cedula)
            if j ==5:
                nombre=input("Digite Nombre del cliente: ")
                mventas[i].append(nombre)
            if j ==6:
                producto=input("Digite el Nombre del producto: ")
                mventas[i].append(producto)
            if j ==7:
                cantidad=int(input("Cantidad: "))
                mventas[i].append(cantidad)
            if j ==8:
                valor_unitario=int(input("Digite el Valor Unitario del producto: "))
                mventas[i].append(valor_unitario)
            if j ==9:
                total=cantidad*valor_unitario
                mventas[i].append(total)
    print("Proxima venta")
print(mventas)

#Calcula todas las ventas
i=0
acumulador_total=0
while i< len(mventas):
    print(mventas[i][9])
    acumulador_total+=acumulador_total+mventas[i][9]
    i+=1
print("Total de la venta: ", acumulador_total)
#calcule el producto mas vendido


#calcule promedio de ventas en un mes y año especificado
año=int(input("Ingrese año a buscar: "))
mes=int(input("Ingrese mes a buscar: "))

acum = 0
cont = 0

i = 0
while i < filas:

    if año==mventas[i][3] and mes == mventas[i][2]:
        acum = acum + mventas[i][9]
        cont = cont + 1
    i = i + 1
print("")

if cont != 0:
    promedio = round(acum / cont, 2)
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
acum = 0
i = 0
while i < len(l_años):

    j = 0
    while j < filas:
        if l_años[i] == mventas[j][3]:
            acum = acum + mventas[j][9]
        j = j + 1
    v_años.append(acum)
    acum = 0
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

cont = 0
i = 0 
while i < len(v_años):
    if v_años[i] == mayor_venta:
        cont = cont + 1
    i = i + 1
print("")

if cont == 1:
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
acum = 0
i = 0
while i < len(lista_meses):

    j = 0
    while j < filas:
        if lista_meses[i] == mventas[j][2]:
            acum = acum + mventas[j][9]
        j = j + 1

    ventas_meses.append(acum)
    acum = 0
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

cont = 0
i = 0 
while i < len(ventas_meses):
    if ventas_meses[i] == mayor_venta:
        cont = cont + 1
    i = i + 1
print("")

if cont == 1:
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


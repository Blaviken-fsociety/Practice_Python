ventas = []

lista_productos = ["Arroz", "Pastas", "Manzana", "Lentejas", "Uvas"]
lista_precios = [2500, 1600, 3000, 2300, 4000]
lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
listas_cc = []

print("- - SISTEMA DE VENTAS - -")
cantidad_registros = eval(input("Ingrese la cantidad de registros: "))

i = 0
while i < cantidad_registros:
    ventas.append([])

    dia = int(input(f"Ingrese el día (Cliente {i+1}): "))
    mes = int(input(f"Ingrese el mes (Cliente {i+1}): "))

    while mes > len(lista_meses) or mes < 1:
        print("Datos no validos...")
        mes = int(input(f"Ingrese el mes (Cliente {i+1}): "))

    mes = lista_meses[mes - 1]
    año = int(input(f"Ingrese el año (Cliente {i+1}): "))

    cc = int(input(f"Ingrese la CC (Cliente {i+1}): "))
    while cc in listas_cc:
        print("CC Repetida...")
        cc = int(input(f"Ingrese la CC (Cliente {i+1}): "))
    listas_cc.append(cc)

    nombre_cliente = input(f"Ingrese el nombre cliente (Cliente {i+1}): ")

    x = 0
    while x < len(lista_productos):
        print(f"{x + 1} = {lista_productos[x]}")
        x = x + 1
    producto = int(input(f"Ingrese el producto (Cliente {i+1}): "))

    while producto > len(lista_productos) or producto < 1:
        print("Datos no validos...")
        producto = int(input(f"Ingrese el producto (Cliente {i+1}): "))

    cantidad = int(input(f"Ingrese la cantidad (Cliente {i+1}): "))

    while cantidad < 1:
        print("Datos no validos...")
        cantidad = int(input(f"Ingrese la cantidad (Cliente {i+1}): "))
  
    valor_unitario = lista_precios[producto - 1]
    producto = lista_productos[producto - 1]
    total = cantidad * valor_unitario
    print("- - - -")

    ventas[i].append(i + 1)
    ventas[i].append(dia)
    ventas[i].append(mes)
    ventas[i].append(año)
    ventas[i].append(cc)
    ventas[i].append(nombre_cliente)
    ventas[i].append(producto)
    ventas[i].append(cantidad)
    ventas[i].append(valor_unitario)
    ventas[i].append(total)

    i = i + 1

print(ventas)

print("- - - -")
total_ventas = 0

i = 0
while i < cantidad_registros:

    total_ventas = total_ventas + ventas[i][9]

    i = i + 1

print(f"Total de ventas: ${total_ventas}")

print("- - - -")
print("Productos vendidos:")

conteo_productos = []
contador = 0
i = 0
while i < len(lista_productos):

    j = 0
    while j < cantidad_registros:
        if lista_productos[i] == ventas[j][6]:
            contador = contador + 1
        j = j + 1

    conteo_productos.append(contador)
    contador = 0
    i = i + 1

i = 0
while i < len(lista_productos):
    print(f"{i + 1}. {lista_productos[i]} (cantidad {conteo_productos[i]})")
    i = i + 1

mas_vendido = conteo_productos[0]
nombre_producto = lista_productos[0]

i = 0
while i < len(conteo_productos):
    if conteo_productos[i] > mas_vendido:
        mas_vendido = conteo_productos[i]
        nombre_producto = lista_productos[i]
    i = i + 1

contador = 0
i = 0 
while i < len(conteo_productos):
    if conteo_productos[i] == mas_vendido:
        contador = contador + 1
    i = i + 1
print("")

if contador == 1:
    print("Producto más vendido:")
    print(f"{nombre_producto} (cantidad {mas_vendido})")
else:
    print("¡Hay máximos iguales!")
    print("Los más vendidos fueron: ")
    i = 0
    while i < len(conteo_productos):
        if conteo_productos[i] == mas_vendido:
            print(f"{lista_productos[i]} (cantidad {mas_vendido})")
        i = i + 1

print("- - - -")
año_buscar = int(input("Ingrese año a buscar: "))
mes_buscar = int(input("Ingrese mes a buscar: "))

acumulador = 0
contador = 0

i = 0
while i < cantidad_registros:

    if año_buscar == ventas[i][3] and mes_buscar == ventas[i][2]:
        acumulador = acumulador + ventas[i][9]
        contador = contador + 1
    i = i + 1
print("")


if contador != 0:
    promedio = round(acumulador / contador, 2)
    print(f"Promedio ventas de año {año_buscar} mes {mes_buscar}: ${promedio}")
else:
    print("No hubo ventas en esa fecha...")
    print(f"Promedio ventas de año {año_buscar} mes {mes_buscar}: $0")
print("- - - -")
print("Años registrados:")

lista_años = []

i = 0
while i < cantidad_registros:
    if ventas[i][3] not in lista_años:
        lista_años.append(ventas[i][3])
    i = i + 1 

ventas_años = []
acumulador = 0
i = 0
while i < len(lista_años):

    j = 0
    while j < cantidad_registros:
        if lista_años[i] == ventas[j][3]:
            acumulador = acumulador + ventas[j][9]
        j = j + 1

    ventas_años.append(acumulador)
    acumulador = 0
    i = i + 1

i = 0
while i < len(lista_años):
    print(f"{i + 1}. {lista_años[i]} (ventas ${ventas_años[i]})")
    i = i + 1

mayor_venta = ventas_años[0]
nombre_año = lista_años[0]

i = 0
while i < len(ventas_años):
    if ventas_años[i] > mayor_venta:
        mayor_venta = ventas_años[i]
        nombre_año = lista_años[i]
    i = i + 1

contador = 0
i = 0 
while i < len(ventas_años):
    if ventas_años[i] == mayor_venta:
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
    while i < len(ventas_años):
        if ventas_años[i] == mayor_venta:
            print(f"{lista_años[i]} (ventas ${mayor_venta})")
        i = i + 1
print("- - - -")
print("Meses registrados:")
lista_meses = []

i = 0
while i < cantidad_registros:
    if ventas[i][2] not in lista_meses:
        lista_meses.append(ventas[i][2])
    i = i + 1 

ventas_meses = []
acumulador = 0
i = 0
while i < len(lista_meses):

    j = 0
    while j < cantidad_registros:
        if lista_meses[i] == ventas[j][2]:
            acumulador = acumulador + ventas[j][9]
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
            print(f"{lista_años[i]} (ventas ${mayor_venta})")
        i = i + 1

print("- - - -")
cc_buscar = int(input("Ingrese CC a buscar: "))

encontrado = False
i = 0
while i < cantidad_registros:
    if cc_buscar == ventas[i][4]:
        encontrado = True
    i = i + 1

if encontrado == False:
    print("Cliente no encontrado...")
else:
    print("¡Cliente encontrado!")
    i = 0
    while i < cantidad_registros:
        if cc_buscar == ventas[i][4]:
            print(f"Nombre: {ventas[i][5]}")
        i = i + 1
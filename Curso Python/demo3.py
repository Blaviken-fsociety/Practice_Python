def run():
    #Base de Datos
    inventario = []
    #Mensaje
    print("Bienvenidos al programa!")
    print("Seleccione una opción!")
    #opciones
    print("1 - para añadir una fila")
    print("2 - para ver el total de las ventas")
    print("3 - para ver el producto mas vendido")
    print("4 - para ver el promedio de un año y mes especifico")
    print("4 - para SALIR del programa\n")
    opc = int(input("Ingrese la opción: "))    

    # Variable a añandir datos
    ingresar = []
    #dirigir opciones
    if opc == 1:
        #ingresar datos
        dia =  int(input("Ingresa el Día: "))
        ingresar.append(dia) 
        mes =  int(input("Ingresa el Mes: "))
        ingresar.append(mes)
        anio = int(input("Ingresar el Año: "))
        ingresar.append(anio)
        cc = str(input("Ingresar Cedula de ciudadanía: "))
        ingresar.append(cc)
        nombre = str(input("Ingresar el nombre y el apellido: "))
        ingresar.append(nombre)
        producto = str(input("Ingresar el nombre del producto: "))
        ingresar.append(producto)
        cant = int(input("Ingrese la cantidad: "))
        ingresar.append(cant)
        valor_unitario = int(input("Ingresar el valor unitario: "))
        ingresar.append(valor_unitario)
        total = int(input("Ingresar el valor Total: "))
        ingresar.append(total)

        #Ingresarlo a la Base de Datos
        inventario.append(ingresar)
        
    elif opc == 2:
        # calcular todas las ventas
        cant_total = 0
        for indice, valor in enumerate(inventario):
            cant_total = cant_total + valor[8]
        print(f"El total de las ventas es de {cant_total}")


    elif opc == 3:
        # Producto mas vendido 
        mayor = 0
        ind = 0
        for indice, valor in enumerate(inventario):
            if valor[8] > mayor or mayor == 0:
                mayor = valor[8]
                ind = valor[5]
        print(f"El producto mas vendido es {ind} con una suma de {mayor}")
            
    elif opc == 4:
        add_mes = int(input("Ingresar el mes interesado!: ")) 
        add_anio = int(input("Ingresar el Año interesado!: "))
        #Calcular ventas de un año y mes especificado
        def calcular_venta(anio, mes):
            prom = 0
            count = 0
            for indice, valor in enumerate(inventario):
                if anio == valor[2] and mes == valor[1]:
                    prom = prom + valor[8]
                    count += 1
            while True:
                try:        
                    promedio = round((prom / count),2)
                    break
                except ZeroDivisionError:
                    print("no existe ningún mes filtrado!! \n Intentarlo nuevamente")
                    add_mes = int(input("Ingresar el mes interesado!: ")) 
                    add_anio = int(input("Ingresar el Año interesado!: "))
            #Retorno
            return print(f"El promedio para el año {anio} y mes {mes} es de {promedio}")

        # probando nuestra funcion
        # año 2022 y mes 6 de prueba
        calcular_venta(add_anio, add_mes)



if __name__ == '__main__':
    run()
columnas=10
filas= int(input("ingrese la cantidad de ventas a registrar: "))
mventas=[]

for i in range(filas):
    mventas.append([])
    for j in range(columnas):
            if j==0:
                id=int(input("Id: "))
                mventas[i].append(id)
            if j==1:
                dia=int(input("Dia (Lunes-1, Martes-2...Domingo-7: "))
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
i=0
acumulador_total=0
while i< len(mventas):
    print(mventas[i][9])
    acumulador_total+=acumulador_total+mventas[i][9]
    i+=1
print("Ventas totales: ", acumulador_total)
           
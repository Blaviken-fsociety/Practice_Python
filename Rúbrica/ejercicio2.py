a="\n"

print("Indicador 3")
print(a)

class Ventas():
    def __init__(self):
        self.__ventas = []

    def setVentas(self, x:list):
        self.__ventas = x

    def getVentas(self):
        return self.__ventas

    def llenarDatos(self):
        print("Llenar Datos: ")
        print(a)
        filas = int(input("Ingrese la cantidad de filas: "))
        for i in range(filas):
            self.getVentas().append([])
            for j in range(8):
                if j == 0:
                    id = int(input(f"Ingrese Id del cliente {i + 1}: "))
                    self.getVentas()[i].append(id)

                if j == 1:
                    producto = input(f"Ingrese producto que compró el cliente {i + 1}: ")
                    self.getVentas()[i].append(producto)

                if j == 2:
                    cantidad = int(input(f"Ingrese la cantidad que llevó el cliente {i + 1}: "))
                    self.getVentas()[i].append(cantidad)

                if j == 3:
                    valor_unitario = eval(input(f"Ingrese valor unitario del producto llevado por el cliente {i + 1}: "))
                    self.getVentas()[i].append(valor_unitario)

                if j == 4:
                    total = valor_unitario * cantidad
                    self.getVentas()[i].append(total)

                if j == 5:
                    dia = int(input(f"Ingrese día: "))
                    self.getVentas()[i].append(dia)

                if j == 6:
                    mes = int(input(f"Ingrese mes: "))
                    self.getVentas()[i].append(mes)

                if j == 7:
                    año = int(input(f"Ingrese año: "))
                    self.getVentas()[i].append(año)
            print(a)

    def mostrarDatos(self):
        print("Datos suministrados")
        print(a)
        for i in range(len(self.getVentas())):
            print(f"{i+1}. Id: {self.getVentas()[i][0]} || Producto: {self.getVentas()[i][1]} || Cantidad: {self.getVentas()[i][2]} || Valor unitario: ${self.getVentas()[i][3]} || Total: ${self.getVentas()[i][4]} || Día: {self.getVentas()[i][5]} || Mes: {self.getVentas()[i][6]} || Año: {self.getVentas()[i][7]}")
        print(a)

    def productoMasVendidoMes(self):
        print("Producto mas vendido")
        print(a)
        mes_buscar = int(input("Ingrese mes a buscar: "))

        encontrado = False
        for i in range(len(self.getVentas())):
            if mes_buscar == self.getVentas()[i][6]:
                encontrado = True

        if not encontrado:
            print("Mes no encontrado")
        else:
            
            lista_productos = []
            for i in range(len(self.getVentas())):
                if mes_buscar == self.getVentas()[i][6]:
                    if self.getVentas()[i][1] not in lista_productos:
                        lista_productos.append(self.getVentas()[i][1])

            conteo_productos = []
            contador = 0
            for i in range(len(lista_productos)):
                for j in range(len(self.getVentas())):
                    if mes_buscar == self.getVentas()[i][6]:
                        if lista_productos[i] == self.getVentas()[j][1]:
                            contador = contador + self.getVentas()[j][2]
                conteo_productos.append(contador)
                contador = 0

            for i in range(len(lista_productos)):
                print(f"{lista_productos[i]} cantidad {conteo_productos[i]}")

            mayor = conteo_productos[0]
            nombre_producto = lista_productos[0]
            for i in range(len(lista_productos)):
                if conteo_productos[i] > mayor:
                    mayor = conteo_productos[i]
                    nombre_producto = lista_productos[i]

            contador = 0
            for i in range(len(conteo_productos)):
                if conteo_productos[i] == mayor:
                    contador = contador + 1

            if contador == 1:
                print(f"{nombre_producto} es el más vendido")
            else:
                print(a)
                print("Los más vendidos fueron: ")
                for i in range(len(conteo_productos)):
                    if conteo_productos[i] == mayor:
                        print(lista_productos[i])
        print(a)
       
    def totalVentasProducto(self):
        print("Total de ventas en productos")
        print(a)
        producto_buscar = input("Ingrese producto a buscar: ")

        encontrado = False
        total = 0
        for i in range(len(self.getVentas())):
            if producto_buscar == self.getVentas()[i][1]:
                total = total + self.getVentas()[i][4]
                encontrado = True
        if not encontrado:
            print("Producto no encontrado")
        else:
            print(f"${total}")
        print(a)

    def totalVentasAño(self):
        print("Total de ventas por año")
        print(a)
        año_buscar = int(input("Ingrese año a buscar: "))

        encontrado = False
        total = 0
        for i in range(len(self.getVentas())):
            if año_buscar == self.getVentas()[i][7]:
                total = total + self.getVentas()[i][4]
                encontrado = True
        if not encontrado:
            print("Año no encontrado")
        else:
            print(f"${total}")
        print(a)

    def ventasMenoresA(self):
        print("Ventas menores a dicho valor")
        print(a)
        valor_referencia = eval(input("Ingrese valor referencia: "))
        
        encontrados = False
        for i in range(len(self.getVentas())):
            if self.getVentas()[i][4] < valor_referencia:
                print(f"${self.getVentas()[i][4]}")
                encontrados = True

        if not encontrados:
            print("Ninguna venta registrada es menor que valor referencia")
        print(a)

    def promedioVentas(self):
        print("Promedio de ventas")
        suma_ventas = 0
        for i in range(len(self.getVentas())):
            suma_ventas = suma_ventas + self.getVentas()[i][4]

        if suma_ventas == 0:
            print("Sumatoria ventas: $0")
            print("Promedio ventas: $0")
        else:
            promedio_ventas = round(suma_ventas / len(self.getVentas()), 2)
            print(f"Sumatoria ventas: ${suma_ventas}")
            print(f"Promedio ventas: ${promedio_ventas}")

def main():
    matriz1 = Ventas()
    matriz1.llenarDatos()
    matriz1.mostrarDatos()

    matriz1.productoMasVendidoMes()
    matriz1.totalVentasProducto()
    matriz1.totalVentasAño()
    matriz1.ventasMenoresA()
    matriz1.promedioVentas()

main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
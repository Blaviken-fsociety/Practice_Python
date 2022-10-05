a="\n"

print(a)
print("Ejercicio A")
print(a)

class mventas:
    
    def __init__(self):
        self.mventas=[]
    
    def Setmventas(self,mventas:list):
        self.mventas=mventas

    def Getmventas(self):
        return self.mventas

    def llenarmatriz(self,filas:int,columnas:int):
        for i in range (filas):
            self.mventas.append([])
            for j in range (columnas):
                if j==0:
                    ide=int(input("Ingrese el id: "))
                    self.mventas[i].append(ide)
                if j==1:
                    nombre=input("Ingrese el nombre del cliente: ")
                    self.mventas[i].append(nombre)
                if j==2:
                    tipo_doc=input("Ingrese el tipo de documento cc/pas/ce/nit: ")
                    self.mventas[i].append(tipo_doc)
                if j==3:
                    num_doc=int(input("Ingrese el numero de documento: "))
                    self.mventas[i].append(num_doc)
                if j==4:
                    producto=input("Ingrese el producto: ")
                    self.mventas[i].append(producto)
                if j==5:
                    cantidad=int(input("Ingrese la cantidad de productos: "))
                    self.mventas[i].append(cantidad)
                if j==6:
                    valorp=int(input("Ingrese el valor del producto: "))
                    self.mventas[i].append(valorp)
                if j==7:
                    total=cantidad*valorp
                    self.mventas[i].append(total)
        print("Proceso exitoso")
    
    def mostrarmatriz(self):
        for i in range(len(self.Getmventas())):
            print(f"{i+1}. ID: {self.Getmventas()[i][0]} | NOMBRE: {self.Getmventas()[i][1]} | TIPO DOC: {self.Getmventas()[i][2]} | NUM DOC: {self.Getmventas()[i][3]} | PRODUCTO: {self.Getmventas()[i][4]} | CANTIDAD: {self.Getmventas()[i][5]} | VALOR: ${self.Getmventas()[i][6]} | TOTAL: ${self.Getmventas()[i][7]}")


    def totalventas(self):
        i=0
        acum=0
        while i < len(self.mventas):
            print(self.mventas[i][7])
            acum=acum+self.mventas[i][7]
            i=i+1
        print("El total de ventas fue: ",acum)

    def productomasvendido(self):
        print("Producto que mas se vendió")
        listaproductos = []
        for i in range(len(self.Getmventas())):
            if self.Getmventas()[i][1] not in listaproductos:
                listaproductos.append(self.Getmventas()[i][4])
        
        conteoproductos = []
        contador = 0
        for i in range(len(listaproductos)):
            for j in range(len(self.Getmventas())):
                if listaproductos[i] == self.Getmventas()[j][4]:
                    contador = contador + self.Getmventas()[j][5] # Cantidad
            conteoproductos.append(contador)
            contador = 0
        
        for i in range(len(listaproductos)):
            print(f"{listaproductos[i]} (cantidad {conteoproductos[i]})")
        
        mayor = conteoproductos[0]
        nombre_producto = listaproductos[0]
        for i in range(len(listaproductos)):
            if conteoproductos[i] > mayor:
                mayor = conteoproductos[i]
                nombre_producto = listaproductos[i]
        
        contador = 0
        for i in range(len(conteoproductos)):
            if conteoproductos[i] == mayor:
                contador = contador + 1
        
        if contador == 1:
            print(f"{nombre_producto} es el producto más vendido")
        else:
            print("")
            print("Hay varios maximos")
            print("Los más vendidos fueron: ")
            for i in range(len(conteoproductos)):
                if conteoproductos[i] == mayor:
                    print(listaproductos[i])
        
    def buscar(self):
        buscadormain=input("Desea buscar por numero de documento(doc) o por ID(id)?: ")
        print("")
        if buscadormain=="doc":
            print("Busqueda por #documento")
            print("")
            buscador = int(input("Digite el numero de documento del cliente: "))
            encontrado = False
            i = 0
            for i in range(len(self.mventas)):
                if buscador == self.mventas[i][3]:
                    encontrado = True
                i = i + 1
            if encontrado == False:
                print("El cliente no se encuentra en la base de datos")
            else:
                print("Se encontró el cliente registrado")
                i = 0
                for i in range(len(self.mventas)):
                    if buscador == self.mventas[i][3]:
                        print("Nombre:", self.mventas[i][1])
                    i = i + 1
        elif buscadormain=="id":
            print("Busqueda por ID del producto")
            print("")
            buscador = int(input("Digite la ID del producto comprado por el cliente: "))
            encontrado = False
            i = 0
            for i in range(len(self.mventas)):
                if buscador == self.mventas[i][0]:
                    encontrado = True
                i = i + 1
            if encontrado == False:
                print("El cliente no se encuentra en la base de datos")
            else:
                print("Se encontró el cliente registrado")
                i = 0
                for i in range(len(self.mventas)):
                    if buscador == self.mventas[i][0]:
                        print("Nombre:", self.mventas[i][1])
                    i = i + 1             
        else:
            print("Error, opcion invalida")

def main():
    matriz1=mventas()
    filas=int(input("Ingrese el numero de ventas a registrar: "))
    columnas=8
    matriz1.llenarmatriz(filas,columnas)
    matriz1.mostrarmatriz()
    matriz1.totalventas()
    matriz1.productomasvendido()
    matriz1.buscar()
main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
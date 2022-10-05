a="\n"

print(a)
print("Ejercicio B")
print(a)

from re import I
from tkinter import Menu
class Sistema_de_ventas():
    def __init__(self,columnas,filas):

        self.columnas = columnas
        self.filas=filas
        self.Menudelrestaurante=[]

    def setMenudelrestaurante(self,Menudelrestaurante:list):
        self.Menudelrestaurante=Menudelrestaurante

    def getMenudelrestaurante(self):
        return self.Menudelrestaurante

    def crearmatriz(self):
        for i in range(self.filas):
            self.Menudelrestaurante.append([])
            for j in range(self.columnas):
                if j == 0:
                    id=int(input(f"ingrese su id [{i}][{j}]: "))
                    self.getMenudelrestaurante()[i].append(id)

                if j == 1:
                    nombre=str(input(f"ingrese su nombre [{i}][{j}]: "))
                    self.getMenudelrestaurante()[i].append(nombre)

                if j == 2:
                    ingrediente=str(input(f"ingrese el nombre de su ingrediente: [{i}][{j}]: "))
                    self.getMenudelrestaurante()[i].append(ingrediente)

                if j == 3:
                    valor=int(input(f"ingrese su valor [{i}][{j}]: "))
                    self.getMenudelrestaurante()[i].append(valor)
                
                if j == 4:
                    cantidad=int(input(f"ingrese la cantidad [{i}][{j}]: "))
                    self.getMenudelrestaurante()[i].append(cantidad)

                if j == 5:
                    total=cantidad*valor
                    self.getMenudelrestaurante()[i].append(total)
        print("--- Proceso exitoso ---")
    
    def mostrarmatriz(self):
        for i in range(len(self.Menudelrestaurante)):
           print(f"Su id es:{self.Menudelrestaurante[i][0]} || Su nombre:{self.Menudelrestaurante[i][1]} || ingrediente:{self.Menudelrestaurante[i][2]} || Valor:{self.Menudelrestaurante[i][3]} || Cantidad:{self.Menudelrestaurante[i][4]} || total:{self.Menudelrestaurante[i][5]}")

    def totaldeventas(self):
        total_de_ventas=0
        i=0
        while i < len(self.Menudelrestaurante):
            total_de_ventas=total_de_ventas+self.Menudelrestaurante[i][5]
            i=i+1
        print(f'el total de ventas fue: {total_de_ventas}')
    
    def productomasvendido(self):
        num=0
        i=0
        while i < len(self.Menudelrestaurante):
            if self.Menudelrestaurante[i][4] > num:
                num=self.Menudelrestaurante[i][4]
                n_p=self.Menudelrestaurante[i][1]
            i=i+1
    
    def b_id(self):
        id= int(input("Ingrese la id que quiere buscar: "))

        for i in range(self.filas):
            if self.Menudelrestaurante[i][0] == id:
                posicion = i 
                break
        
        print(self.Menudelrestaurante[posicion])
                    
            

def main():
    filas=int(input("Ingrese la cantidad de usuarios: "))
    columnas=6
    matriz1= Sistema_de_ventas(columnas,filas)
    matriz1.crearmatriz()
    matriz1.mostrarmatriz()
    matriz1.b_id()
main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
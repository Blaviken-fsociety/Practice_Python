
a="\n"



class m:

    def __init__(self):
        self.m1=[]
        self.m2=[]

    def Setm1(self,m1:list):
        self.m1=m1
    
    def Getm1(self):
        return self.m1

    def Setm2(self,m2:list):
        self.m2=m2
    
    def Getm2(self):
        return self.m2

    def llenar_matriz1(self,filas:int, columnas:int):
        for i in range (filas):
            self.m1.append([])
            for j in range (columnas):
                valor1=int(input("Ingrese un elemento: "))
                self.m1[i].append(valor1)
        print("Proceso Exitoso....")

    def mostrar_matriz1(self):
        for i in range(len(self.m1)):
            for j in range(len(self.m1[0])):
                dato=self.m1[i][j]
                print(dato)

    def llenar_matriz2(self,filas:int, columnas:int):
        for i in range (filas):
            self.m2.append([])
            for j in range (columnas):
                valor2=int(input("Ingrese un elemento: "))
                self.m2[i].append(valor2)
        print("Proceso Exitoso....")

    def mostrar_matriz2(self):
        for i in range(len(self.m2)):
            for j in range(len(self.m2[0])):
                dato=self.m2[i][j]
                print(dato)

    def diagonal_principal_secundaria1(self):
        j=0
        sumato_prin=0
        sumato_secu=0
        for i in range(len(self.m1)):
            sumato_secu=sumato_secu+self.m1[i][len(self.m1[0])- 1 -j]
            j=j+1
            for j in range(len(self.m1[0])):
                if j == i:
                    sumato_prin=sumato_prin+self.m1[i][j]
        print(" ")
        print(f"Sumatoria de diagonal principal: {sumato_prin}")
        print(" ")
        print(f"Sumatoria de diagonal secundaria: {sumato_secu}")
        print(" ")
        if sumato_prin > sumato_secu:
            print("La diagonal principal es mayor")
            print(" ")
            print("La diagonal secundaria es menor")
            print(" ")
        elif sumato_prin < sumato_secu:
            print("La diagonal secundaria es mayor")
            print(" ")
            print("La diagonal principal es menor")
            print(" ")
        else:
            print("Las dos diagonales tienen el mismo valor")
            print(" ")

    def diagonal_principal_secundaria2(self):
        j=0
        sumato_prin=0
        sumato_secu=0
        for i in range(len(self.m2)):
            sumato_secu=sumato_secu+self.m2[i][len(self.m2[0])- 1 -j]
            j=j+1
            for j in range(len(self.m2[0])):
                if j == i:
                    sumato_prin=sumato_prin+self.m2[i][j]
        print(" ")
        print(f"Sumatoria de diagonal principal: {sumato_prin}")
        print(" ")
        print(f"Sumatoria de diagonal secundaria: {sumato_secu}")
        print(" ")
        if sumato_prin > sumato_secu:
            print("La diagonal principal es mayor")
            print(" ")
            print("La diagonal secundaria es menor")
            print(" ")
        elif sumato_prin < sumato_secu:
            print("La diagonal secundaria es mayor")
            print(" ")
            print("La diagonal principal es menor")
            print(" ")
        else:
            print("Las dos diagonales tienen el mismo valor")
            print(" ")

        
    
class Operaciones:

    """def suma_matriz(self):
        print(a)
        print("SUMA")
        filas = len(self.m1().getMatriz())
        columnas = len(self.m1().getMatriz()[0])
        matriz3 = []
        for i in range(filas):
            matriz3.append([])
            for j in range(columnas):
                x = self.getm1().getMatriz()[i][j] + self.getm2().getMatriz()[i][j]
                matriz3[i].append(x)
        for i in range(filas):
            print("[", end=" ")
            for j in range(columnas):
                if j != columnas - 1:
                    print(f"{matriz3[i][j]}", end=" ")
                else:
                    print(f"{matriz3[i][j]}", end=" ")
            print("]")"""

    

def main():

    matriz1=m()
    filas=int(input("Ingrese el numero de filas: "))
    columnas=int(input("Ingrese el numero de columnas: "))
    matriz1.llenar_matriz1(filas,columnas)
    matriz1.mostrar_matriz1()
    matriz1.diagonal_principal_secundaria1()

    matriz2=m()
    filas=int(input("Ingrese el numero de filas: "))
    columnas=int(input("Ingrese el numero de columnas: "))
    matriz2.llenar_matriz2(filas,columnas)
    matriz2.mostrar_matriz2()
    matriz2.diagonal_principal_secundaria2()



main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
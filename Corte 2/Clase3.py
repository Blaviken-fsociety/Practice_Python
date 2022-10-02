a="\n"

class Matrices():
    def __init__(self):
        self.__matriz = []

    def setMatriz(self, x:list):
        self.__matriz = x

    def getMatriz(self):
        return self.__matriz

    def llenarMatriz(self, indice:str, filas:int, columnas:int):
        print(a)
        print(f"Ingrese los datos de la matriz {indice}")
        for i in range(filas):
            self.getMatriz().append([])
            for j in range(columnas):
                valor = int(input("Ingrese un elemento: "))
                self.getMatriz()[i].append(valor)

    def mostrarMatriz(self, indice:str):
        print(a)
        print(f"Matriz {indice}")
        filas = len(self.getMatriz())
        columnas = len(self.getMatriz()[0])
        for i in range(filas):
            print("[", end="")
            for j in range(columnas):
                if j != columnas - 1:
                    print(f"{self.getMatriz()[i][j]}", end=" ")
                else:
                    print(f"{self.getMatriz()[i][j]}", end="")
            print("]")
          
class Operadoraiones():

    def suma(self):
        print(a)
        print("Suma de matrices: ")
        print(a)
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        matriz3 = []
        for i in range(filas):
            matriz3.append([])
            for j in range(columnas):
                x = self.getParte1().getMatriz()[i][j] + self.getParte2().getMatriz()[i][j]
                matriz3[i].append(x)
        
        for i in range(filas):
            print("[", end="")
            for j in range(columnas):
                if j != columnas - 1:
                    print(f"{matriz3[i][j]}", end=" ")
                else:
                    print(f"{matriz3[i][j]}", end="")
            print("]")

    def resta(self):
        print(a)
        print("Resta de matrices: ")
        print(a)
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        matriz3 = []
        for i in range(filas):
            matriz3.append([])
            for j in range(columnas):
                x = self.getParte1().getMatriz()[i][j] - self.getParte2().getMatriz()[i][j]
                matriz3[i].append(x)
        
        for i in range(filas):
            print("[", end="")
            for j in range(columnas):
                if j != columnas - 1:
                    print(f"{matriz3[i][j]}", end=" ")
                else:
                    print(f"{matriz3[i][j]}", end="")
            print("]")

    def multi(self):
        print(a)
        print("Multiplicación de matrices: ")
        print(a)
        m1 = self.getParte1().getMatriz()
        m2 = self.getParte2().getMatriz()

        if len(m1[0]) == len(m2):
            matriz3 = []
            for i in range(len(m1)):
                matriz3.append([])
                for j in range(len(m2[0])):
                    matriz3[i].append(0)

            for i in range(len(m1)):
                for j in range(len(m2[0])):

                    for k in range(len(m1[0])):
                        matriz3[i][j] = matriz3[i][j] + m1[i][k] * m2[k][j]

            for i in range(len(matriz3)):
                print("[", end="")
                for j in range(len(matriz3[0])):
                    if j != len(matriz3[0]) - 1:
                        print(f"{matriz3[i][j]}", end=" ")
                    else:
                        print(f"{matriz3[i][j]}", end="")
                print("]")
        else:
           print("No se pueden multiplicar")

    def __init__(self):
        self.__matriz1 = Matrices()
        self.__matriz2 = Matrices()

    def setParte1(self, x:Matrices()):
        self.__matriz1 = x
    
    def getParte1(self):
        return self.__matriz1
    
    def setParte2(self, x:Matrices()):
        self.__matriz2 = x
    
    def getParte2(self):
        return self.__matriz2

    def Comparar_Diagonal_Principal(self):
        print(a)
        print("Comparamos la diagonal principal de ambas matrices: ")
        print(a)

        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        parte1 = []
        parte2 = []
        for i in range(filas):
            for j in range(columnas):
                if i == j:
                    parte1.append(self.getParte1().getMatriz()[i][j])
                    parte2.append(self.getParte2().getMatriz()[i][j])

        mayor_parte1 = parte1[0]
        mayor_parte2 = parte2[0]
        menor_parte1 = parte1[0]
        menor_parte2 = parte2[0]

        for i in range(len(parte1)):
            if parte1[i] > mayor_parte1:
                mayor_parte1 = parte1[i]
            if parte1[i] < menor_parte1:
                menor_parte1 = parte1[i]

            if parte2[i] > mayor_parte2:
                mayor_parte2 = parte2[i]
            if parte2[i] < menor_parte2:
                menor_parte2 = parte2[i]
        
        sum_parte1 = 0
        sum_parte2 = 0
        for i in range(len(parte1)):
            sum_parte1 = sum_parte1 + parte1[i]
            sum_parte2 = sum_parte2 + parte2[i]
        
        if len(parte1) == 0:
            prom_parte1 = 0
        else:
            prom_parte1 = sum_parte1 / len(parte1)

        if len(parte2) == 0:
            prom_parte2 = 0
        else:
            prom_parte2 = sum_parte2 / len(parte2)

        print(f"Dígito mayor en la matriz 1: {mayor_parte1}")
        print(f"Dígito mayor en la matriz 2: {mayor_parte2}")
        print(f"Dígito menor en la matriz 1: {menor_parte1}")
        print(f"Dígito menor en la matriz 2: {menor_parte2}")
        print(f"Promedio en la matriz 1: {prom_parte1}")
        print(f"Promedio en la matriz 2: {prom_parte2}")

    def Comparar_Elementos_de_Matrices(self):
        print(a)
        print("Comparamos los elementos de ambas matrices: ")
        print(a)

        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        mayor_parte1 = self.getParte1().getMatriz()[0][0]
        mayor_parte2 = self.getParte2().getMatriz()[0][0]
        menor_parte1 = self.getParte1().getMatriz()[0][0]
        menor_parte2 = self.getParte2().getMatriz()[0][0]
        for i in range(filas):
            for j in range(columnas):
                if self.getParte1().getMatriz()[i][j] > mayor_parte1:
                    mayor_parte1 = self.getParte1().getMatriz()[i][j]
                if self.getParte1().getMatriz()[i][j] < menor_parte1:
                    menor_parte1 = self.getParte1().getMatriz()[i][j]

                if self.getParte2().getMatriz()[i][j] > mayor_parte2:
                    mayor_parte2 = self.getParte2().getMatriz()[i][j]
                if self.getParte2().getMatriz()[i][j] < menor_parte2:
                    menor_parte2 = self.getParte2().getMatriz()[i][j]

        sum_parte1 = 0
        sum_parte2 = 0
        for i in range(filas):
            for j in range(columnas):
                sum_parte1 = sum_parte1 + self.getParte1().getMatriz()[i][j]
                sum_parte2 = sum_parte2 + self.getParte2().getMatriz()[i][j]
        
        cantidad_elementos = filas * columnas
 
        if cantidad_elementos == 0:
            prom_parte1 = 0
        else:
            prom_parte1 = sum_parte1 / cantidad_elementos

        if cantidad_elementos == 0:
            prom_parte2 = 0
        else:
            prom_parte2 = sum_parte2 / cantidad_elementos
        
        print(f"Dígito mayor en la matriz 1: {mayor_parte1}")
        print(f"Dígito mayor en la matriz 2: {mayor_parte2}")
        print(f"Dígito menor en la matriz 1: {menor_parte1}")
        print(f"Dígito menor en la matriz 2: {menor_parte2}")
        print(f"Promedio en la matriz 1: {prom_parte1}")
        print(f"Promedio en la matriz 2: {prom_parte2}")

    def Comparar_Diagonal_Secundaria(self):
        print(a)
        print("Comparamos la diagonal secundaria de ambas matrices: ")
        print(a)
        filas = len(self.getParte1().getMatriz())
        columnas = len(self.getParte1().getMatriz()[0])
        parte1 = []
        parte2 = []
        for i in range(filas):
            for j in range(columnas):
                if i == j:
                    parte1.append(self.getParte1().getMatriz()[i][columnas - 1 - j])
                    parte2.append(self.getParte2().getMatriz()[i][columnas - 1 - j])

        mayor_parte1 = parte1[0]
        mayor_parte2 = parte2[0]
        menor_parte1 = parte1[0]
        menor_parte2 = parte2[0]
        for i in range(len(parte1)):
            if parte1[i] > mayor_parte1:
                mayor_parte1 = parte1[i]
            if parte1[i] < menor_parte1:
                menor_parte1 = parte1[i]

            if parte2[i] > mayor_parte2:
                mayor_parte2 = parte2[i]
            if parte2[i] < menor_parte2:
                menor_parte2 = parte2[i]
        
        sum_parte1 = 0
        sum_parte2 = 0
        for i in range(len(parte1)):
            sum_parte1 = sum_parte1 + parte1[i]
            sum_parte2 = sum_parte2 + parte2[i]
        
        if len(parte1) == 0:
            prom_parte1 = 0
        else:
            prom_parte1 = sum_parte1 / len(parte1)

        if len(parte2) == 0:
            prom_parte2 = 0
        else:
            prom_parte2 = sum_parte2 / len(parte2)

        print(f"Dígito mayor en la matriz 1: {mayor_parte1}")
        print(f"Dígito mayor en la matriz 2: {mayor_parte2}")
        print(f"Dígito menor en la matriz 1: {menor_parte1}")
        print(f"Dígito menor en la matriz 2: {menor_parte2}")
        print(f"Promedio en la matriz 1: {prom_parte1}")
        print(f"Promedio en la matriz 2: {prom_parte2}") 
        
def main():

    m1 = Matrices()
    m1.llenarMatriz("1", 3, 3)
    m1.mostrarMatriz("1")

    m2 = Matrices()
    m2.llenarMatriz("2", 3, 3)
    m2.mostrarMatriz("2")

    m3 = Operadoraiones()
    m3.setParte1(m1)
    m3.setParte2(m2)
    m3.suma()
    m3.resta()
    m3.multi()
    m3.Comparar_Diagonal_Principal()
    m3.Comparar_Elementos_de_Matrices()
    m3.Comparar_Diagonal_Secundaria()
    
main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
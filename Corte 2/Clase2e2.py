a="\n"

class vector:

    def __init__(self):
        self.vector1=[]

    def Setvector1(self,v1:list):
        self.vector1=v1
    
    def Getvector1(self):
        return self.vector1

    def llenarvector(self,tam:int):
        for i in range(tam):
            valor=int(input("Ingrese un elemento: "))
            self.vector1.append(valor)

    def mostrar_vector(self):
        for i in self.vector1:
            print(i)

    def mostrar_vector_invertido(self):
        #i=len(a)-1
        i=len(self.vector1)-1
        while i >= 0:
            print(self.vector1[i])
            i-=1

    def promedio_vector(self):
        acum=0
        tam=len(self.vector1)
        for i in self.vector1:
            acum=acum+1
        promedio=acum+i
        print("El promedio de los elementos es: ",promedio)

    def mayor_menor(self):
        mayor=self.vector1[0]
        menor=self.vector1[0]
        for i in self.vector1:
            if i>mayor:
                mayor=i
            if i<menor:
                menor=i
        print("Mayor: ",mayor)
        print("Menor: ",menor)
    
    def negativos_positivos(self):
        neg=self.vector1[0]
        pos=self.vector1[0]
        contneg=0
        contpos=0
        for i in self.vector1:
            if i<0:
                neg=neg+i
                contneg=contneg+1
            else:
                pos=pos+i
                contpos=contpos+1
        if contneg !=0:
            promneg=neg/contneg
        print("El promedio de los numero negativos es: ",promneg)
        if contneg !=0:
            prompos=pos/contpos
            print("El promedio de los numero positivos es: ",prompos)

def main():

    tam=int(input("Ingrese el tamaño del vector: "))
    a=vector()
    a.llenarvector(tam)
    a.mostrar_vector()
    a.mostrar_vector_invertido()
    a.promedio_vector()
    a.mayor_menor()
    a.negativos_positivos()

    tam=int(input("Ingrese el tamaño del vector: "))
    b=vector()
    b.llenarvector(tam)
    b.mostrar_vector()
    b.mostrar_vector_invertido()
    b.promedio_vector()
    b.mayor_menor()
    b.negativos_positivos()

    tam=int(input("Ingrese el tamaño del vector: "))
    c=vector()
    c.llenarvector(tam)
    c.mostrar_vector()
    c.mostrar_vector_invertido()
    c.promedio_vector()
    c.mayor_menor()
    c.negativos_positivos()

main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
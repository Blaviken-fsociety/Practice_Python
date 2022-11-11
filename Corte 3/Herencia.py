a="\n"
class padre():

    def __init__(self):
        self.nombre=""
        self.apellido=""

    def setnombre(self, nombre:str):
        self.nombre = nombre

    def getnombre(self):
        return self.nombre

    def setapellido(self,apellido:str):
        self.apellido = apellido

    def getapellido(self):
        return self.apellido

    def imprimir(self):
        print(self.nombre)
        print(self.apellido)

class hijo(padre):

    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.edad=0
    
    def imprimir(self):
        print(a)
        print("     Hijo    ")
        print("-------------")
        super().imprimir()
        print(self.edad)

def main():

    yulieth=padre()
    yulieth.setnombre("Yulieth Carolina")
    yulieth.setapellido("Diago Hernandez")
    print("    Padre    ")
    print("-------------")
    yulieth.imprimir()

    carolina=hijo()
    carolina.setnombre("Julio Cesar")
    carolina.setapellido("Arellano Guerrero")
    carolina.edad=23
    carolina.imprimir()

main()

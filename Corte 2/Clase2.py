a="\n"

class personas:
    def __init__(self,nombre:str,apellido:str):
        self.nombre=nombre
        self.apellido=apellido
    
    def SetNombre(self,nombre:str):
        self.nombre=nombre

    def GetNombre(self):
        return self.nombre

    def SetApellido(self,apellido:str):
        self.nombre=apellido

    def GetApellido(self):
        return self.apellido

    def MostrarSaludo(self):
        print("Hola",self.nombre,"", self.apellido)

def main():

    nombre=input("Ingrese su Nombre: ")
    apellido=input("Ingrese su Apellido: ")
    Julio=personas(nombre,apellido)
    Julio.MostrarSaludo()

main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
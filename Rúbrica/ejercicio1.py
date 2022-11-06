import telnetlib


a="\n"

class Cliente:
    def __init__(self,nombre:str,apellido:str, id:str, telefono:str, email:str):
        self.nombre=nombre
        self.apellido=apellido
        self.id=id
        self.telefono=telefono
        self.email=email
    
    def SetNombre(self,nombre:str):
        self.nombre=nombre

    def GetNombre(self):
        return self.nombre

    def SetApellido(self,apellido:str):
        self.nombre=apellido

    def GetApellido(self):
        return self.apellido

    def Setid(self,id:str):
        self.nombre=id

    def Getid(self):
        return self.id

    def SetTelefono(self,telefono:str):
        self.nombre=telefono

    def GetTelefono(self):
        return self.telefono

    def Setemail(self,email:str):
        self.nombre=email

    def Getemail(self):
        return self.email

class Paquetes:

    def __init__(self,idP:str,fragil:str,peso:int):
        self.idP=idP
        self.peso=peso
        self.fragil=fragil

    def SetIdP(self,idP:str):
        self.idP=idP

    def GetIdP(self):
        return self.idP

    def Setfragil(self,fragil:str):
        self.idP=fragil

    def Getfragil(self):
        return self.fragil

    def SetPeso(self,peso:int):
        self.peso=peso

    def GetPeso(self):
        return self.peso

class Venta:
    def __init__(self,idV:str,fecha:str,valor_kilo:int,valor_envio:int):
        self.idV=idV
        self.fecha=fecha
        self.valor_kilo=valor_kilo
        self.valor_envio=valor_envio

    def SetIdV(self,idV:str):
        self.idV=idV

    def GetIdV(self):
        return self.idV

    def SetFecha(self,fecha:str):
        self.idV=fecha

    def GetFecha(self):
        return self.fecha

    def SetValor_kilo(self,valor_kilo:int):
        self.valor_kilo=valor_kilo

    def GetValor_kilo(self):
        return self.valor_kilo

    def SetValor_envío(self,valor_envio:int):
        self.valor_envio=valor_envio

    def GetValor_kilo(self):
        return self.valor_envio
        

        

def main():

    print(a)
    print("Cliente")
    print(a)
    nombre=input("Ingrese su Nombre: ")
    apellido=input("Ingrese su Apellido: ")
    id=input("Ingrese la Id del cliente: ")
    telefono=input("Ingrese un telefono de contacto: ")
    email=input("Ingrese el email del cliente: ")
    print(a)
    print("Paquete")
    print(a)
    idP=input("Ingrese el id del paquete: ")
    peso=int(input("Ingrese el peso del paquete en Kg: "))
    Fragil=input("El paquete es gragil (Si/No): ")
    print(a)
    print("Venta")
    print(a)
    idV=input("Ingrese el id de la venta: ")
    fecha=input("Ingrese el día de la venta (DD/MM/AAAA): ")
    valor_kilo=int(input("Ingrese valor por cada kilo: "))

    valor_envio=(peso*valor_kilo)
    print(a)
    print("|",idV,"|",fecha,"|",nombre,"|",apellido,"|",id,"|",peso,"|",valor_kilo)
    print(a)
    print("El valor del envio sería de: ",valor_envio," Pesos Colombianos")

main()

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
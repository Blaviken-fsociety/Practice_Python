#Programación orientrada a objetos (POO)
#Set()=>colocar, poner, asignar
#get()=>Obtener
class Fraccionarios: #----->Definición de clase
#Creación del constructor
    def __init__(self): #----->Creación de Constructor
        self.numerador=0 
        self.denominador=0 #----->Creación de atributos
def main(): #----->Uso de Método main o principal para pruebas
    f1=Fraccionarios()
    f1.numerador=10
    f1.denominador=20

    f2=Fraccionarios() #----->Creación de objeto
    f2.numerador=30
    f2.denominador=40

    #Calculamos el numero nuevo
    numerador=(f1.numerador*f2.denominador)+(f1.denominador*f2.numerador) #----->Uso de Elementos del objeto
    denominador=(f1.numerador+f2.denominador)
    print("numerador: ", numerador)
    print("El resultado es: ", (numerador/denominador))

main()
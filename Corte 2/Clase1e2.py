#Programación orientrada a objetos (POO)
class Fraccionarios: 

    def __init__(self):
        self.numerador=0 
        self.denominador=0

    def setNumerador(self,x:int):
        self.numerador=x

    def getNumerador(self):
        return self.numerador
    
    def setDenominador(self,x:int):
        self.denominador=x

    def getDenominador(self):
        return self.denominador 

def main(): 
    f1=Fraccionarios()
    f1.setNumerador(10)
    f1.setDenominador(20)

    f2=Fraccionarios() 
    f2.setNumerador(30)
    f2.setDenominador(40)

    numerador=(f1.getNumerador()*f2.getDenominador())+(f1.getDenominador()*f2.getNumerador()) 
    denominador=(f1.getNumerador()*f2.getDenominador())
    print("numerador: ", numerador)
    print("El resultado es: ", (numerador/denominador))

main()
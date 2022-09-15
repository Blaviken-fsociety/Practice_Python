a="\n"

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

class Calculadora_Fraccionarios:
    
    def __init__(self):
        self.f1=Fraccionarios()
        self.f2=Fraccionarios()

    def setF1(self,x:Fraccionarios()):
        self.f1=x

    def getF1(self):
        return self.f1

    def setF2(self,x:Fraccionarios()):
        self.f2=x

    def getF2(self):
        return self.f2

    def SumarFraccionarios(self):
        numerador=(self.f1.getNumerador()*self.f2.getDenominador())+(self.f1.getDenominador()*self.f2.getNumerador())
        denominador=self.f1.getDenominador()*self.f2.getDenominador()
        print(a)
        print("El resultado de la suma Heterogénea es: ",(numerador/denominador))

    def SumarHomoFraccionarios(self):
        numerador=(self.f1.getNumerador()+self.f2.getNumerador())
        denominador=self.f1.getDenominador()
        print("Elresultado de la suma Homogénea es: ",(numerador/denominador))

    def RestaFraccionarios(self):
        numerador=(self.f1.getNumerador()*self.f2.getDenominador())-(self.f1.getDenominador()*self.f2.getNumerador())
        denominador=self.f1.getDenominador()*self.f2.getDenominador()
        print("El resultado de la resta es: ",(numerador/denominador))

    def MultiFraccionarios(self):
        numerador=self.f1.getNumerador()*self.f2.getNumerador()
        denominador=self.f1.getDenominador()*self.f2.getDenominador()
        print("El resultado de la multiplicación es:", (numerador/denominador))

def main(): 
    f1=Fraccionarios()
    f1.setNumerador(10)
    f1.setDenominador(20)

    f2=Fraccionarios() 
    f2.setNumerador(30)
    f2.setDenominador(40)

    calc1=Calculadora_Fraccionarios()
    calc1.setF1(f1)
    calc1.setF2(f2)
    calc1.SumarFraccionarios()
    calc1.RestaFraccionarios()
    calc1.MultiFraccionarios()
    
    f3=Fraccionarios()
    f3.setNumerador(4)
    f3.setDenominador(5)

    f4=Fraccionarios() 
    f4.setNumerador(9)
    f4.setDenominador(5)

    calc1=Calculadora_Fraccionarios()
    calc1.setF1(f3)
    calc1.setF2(f4)
    calc1.SumarHomoFraccionarios()
    
main()
print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)
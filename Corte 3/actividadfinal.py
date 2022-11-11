#Clase padre
#nombre, apellido, identificación, edad, correo
a="\n"
class persona():

    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.identificación=""
        self.edad=""
        self.correo=""

    def setnombre(self, x:str):
        self.nombre = x

    def getnombre(self):
        return self.nombre

    def setapellido(self,x:str):
        self.apellido = x

    def getapellido(self):
        return self.apellido

    def setidentificación(self, x:int):
        self.identificación = x

    def getidentificación(self):
        return self.identificación

    def setedad(self,x:int):
        self.edad = x

    def getedad(self):
        return self.edad

    def setcorreo(self,x:str):
        self.correo = x

    def getcorreo(self):
        return self.correo

    def imprimirdatos(self):
        print("Nombre: ",self.nombre," ",self.apellido)
        print("Identificación: ",self.identificación)
        print("Edad: ",self.edad)
        print("Correo: ",self.correo)

class empleados(persona):

    def __init__(self):
        super().__init__()
        self.cargos=""
        self.antiguedad=0
        self.profesión=""

    def setcargo(self,x:str):
        self.cargo=x

    def getcargo(self):
        return self.cargo

    def setantiguedad(self,x:str):
        self.antiguedad=x

    def getantiguedad(self):
        return self.antiguedad

    def setprofesión(self,x:str):
        self.profesión=x

    def getprofesión(self):
        return self.profesión

    def imprimirdatos(self):
        super().imprimirdatos()
        print("Cargo: ", self.cargo)
        print("Antiguedad: ", self.antiguedad)
        print("Profesión: ", self.profesión)

class tiempo_completo(empleados):

    def __init__(self):
        super().__init__()
        self.horas=0
        self.area_formación=0

    def sethoras(self,x:int):
        self.horas=x

    def gethoras(self):
        return self.horas

    def setarea_formación(self,x:str):
        self.area_formación=x

    def getarea_formación(self):
        return self.area_formación

    def imprimirdatos(self):
        super().imprimirdatos()
        print("Horas trabajadas a la semana: ", self.horas)
        print("Área de formación: ", self.area_formación)

class obra_labor(empleados):

    def __init__(self):
        super().__init__()
        self.horas_trabajadas=0
        self.valor_hora=0

    def sethoras_trabajadas(self,x:int):
        self.horas_trabajadas=x

    def gethoras_trabajadas(self):
        return self.horas_trabajadas

    def setvalor_hora(self,x:int):
        self.valor_hora=x

    def getvalor_hora(self):
        return self.valor_hora

    def setarea_formación(self,x:str):
        self.area_formación=x

    def getarea_formación(self):
        return self.area_formación

    def imprimirdatos(self):
        super().imprimirdatos()
        print("Área de formación: ", self.area_formación)
        print("Horas trabajadas a la semana: ", self.horas_trabajadas)
        print("Valor de horas trabajadas: ", self.valor_hora)
        print(self.nombre, self.apellido,"gana", self.horas_trabajadas*self.valor_hora, "a la semana")

class estudiantes(persona):

    def __init__(self):
        super().__init__()
        self.año_formación=0
        self.nombre_institución=""
        self.promedio=0

    def setaño_formación(self,x:int):
        self.año_formación=x

    def getaño_formación(self):
        return self.año_formación

    def setnombre_institución(self,x:str):
        self.nombre_institución=x

    def getnombre_institución(self):
        return self.nombre_institución

    def setpromedio(self,x:int):
        self.promedio=x

    def getpromedio(self):
        return self.promedio

    def imprimirdatos(self):
        super().imprimirdatos()     
        print("Año de formación:",self.año_formación)
        print("promedio del estudiante:",self.promedio)
        print("Institución:",self.nombre_institución)

class secundaria(estudiantes):

    def __init__(self):
        super().__init__()
        self.mensualidad=0
        self.materia_fav=""
        self.estudiar_futuro=""

    def setmensualidad(self,x:int):
        self.mensualidad=x

    def getmensualidad(self):
        return self.mensualidad

    def setmateria_fav(self,x:str):
        self.materia_fav=x

    def getmateria_fav(self):
        return self.materia_fav

    def setestudiar_futuro(self,x:str):
        self.estudiar_futuro=x

    def getestudiar_futuro(self):
        return self.estudiar_futuro

    def imprimirdatos(self):
        super().imprimirdatos()
        print("Los representantes de",self.nombre, self.apellido,"paga",self.mensualidad,"pesos al mes")
        print("Materia favorita:",self.materia_fav)
        print(self.nombre, self.apellido,"quiere ser",self.estudiar_futuro)

class Universitario(estudiantes):
    
    def __init__(self):
        super().__init__()
        self.carrera_estu=""
        self.valor_unid_credit=0
        self.credit_matricula=0

    def setcarrera_estu(self,x:str):
        self.carrera_estu=x

    def getcarrera_estu(self):
        return self.carrera_estu

    def setvalor_unid_credit(self,x:int):
        self.valor_unid_credit=x

    def getvalor_unid_credit(self):
        return self.valor_unid_credit

    def setcredit_matricula(self,x:int):
        self.credit_matricula=x

    def getcredit_matricula(self):
        return self.credit_matricula

    def imprimirdatos(self):
        super().imprimirdatos()
        print(self.nombre, self.apellido,"estudia",self.carrera_estu)
        print("Créditos matriculados:",self.credit_matricula)
        print("Valor de unidad de créditos:",self.valor_unid_credit)
        print("El semestre de",self.nombre,self.apellido,"tiene un precio estimado de",self.credit_matricula*self.valor_unid_credit,"pesos")

def main():

    """ejemplo1=persona()
    ejemplo1.setnombre("Julio")
    ejemplo1.setapellido("Arellano")
    ejemplo1.setidentificación(1127615417)
    ejemplo1.setedad(23)
    ejemplo1.setcorreo("jarellan@cuc.edu.co")
    ejemplo1.imprimirdatos()

    print(a)
    print("Empleados")
    print("---------------------------------------------------------------")
    ejemplo2=empleados()
    ejemplo2.setnombre("Calos")
    ejemplo2.setapellido("Castro")
    ejemplo2.setidentificación(27246006)
    ejemplo2.setedad(27)
    ejemplo2.setcorreo("Carloscastro@gmail.com")
    ejemplo2.setcargo("Docente")
    ejemplo2.setantiguedad(1)
    ejemplo2.setprofesión("Ingeniero de sistemas")
    ejemplo2.imprimirdatos()

    print(a)"""
    print("Tiempo completo")
    print("---------------------------------------------------------------")

    ejemplo3=tiempo_completo()
    ejemplo3.setnombre("Julio")
    ejemplo3.setapellido("Arellano")
    ejemplo3.setidentificación(1127615417)
    ejemplo3.setedad(30)
    ejemplo3.setcorreo("jarellan@cuc.edu.co")
    ejemplo3.setcargo("Docente")
    ejemplo3.setantiguedad(5)
    ejemplo3.setprofesión("Ingeniero de sistemas")
    ejemplo3.sethoras(40)
    ejemplo3.setarea_formación("Redes")
    ejemplo3.imprimirdatos()

    print(a)
    print("Obra labor")
    print("---------------------------------------------------------------")

    ejemplo4=obra_labor()
    ejemplo4.setnombre("Elder")
    ejemplo4.setapellido("Dayán")
    ejemplo4.setidentificación(1234567891)
    ejemplo4.setedad(35)
    ejemplo4.setcorreo("ElderDayan@cuc.edu.co")
    ejemplo4.setcargo("Docente")
    ejemplo4.setantiguedad(7)
    ejemplo4.setprofesión("Cantante")
    ejemplo4.setarea_formación("Composición y canto")
    ejemplo4.sethoras_trabajadas(48)
    ejemplo4.setvalor_hora(10000)
    ejemplo4.imprimirdatos()
    
    """print(a)
    print("Estudiante")
    print("---------------------------------------------------------------")

    ejemplo5=estudiantes()
    ejemplo5.setnombre("Manuel")
    ejemplo5.setapellido("Turismo")
    ejemplo5.setidentificación(1154187469)
    ejemplo5.setedad(16)
    ejemplo5.setcorreo("manuelturismo@lasnieves.edu.co")
    ejemplo5.setaño_formación(11)
    ejemplo5.setpromedio(3.9)
    ejemplo5.setnombre_institución("Unidad Educativa Cococho de las Nieves")
    ejemplo5.imprimirdatos()"""

    print(a)
    print("Secundaria")
    print("---------------------------------------------------------------")

    ejemplo6=secundaria()
    ejemplo6.setnombre("Manuel")
    ejemplo6.setapellido("Turismo")
    ejemplo6.setidentificación(1154187469)
    ejemplo6.setedad(16)
    ejemplo6.setcorreo("manuelturismo@lasnieves.edu.co")
    ejemplo6.setaño_formación(11)
    ejemplo6.setpromedio(3.9)
    ejemplo6.setnombre_institución("Unidad Educativa Cococho de las Nieves")
    ejemplo6.setmensualidad(500000)
    ejemplo6.setmateria_fav("Educación física")
    ejemplo6.setestudiar_futuro("Policía")
    ejemplo6.imprimirdatos()

    print(a)
    print("Universitario")
    print("---------------------------------------------------------------")

    ejemplo7=Universitario()
    ejemplo7.setnombre("Junior")
    ejemplo7.setapellido("Caldera")
    ejemplo7.setidentificación(27246006)
    ejemplo7.setedad(23)
    ejemplo7.setnombre_institución("Corporación Universitaria de la Costa")
    ejemplo7.setcorreo("jcaldera@cuc.edu.co")
    ejemplo7.setaño_formación(2)
    ejemplo7.setpromedio(4.2)
    ejemplo7.setcarrera_estu("Comunicación Social")
    ejemplo7.setvalor_unid_credit(379000)
    ejemplo7.setcredit_matricula(17)
    ejemplo7.imprimirdatos()

main()
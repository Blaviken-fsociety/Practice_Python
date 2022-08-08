#La suma de los primeros n numeros

n = int(input("Ingrese un numero: "))
suma=0
for i in range(1,n +1):
    suma=suma + i
print("La suma de los n numeros hasta" ,n, "es: ",suma)

#crear un vector estatico
a=[1,2,3,4,5,6,7,8,9,10]
print(a)

#crear un vector y llenarlo de manera manual
b=[]
b.append(10)
b.append(20)
b.append(30)
b.append(40)
print("vector b: ",b)

#crear un vector dinamico y que el usuario sea quien ingrese los valores
n=eval(input("Ingrese la cantidad de elementos: "))
c=[]
for i in range(n):
    valor=eval(input(f"ingrese un elemento en la posicion {i} : "))
    c.append(valor)
print("vector c:", c)

#primera y ultima posicion del vector
print("El mprimer elemento es",c[0])
print("El ultimo elemento es", c[n-1])

#promedio de elementos
acum=0
for i in c:
    acum=acum+i
promedio=acum/len(c)
print("El promedio de los elementos es: ",promedio)

#promedio de negativos y positivos
pos=0
contpos=0
neg=0
contneg=0
for i in c:
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

#maximo y minimo
mayor=c[0]
for i in range(n):
    if c[i]>mayor:
        mayor= c[i]
print ("El elemento mayor",mayor)

menor=c[0]
for i in range(n):
    if c[i]<menor:
        menor= c[i]
print ("El elemento menor",menor)

#Mostrar los vectores de derecha a izquierda

x=len(c)-1
while x >=0:
    print(c[x])
    x= x - 1

#Dado un valor decir si esta o no dentro del vector y cuantas veces esta
vbuscado = eval(input("Ingrese el valor a buscar: "))
x = 0
contavbuscado=0
while x < len(c):
    if c[x] == vbuscado:
        contavbuscado = contavbuscado + 1
    x += 1

if contavbuscado != 0:
    if contavbuscado == 1:
        print("Valor encontrado", contavbuscado, " vez")
    elif contavbuscado > 1:
        print("Valor encontrado ", contavbuscado, " veces)")
else:
    print("Valor no encontrado")

#Dado un vector de numeros mostrar la tabla de multiplicar de dichos elementos
x = 0
while x < len(c):
    dato = c[x]
    for i in range(0,11,1):
        print(dato, "x", i,"=",(dato*i), )
    x += 1


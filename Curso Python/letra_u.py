matriz = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
f = int(input("Ingresa la fila: "))
c = int(input("Ingresa la columna: "))
t = int(f * 2 * c - 2)
a = int(t / 26 + 1)
s = c - 2
matriz2=[]
b = int (0)
print("a"+str(a))
for i in range(0,a):
    matriz2+=matriz2
for i in range(0,26 * a - t):
    matriz.pop()
cont = 0
a="\nMatriz U:\n"
for i in range(0, f):
    if i != f - 1:
        a += str(matriz2[cont])
        for j in range(0, s * 2 + 1):
            a +=str(" ")
        a += str(matriz2[t - cont - 1])
    else:
        for j in range(0, c):
            a += str(matriz2[i + j]) + " "
    a += "\n"
    cont += 1
cont = 0
a += "\n\nMatriz Resultante\n"
for i in range(0, f):
    if i != f - 1:
        a += str(matriz2[t - cont -1])
        for j in range(0, s * 2 + 1):
            a += str(" ")
        a += str(matriz2[t - cont])
    else:
        for j in range(c - 1, -1, -1):
            a += str(matriz2[i +j]) + " "
    a += "\n"
    cont += 1
print(a)
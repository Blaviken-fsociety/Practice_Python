# Serie 4, 3, 2, 1, 4, 3, 2...
#c = contador
#w = interruptor
n = int(input("Ingrese un numero: "))
c = 0
w = 4
while c < n:
    print(w)
    if w > 1:
        w = w -1
    else:
        w = 4
    c = c + 1
    


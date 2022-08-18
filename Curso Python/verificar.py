n=eval(input("Ingrese la cantidad de elementos: "))
j=[]
for i in range(n):
    valor=eval(input(f"ingrese un elemento en la posicion {i} : "))
    j.append(valor)
verificar = eval(input("Ingrese el numero a verificar: "))
print(f"{verificar} se repite ",j.count(verificar)," veces")
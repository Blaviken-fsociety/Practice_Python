#vector 1
a=[]
cantidad_ele = eval(input("Ingrese el numero de elementos: "))

for i in range(cantidad_ele):
	x=eval(input(f"Ingrese un valor {i}: "))
	a.append(x)
	i=i+1
print(a)
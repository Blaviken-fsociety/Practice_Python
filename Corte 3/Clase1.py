# creamos variable para la lectura del archivo txt
informacion=open("Corte 3/ejemplo.txt","r+")

for i in informacion:
    print(i)

#escritura

informacion.write("\n"+"agrando una linea al final"+"\n")
informacion.close()
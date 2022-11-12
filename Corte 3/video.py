a="\n"
#Actividad Final : Escritura y lectura de datos binarios

nombre_archivo= "frase.dat"

#Escritura de un archivo de texto:

with open(nombre_archivo, "wb") as f:
    f.write(b"Python es tremendo")
    f.write(b"\n")
    f.write(b"resto del contenido")
    f.write(b"\n")
    f.write(b"Fin del archivo")

# Lectura total del contenido del archivo:

with open (nombre_archivo, "rb") as f:
    datos =f.read()
    print(datos.decode("utf-8"))
print()

#Lectura línea por linea del contenido del archivo:

with open(nombre_archivo, "rb") as f:
    for linea in f:
        print("Oración: ",linea.decode("utf-8"),end="")

#Muchas gracias por su atención 
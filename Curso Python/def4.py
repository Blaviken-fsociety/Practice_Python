#separar una lista en pares e impares

ejemplo = [3,7,9,5,8,3,7,12]

def separar_listas(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

pares, impares = separar_listas(ejemplo)

print(pares)
print(impares)
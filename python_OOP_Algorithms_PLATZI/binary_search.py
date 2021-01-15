import random as rndm

def busqueda_binaria(lista, comienzo, final, objetivo, contador):

    contador += 1

    if comienzo > final:
        return (False, contador)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, contador)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador)

def busqueda_lineal(lista, objetivo, contador):
    match = False

    for elemento in lista:
        contador += 1
        if elemento == objetivo:
            match = True
            break
    return (match, contador)

if __name__ == "__main__":
    contador1, contador2 = 0, 0
    tamanio_de_lista = int(input("De que tamanio sera la lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = sorted([rndm.randint(0, 100) for i in range(tamanio_de_lista)])

    print(lista)

    (encontrado1, contador1) = busqueda_lineal(lista, objetivo, contador1)
    print(f"El elemento {objetivo} {'esta' if encontrado1 else 'no esta'} en la lista")
    print(f"iteraciones busqueda lineal: {contador1}")

    (encontrado2, contador2) = busqueda_binaria(lista, 0, len(lista), objetivo, contador2)
    print(f"El elemento {objetivo} {'esta' if encontrado2 else 'no esta'} en la lista")
    print(f"iteraciones busqueda binaria: {contador2}")
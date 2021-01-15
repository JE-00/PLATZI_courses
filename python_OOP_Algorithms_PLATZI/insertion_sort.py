import random


def insertion_sort(lista):
    cont = 0
    for indice in range(1, len(lista)):
        posicion_actual = indice
        valor_actual = lista[indice]

        while posicion_actual > 0 and valor_actual < lista[posicion_actual - 1]:
            cont += 1
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        if posicion_actual != 0:
            cont += 1

        lista[posicion_actual] = valor_actual

    return lista, cont


if __name__ == "__main__":
    tamanio_de_lista = int(input("De que tamanio sera la lista? "))

    lista = [random.randint(0, 100) for i in range(tamanio_de_lista)]
    print(lista)

    (lista_ordenada, iteraciones) = insertion_sort(lista)
    print(lista_ordenada)
    print(iteraciones)

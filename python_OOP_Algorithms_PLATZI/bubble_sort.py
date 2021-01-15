import random

def bubble_sort(lista, iteraciones = 0):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            iteraciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return (lista, iteraciones)

if __name__ == "__main__":
    tamanio_de_lista = int(input("De que tamanio sera la lista? "))

    lista = [random.randint(0, 100) for i in range(tamanio_de_lista)]
    print(lista)

    (lista_ordenada, iteraciones) = bubble_sort(lista)
    print(lista_ordenada)
    print(iteraciones)


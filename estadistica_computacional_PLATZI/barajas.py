
"""
Carta más alta:Cuando los jugadores no tienen ninguna de las manos anteriormente explicadas,la mano con la carta mayor
gana.

Pareja:Dos cartas del mismo rango númerico. En el caso de que dos manos tengan una pareja, la pareja mayor de la mano
gana.

Doble pareja:Cualquier pareja de un rango númerico junto con otra pareja de otro rango númerico. Cuando hay más de una
mano con doble pareja, la mano con la carta mayor fuera de las parejas gana.

Trio (Three of a Kind):Tres cartas de un mismo rango de números.

Escalera:Cinco cartas en secuencia. Cuando más de una escalera está compitiendo, la mano que tenga la carta mayor es la
ganadora. Un as puede ser tomado como alto o bajo (pero no alto y bajo en la misma mano).El palo no tiene relevancia.

Color:Cinco cartas de un mismo palo. Cuando existe una competencia entre el color, el que tenga la carta mayor de color
gana.

Full House:Un trio del mismo rango de números más una pareja.

Poker (Four of a kind): Cuatro cartas del mismo rango de número. En este caso el palo no tiene revelancia.

Escalera de Color: Escalera con las cinco cartas del mismo palo.

Escalera Real: Escalera del mismo color desde el 10 al As.
"""

import random
import collections

PALOS = ["espada", "corazon", "rombo", "trebol"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]


def crear_baraja():
    barajas = []

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    return barajas


def obtener_mano(barajas, tamanio_mano):
    mano = random.sample(barajas, tamanio_mano)
    return mano


def crear_manos(barajas, tamanio_mano):
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamanio_mano)
        manos.append(mano)
    return manos


def probabilidad_par(manos):
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break
    return pares / intentos


def probabilidad_dospares(manos):
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                if pares == 2:
                    break
    return pares / intentos


def probabilidad_trio(manos):
    trio = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 3:
                trio += 1
                break
    return trio / intentos


def probabilidad_escalera(manos):
    pass


def main(tamanio_mano, intentos):
    barajas = crear_baraja()
    manos = crear_manos(barajas, tamanio_mano)
    for _ in range(intentos):
        probabilidad_par(manos)
        probabilidad_dospares(manos)
        probabilidad_trio(manos)
        probabilidad_escalera(manos)

    print(f"La probabilidad de tener un par en una mano de {tamanio_mano} es de {probabilidad_par}")


if __name__ == '__main__':
    tamanio_mano = int(input("De cuantas barajas sera la mano: "))
    intentos = int(input("¿Cuantos intentos para calcular la probabilidad? "))

    main(tamanio_mano, intentos)

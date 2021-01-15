import random
import collections
import numpy as np
from bokeh.plotting import figure, output_file, show


def tirar_dado(numero_tiros):
    secuencia_tiros = []
    for _ in range(numero_de_tiros):
        dado_1 = random.choice([1, 2, 3, 4, 5, 6])
        dado_2 = random.choice([1, 2, 3, 4, 5, 6])
        tiro = dado_1 + dado_2
        secuencia_tiros.append(tiro)
    return secuencia_tiros


def graficar(x, y):
    plot = figure(title="Distribucion Normal")
    plot.vbar(x, top=y, width=0.1, color="#CAB2D6")
    output_file("vertical_bar.html")
    show(plot)


def estimacion(numero_tiros):
    estimados = tirar_dado(numero_tiros)
    media_estimados = np.mean(estimados)
    sigma = np.std(estimados)
    counter = dict(collections.Counter(estimados))
    graficar(list(counter.keys()), list(counter.values()))
    return media_estimados, sigma


def main(numero_tiros):
    media, sigma = estimacion(numero_tiros)
    print(f'Est = {round(float(media), 5)}, sigma = {round(float(sigma), 5)}')


if __name__ == '__main__':
    while True:
        numero_de_tiros = int(input('Diga la cantidad de tiros: '))
        main(numero_de_tiros)

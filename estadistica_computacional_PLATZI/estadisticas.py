import random
import math
from bokeh.plotting import figure, show
import numpy as np


def media(X):
    return sum(X) / len(X)


def varianza(X):
    miu = media(X)
    acumulador = 0
    for x_i in X:
        acumulador += (x_i - miu) ** 2
    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))


def distribucion_normal(X, miu, sigma):
    Y = []
    for x in X:
        y = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-1 / 2 * ((x - miu) / (sigma)) ** 2)
        Y.append(y)
    return Y


def graficar(X, Y, miu, sigma):
    grafica = figure(title=f'Distribución normal', x_axis_label='x', y_axis_label='y')

    grafica.line(X, Y, legend_label=f'Distribución normal', line_color='blue')
    grafica.vbar(x=X, width=0.1, bottom=0, top=Y, legend_label=f'Distribución normal', color='blue')


    media_y = [min(Y), max(Y)]
    media_x = [miu, miu]

    grafica.line(media_x, media_y, legend_label=f'Media', line_color='red')

    desviacion_estandar_1_y = [min(Y), max(Y)]
    desviacion_estandar_1_x = [miu + sigma, miu + sigma]

    grafica.line(desviacion_estandar_1_x, desviacion_estandar_1_y, legend_label=f'Desviación estándar', line_color='green')

    desviacion_estandar_2_y = [min(Y), max(Y)]
    desviacion_estandar_2_x = [miu - sigma, miu - sigma]

    grafica.line(desviacion_estandar_2_x, desviacion_estandar_2_y, line_color='green')

    show(grafica)


if __name__ == '__main__':
    X = sorted([random.randint(1, 101) for i in range(100)])

    miu = media(X)

    sigma_al_cuadrado = varianza(X)

    sigma = desviacion_estandar(X)

    Y = distribucion_normal(X, miu, sigma)
    
    graficar(X, Y, miu, sigma)

    print("Arreglo de X: ", X)
    print("Media = ", miu)
    print("Varianza = ", sigma_al_cuadrado)
    print("Desviacion estandar = ", sigma)

"""
# version usando numpy
    
if __name__ == "__main__":
    X = np.random.randint(1 , 21 , size=20)
    
    miu = np.mean(X)
    
    sigma_al_cuadrado = np.std(X)
    
    sigma = np.var(X)
    
    print("Arreglo de X: ", X)
    print("Media = ", miu)
    print("Varianza = ", sigma_al_cuadrado)
    print("Desviacion estandar = ", sigma)
"""

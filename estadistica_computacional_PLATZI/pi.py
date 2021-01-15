import random
import numpy as np

def aventar_agujas(numero_agujas):
    agujas_dentro = 0

    for _ in range(numero_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_del_centro = np.sqrt(x**2 + y**2)

        if distancia_del_centro <= 1:
            agujas_dentro += 1

    return (4 * agujas_dentro) / numero_agujas


def estimacion(numero_agujas, intentos):
    estimados = []
    for _ in range(intentos):
        estimacion_pi = aventar_agujas(numero_agujas)
        estimados.append(estimacion_pi)
    media_estimados = np.mean(estimados)
    sigma = np.std(estimados)
    print(f"agujas = {numero_agujas}, media = {round(float(media_estimados), 5)}, sigma = {round(float(sigma), 5)}")

    return media_estimados, sigma


def estimar_pi(precision, numero_agujas, intentos):
    sigma = precision
    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_agujas, intentos)
        numero_agujas *= 2
    # return media


if __name__ == '__main__':
    estimar_pi(0.01, 1000, 1000)

"""
PARA GRAFICAR UNA ESTIMACION

import os
import random as random
import math as math
import statistics as std
from bokeh.plotting import figure, output_file, show
os.system('cls')

tries = 10
puntos = 100

def estimar_pi(puntos):
    in_circle_x = []
    in_circle_y = []
    out_circle_x = []
    out_circle_y = []
    pi_array =[]

    for i in range(puntos):
        pos_x = random.uniform(-1,1)
        pos_y = random.uniform(-1,1)

        if math.sqrt(pos_x**2 + pos_y**2) <= 1:
            in_circle_x.append(pos_x)
            in_circle_y.append(pos_y)
        else:
            out_circle_x.append(pos_x)
            out_circle_y.append(pos_y)

    estimate_pi = (4 * len(in_circle_x)) / puntos
    return (estimate_pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y)
    #return ()

def crear_muestra(tries):
    pi_array =[]
    for i in range(tries):
        pivalor,in_circle_x, in_circle_y, out_circle_x, out_circle_y = estimar_pi(puntos)
        pi_array.append(pivalor)
    return (pi_array, in_circle_x, in_circle_y, out_circle_x, out_circle_y)

deviation = 1       # Valor inicial para poder empezar el ciclo while
presicion = 0.1     # Precision en cifras significativas para determinar el 
                    # valor estimado de pi (CUIDADO!!!!)

iteration = 1

while deviation >= (presicion / 1.96):
    pi_array, in_circle_x, in_circle_y, out_circle_x, out_circle_y = crear_muestra(tries)
    deviation = std.stdev(pi_array)
    variance = std.variance(pi_array) 
    mean = std.mean(pi_array)
    
    print(f'------------------       Iteracion number: {(iteration)}      ------------------')
    print(f'Standard deviation: {round(deviation,5)}, Variance : {round(variance,5)}, pi estimated: {round(mean,5)}')
    print(f'Numero de intentos {tries}, Numero de puntos {puntos}\n\n')
    #print(f)
    puntos *= 10
    tries *= 10
    iteration += 1

output_file("line.html")
plot = figure(plot_width=600, plot_height=600)
plot.circle(in_circle_x, in_circle_y, size=5, color="red", alpha=0.5)
plot.circle(out_circle_x, out_circle_y, size=5, color="navy", alpha=0.5)
show(plot)
"""

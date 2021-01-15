from bokeh.plotting import figure, show
import random


def tirar_dado(numero_tiros):
    secuencia_tiros = []
    for _ in range(numero_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_tiros.append(tiro)
    return secuencia_tiros


def plot(simulaciones, probabilidades):
    plot = figure(title='Probability get 1 with 1 shot',
                  x_axis_label='Attempts',
                  y_axis_label='Probability')

    plot.line(simulaciones, probabilidades)
    show(plot)


def probabilidad(tiros, numero_intentos):
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
    return tiros_con_1 / numero_intentos


def main(numero_tiros, numero_intentos):
    simulaciones = []
    probabilidades = []
    for i in range(1, numero_intentos, 100):
        tiros = []
        for _ in range(i):
            secuencia_tiros = tirar_dado(numero_tiros)
            tiros.append(secuencia_tiros)

        probabilidad_1 = probabilidad(tiros, i)
        probabilidades.append(probabilidad_1)
        simulaciones.append(i)

    print(f"Probabilidad de obtener 1 en {numero_tiros} tiros es de {probabilidad_1}")
    plot(simulaciones, probabilidades)


if __name__ == '__main__':
    numero_tiros = int(input("Cuantos tiros quieres? "))
    numero_intentos = int(input("Cuantas simulaciones? "))

    main(numero_tiros, numero_intentos)

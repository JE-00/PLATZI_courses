from borracho import EstoyPEdisimonomamesjajaka
from coordenada import Coordenada
from campo import Campo

from bokeh.plotting import figure, show


def main(distancias_caminata, numero_intentos, tipo_borracho):
    inicio = Coordenada(0, 0)
    for caminata in distancias_caminata:
        campo = Campo()
        campo.aniadir_borracho(borracho, inicio) #poner un borracho en origen
        ejecutar_caminata(campo, borracho, caminata)


def ejecutar_caminata(campo, borracho, distancia):
    x_arreglo = []
    y_arreglo = []
    x_arreglo.append(campo.obtener_coordenada(borracho).x)
    y_arreglo.append(campo.obtener_coordenada(borracho).y)
    for _ in range(distancia):
        campo.mover_borracho(borracho) #se actualiza las coordenadas del borracho
        x_arreglo.append(campo.obtener_coordenada(borracho).x)
        y_arreglo.append(campo.obtener_coordenada(borracho).y)

    graficar(x_arreglo, y_arreglo)


def graficar(x, y):
    figura = figure(title="Camino aleatorio")
    figura.line(x, y, legend_label="Distancia media")

    show(figura)


if __name__ == '__main__':
    distancias_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100
    borracho = EstoyPEdisimonomamesjajaka('Jose')

    main(distancias_caminata, numero_intentos, borracho)

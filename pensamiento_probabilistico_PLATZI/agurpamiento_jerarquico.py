"""
Algoritmo de agrupamiento jerárquico:
- Se empieza tratando a cada dato como un grupo llamado cluster
- Se mide la distancia media entre cada cluster
- En cada iteración se unen los dos clusters mas cercanos (con menor distancia promedio)
- Estas iteraciones se repiten hasta tener un solo cluster con todos los datos
"""

import numpy as np


# Genera las coordenadas aleatorias de los datapoints aleatorios
def generar_puntos(num_datapoints):
    """
    :param num_datapoints:
    :return datapoints:
    """
    for i in range(num_datapoints):
        datapoint = (i, np.random.randint(0, 20), np.random.randint(0, 20))
        datapoints.append(datapoint)
    return datapoints


def distancia_euclidiana(cluster_1, cluster_2):
    distancias = []
    for i in range(len(datapoints)):
        for j in range(len(datapoints)):
            if j + i + 1 < len(datapoints):
                current_point = datapoints[i]
                next_point = datapoints[j + i + 1]
                distancia = np.sqrt((current_point[1] - next_point[1]) ** 2 + (current_point[2] - next_point[2]) ** 2)
                distancias.append([current_point[0], next_point[0], distancia])
            return distancias
    return


def unir_clusters(clusters):
    distancias = []
    i = 0
    # [0, (cluster_1[1] + cluster_2[1]) / 2, (cluster_1[1] + cluster_2[1]) / 2]
    for i in clusters:
            distancias[i] = distancia_euclidiana(cluster_1, cluster_2)


if __name__ == '__main__':
    num_datapoints = int(input("Numero de datapoints: "))
    datapoints = generar_puntos(num_datapoints)
    print(datapoints)
    unir_clusters(datapoints)

class Campo:

    def __init__(self):
        self.coordenadas_borrachos = {}

    def aniadir_borracho(self, borracho, coordenada):
        self.coordenadas_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        dx, dy = borracho.camina()
        coordenada_actual = self.coordenadas_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(dx, dy)

        self.coordenadas_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_borrachos[borracho]

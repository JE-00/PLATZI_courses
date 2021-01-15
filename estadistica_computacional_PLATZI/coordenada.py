class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, dx, dy):
        return Coordenada(self.x + dx, self.y + dy)

    def distancia(self, otra_coordenada):
        dx = self.x - otra_coordenada.x
        dy = self.y - otra_coordenada.y

        return(dx**2 + dy**2)**0.5

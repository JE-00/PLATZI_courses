class Lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura = "caliente"):
        self._llenar_tanque_de_agua(temperatura)
        self._aniadir_jabon()
        self._enjuagar()
        self._centrifugar()
    def _llenar_tanque_de_agua(self, temperatura):
        print(f"Llenando el tanque con agua {temperatura}")

    def _aniadir_jabon(self):
        print("Aniadiendo jabon")

    def _enjuagar(self):
        print("Enjuagando la ropa")

    def _centrifugar(self):
        print("Centrifugado la ropa")

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
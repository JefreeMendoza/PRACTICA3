class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        pass
    def calcular_area(self):
        area = self.largo*self.ancho
        return area
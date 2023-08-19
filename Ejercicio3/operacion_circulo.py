class Circulo: 
    def __init__(self, radio):
        self.radio = radio
        pass

    def calcular_area(self):
        PI = 3.1415
        area = PI*self.radio**2
        return area
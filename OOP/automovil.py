class Automovil:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self._estado = "en reposo"
        self._motor = None
        self.cantidad_combustible = 0
    
    def manejar(self):
        if self.cantidad_combustible == 0:
            print("Lo siento, necesitas combustible")
        else:
            print("En marcha!")
            self.cantidad_combustible = self.cantidad_combustible - 1

class Motor:
    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo


mi_auto = Automovil("rojo", "Vento", "2020")
mi_auto.manejar()

mi_auto.cantidad_combustible = 10
mi_auto.manejar()

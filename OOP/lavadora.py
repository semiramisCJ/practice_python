class Lavadora:
    def __init__(self, modelo, marca, capacidad, color="blanco"):
        self.modelo = modelo
        self.marca = marca
        self.capacidad = capacidad
        self.color = color
        self.numero_prendas = 0
    
    def _enjuagar(self):
        print("Estoy enjuagando")
    
    def _centrifugar(self):
        print("Centrifugando")

    def lavar(self, numero_prendas):
        self.numero_prendas = numero_prendas
        if self.numero_prendas == 0:
            print("Lo siento, necesitas poner ropa primero")
        elif self.numero_prendas <= round(self.capacidad/2):
            print(f"Empieza ciclo de lavado para {numero_prendas} prendas")
            self._enjuagar()
            self._centrifugar()
        else:
            print("No puedo lavar porque excedes mi capacidad")
            print(f"Maximo acepto {round(self.capacidad/2)} prendas")


if __name__ == "__main__":
    lavadorita = Lavadora("2019", "LG", 15)
    lavadorita.lavar(10)
    lavadorita.lavar(5)

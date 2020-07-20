class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("Ando a pie")
    
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("Ando sobre una bicicleta")

if __name__ == "__main__":
    pepita = Persona("Pepita")
    print(f'Hola, soy {pepita.nombre}')
    pepita.avanza()

    juanita = Ciclista("Juanita")
    print(f'Hola, soy {juanita.nombre}')
    juanita.avanza()

class Pais:
    def __init__(self, nombre, regiones):
        self.nombre = nombre
        self.regiones = regiones

class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self.identificador = identificador
        self.pais = pais
        self._region = None
    
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self.pais.regiones:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en el pais de {self.pais.nombre}')


if __name__ == "__main__":
    mexico = Pais("Mexico", ["CDMX", "Morelos", "Nayarit"])
    casilla = CasillaDeVotacion(123, mexico)
    print(casilla.region)
    casilla.region = "CDMX"
    print(casilla.region)

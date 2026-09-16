class Direccio:
    def __init__(self, carrer, ciutat, pais):
        self.carrer = carrer
        self.ciutat = ciutat
        self.pais = pais

    def __str__(self):
        return f"{self.carrer}, {self.ciutat}, {self.pais}"
from . import Direccio

class Persona:
    def __init__(self, nom, edat, carrer, ciutat, pais):
        self.nom = nom
        self.edat = edat
        self.direccio = Direccio(carrer, ciutat, pais)

    def __str__(self):
        return f"Nom: {self.nom}, Edat: {self.edat}, Direcció: {self.direccio}"
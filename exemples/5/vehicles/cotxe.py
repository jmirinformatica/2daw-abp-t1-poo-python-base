from . import Vehicle

class Cotxe(Vehicle):

    def __init__(self, marca, model, portes):
        super().__init__(marca, model)
        self.portes = portes

    # Implementa @abstractmethod
    @property
    def nom(self):
        return "Cotxe"
    
    # Implementa @abstractmethod
    @property
    def rodes(self):
        return 4

    # Implementa @abstractmethod
    def mostra_seguretat(self):
        print("Has de posar-te el cinturó de seguretat")

    # Sobrescriu el mètode
    def __str__(self):
        c = super().__str__()
        return f"{c} i {self.portes} portes"
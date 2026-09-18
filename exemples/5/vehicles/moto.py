from . import Vehicle

class Moto(Vehicle):
    
    # Implementa @abstractmethod
    @property
    def nom(self):
        return "Moto"
    
    # Implementa @abstractmethod
    @property
    def rodes(self):
        return 2

    # Implementa @abstractmethod
    def mostra_seguretat(self):
        print("Has de posar-te el casc")
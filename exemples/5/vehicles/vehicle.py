from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def nom(self):
        pass

    def start(self):
        print(f"El vehicle {self.nom()} està en marxa")

    def stop(self):
        print(f"El vehicle {self.nom()} s'ha aturat")
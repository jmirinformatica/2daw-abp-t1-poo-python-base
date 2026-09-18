from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, marca, model):
        self.marca = marca
        self.model = model

    # -------------------
    # MÈTODES ABSTRACTES
    # -------------------

    @property
    @abstractmethod
    def nom(self) -> str:
        pass

    @property
    @abstractmethod
    def rodes(self) -> int:
        pass

    @abstractmethod
    def mostra_seguretat(self):
        pass

    # -------------------
    # ALTRES MÈTODES
    # -------------------

    def start(self):
        print(f"El vehicle {self.nom} està en marxa")

    def stop(self):
        print(f"El vehicle {self.nom} s'ha aturat")

    def __str__(self):
        return f"{self.marca} {self.model} amb {self.rodes} rodes"
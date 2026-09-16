class Alumne:
    
    # Nombre d'alumnes com a variable de classe
    nombre_alumnes = 0

    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        Alumne.nombre_alumnes += 1

    # -------------------
    # GETTERS / SETTERS
    # -------------------

    @property
    def edat(self) -> int:
        return self._edat

    @edat.setter
    def edat(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("edat ha de ser un número")
        if valor <= 0:
            raise ValueError("edat ha de ser superior a zero")
        self._edat = valor
class Alumne:
    def __init__(self, nom):
        self.nom = nom
        self.assignatures = []

    def afegeix_assignatura(self, assignatura):
        self.assignatures.append(assignatura)

    def llista_assignatures(self):
        for assignatura in self.assignatures:
            print(assignatura)
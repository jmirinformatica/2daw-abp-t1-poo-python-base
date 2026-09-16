class Animal:
    def __init__(self, nom):
        self.nom = nom

    def menja(self):
        print(f"{self.nom} està menjant")

    def dorm(self):
        print(f"{self.nom} està dormint")

    def corre(self):
        print(f"{self.nom} està corrent")

    def __str__(self):
        return f"Soc el/l'animal anomenat {self.nom}"
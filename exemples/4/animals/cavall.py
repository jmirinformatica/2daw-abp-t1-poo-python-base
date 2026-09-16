from . import Animal

class Cavall(Animal):
    def corre(self):
        super().corre()
        print("... i va molt ràpid!")

    def __str__(self):
        desc = super().__str__()
        return desc + " i soc un cavall"
from animals import Gos, Tortuga, Cavall

un_gos = Gos("Papitu")
un_gos.menja()
un_gos.dorm()
un_gos.corre()
print(un_gos)

una_tortuga = Tortuga("Pepa")
una_tortuga.menja()
una_tortuga.dorm()
una_tortuga.corre()
una_tortuga.neda()
print(una_tortuga)

un_cavall = Cavall("Ferdinand")
un_cavall.menja()
un_cavall.dorm()
un_cavall.corre()
print(un_cavall)

# polimorfisme
print("------------------------------------------------------------")
llista_animals = [un_gos, una_tortuga, un_cavall]
for animal in llista_animals:
    animal.corre()

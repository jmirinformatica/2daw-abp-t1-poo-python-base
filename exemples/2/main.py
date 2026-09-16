from alumne import Alumne

a1 = Alumne("Alfonso", 49)
a2 = Alumne("Marta", 24)

a2.edat = 25
#a2.edat = None  # edat no vàlida
#a2.edat = "0" # edat no vàlida
#a2.edat = 0  # edat no vàlida

print(Alumne.nombre_alumnes)
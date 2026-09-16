from escola import Alumne, Assignatura

alumne1 = Alumne("Marta")
alumne2 = Alumne("Pere")

assignatura1 = Assignatura("Matemàtiques")
assignatura2 = Assignatura("Física")
assignatura3 = Assignatura("Química")

alumne1.afegeix_assignatura(assignatura1)
alumne1.afegeix_assignatura(assignatura2)

alumne2.afegeix_assignatura(assignatura1)
alumne2.afegeix_assignatura(assignatura3)

print("-----")
alumne1.llista_assignatures()
print("-----")
alumne2.llista_assignatures()   

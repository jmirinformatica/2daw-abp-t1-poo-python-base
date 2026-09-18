from vehicles import Cotxe, Moto

cotxe = Cotxe("Cupra", "Raval", 5)
print(cotxe)
cotxe.mostra_seguretat()
cotxe.start()
cotxe.stop()

moto = Moto("Kawasaki", "Ninja")
print(moto)
moto.mostra_seguretat()
moto.start()
moto.stop()

# error pq no es pot instanciar una classe abstracta
# vehicle = Vehicle()
from cotxe import Cotxe

cotxe1 = Cotxe("Renault Megane", 2012, "verd", True)
cotxe2 = Cotxe("Seat Toledo", 1987, "vermell", False)

cotxe1.start()
cotxe2.start()

cotxe2.stop()
cotxe1.stop()
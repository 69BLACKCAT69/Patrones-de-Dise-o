class TazaEuropea:
    def servir(self):
        print("☕ Sirviendo café en taza europea.")

class TazaAmericana:
    def serve_coffee(self):
        print("☕ Serving coffee in American mug.")

class AdaptadorTazaAmericana:
    def __init__(self, taza_americana):
        self.taza = taza_americana

    def servir(self):
        self.taza.serve_coffee()

# Uso
taza1 = TazaEuropea()
taza2 = AdaptadorTazaAmericana(TazaAmericana())
taza1.servir()
taza2.servir()

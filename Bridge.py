class PreparacionCafé:
    def preparar(self):
        pass

class Expreso(PreparacionCafé):
    def preparar(self):
        return "Espresso"

class Capuchino(PreparacionCafé):
    def preparar(self):
        return "Capuchino"

class Barista:
    def __init__(self, tipo_preparacion):
        self.tipo = tipo_preparacion

    def servir(self):
        print(f"☕ Sirviendo un {self.tipo.preparar()}")

# Uso
barista1 = Barista(Expreso())
barista2 = Barista(Capuchino())
barista1.servir()
barista2.servir()

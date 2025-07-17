class CafeBase:
    def obtener_descripcion(self):
        return "Café"

    def costo(self):
        return 30

class ConLeche:
    def __init__(self, cafe):
        self.cafe = cafe

    def obtener_descripcion(self):
        return self.cafe.obtener_descripcion() + " con leche"

    def costo(self):
        return self.cafe.costo() + 10

class ConCanela:
    def __init__(self, cafe):
        self.cafe = cafe

    def obtener_descripcion(self):
        return self.cafe.obtener_descripcion() + " con canela"

    def costo(self):
        return self.cafe.costo() + 5

# Uso
cafe = CafeBase()
cafe = ConLeche(cafe)
cafe = ConCanela(cafe)
print(cafe.obtener_descripcion())  # Café con leche con canela
print(f"💵 Total: ${cafe.costo()} pesos")

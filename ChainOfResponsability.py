class Empleado:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def manejar_pedido(self, pedido):
        if self.siguiente:
            self.siguiente.manejar_pedido(pedido)
        else:
            print("❌ Nadie pudo manejar el pedido.")

class Mesero(Empleado):
    def manejar_pedido(self, pedido):
        if pedido == "agua":
            print("🚶‍♂️ Mesero trae el agua.")
        else:
            super().manejar_pedido(pedido)

class Barista(Empleado):
    def manejar_pedido(self, pedido):
        if pedido == "café":
            print("👨‍🍳 Barista prepara el café.")
        else:
            super().manejar_pedido(pedido)

# Uso
cadena = Mesero(Barista())
cadena.manejar_pedido("agua")
cadena.manejar_pedido("café")
cadena.manejar_pedido("pastel")

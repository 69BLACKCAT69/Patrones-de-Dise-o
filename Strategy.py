class PagoEstrategia:
    def pagar(self, cantidad):
        pass

class PagoEfectivo(PagoEstrategia):
    def pagar(self, cantidad):
        print(f"🪙 Pagado en efectivo: ${cantidad} pesos")

class PagoTarjeta(PagoEstrategia):
    def pagar(self, cantidad):
        print(f"💳 Pagado con tarjeta: ${cantidad} pesos")

class Cliente:
    def __init__(self, estrategia_pago):
        self.estrategia = estrategia_pago

    def realizar_pago(self, cantidad):
        self.estrategia.pagar(cantidad)

# Uso
cliente1 = Cliente(PagoEfectivo())
cliente2 = Cliente(PagoTarjeta())
cliente1.realizar_pago(100)
cliente2.realizar_pago(150)

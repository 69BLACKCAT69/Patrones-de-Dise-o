class CajaRegistradora:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("🧾 Creando la caja registradora...")
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def cobrar(self, cantidad):
        print(f"💰 Cobrado: ${cantidad} pesos")

# Uso
caja1 = CajaRegistradora()
caja2 = CajaRegistradora()
print(caja1 is caja2)  # True

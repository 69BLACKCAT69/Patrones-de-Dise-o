# Patrones-de-Diseño

☕ Escenario: Cafetería Virtual


---

1️⃣ Singleton — Solo puede existir una caja registradora

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


---

2️⃣ Adapter — Adaptar una taza americana a la taza que usamos

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


---

3️⃣ Bridge — Separar la forma de preparar el café de cómo se sirve

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


---

4️⃣ Decorator — Añadir ingredientes al café sin cambiar su clase

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


---

5️⃣ Chain of Responsibility — Cada empleado decide si puede preparar un pedido

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


---

6️⃣ Strategy — Seleccionar forma de pago (efectivo, tarjeta, QR)

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


---

✅ Conclusión

Todos estos patrones están en el mismo mundo: una cafetería.

Singleton: solo una caja

Adapter: adaptar objetos diferentes

Bridge: separar preparación de servicio

Decorator: añadir ingredientes al vuelo

Chain: empleados manejan lo que pueden

Strategy: cambiar la forma de pagar

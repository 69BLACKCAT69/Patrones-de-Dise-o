# Patrones de Diseño en una Cafetería Virtual

Este README.md describe la implementación de varios patrones de diseño creacionales, estructurales y de comportamiento utilizando el escenario de una cafetería virtual. Cada sección presenta un patrón con su respectiva explicación y código Python.

## 1. Singleton

**Descripción:** El patrón Singleton asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a ella. En este ejemplo, la `CajaRegistradora` es un Singleton, garantizando que solo haya una caja registradora en la cafetería.

**Código:**

\`\`\`python
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
\`\`\`

## 2. Adapter

**Descripción:** El patrón Adapter permite que clases con interfaces incompatibles trabajen juntas. Actúa como un traductor entre dos interfaces. Aquí, el `AdaptadorTazaAmericana` adapta la interfaz de `TazaAmericana` a la interfaz esperada por la cafetería (`servir`).

**Código:**

\`\`\`python
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
\`\`\`

## 3. Bridge

**Descripción:** El patrón Bridge desacopla una abstracción de su implementación, de manera que ambas puedan variar independientemente. En este caso, separa la forma de `PreparacionCafé` (abstracción) de la entidad que la utiliza para servir (`Barista` - implementación).

**Código:**

\`\`\`python
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
\`\`\`

## 4. Decorator

**Descripción:** El patrón Decorator permite añadir funcionalidades a un objeto dinámicamente, envolviéndolo en un objeto decorador. Aquí, `ConLeche` y `ConCanela` son decoradores que añaden ingredientes y modifican la descripción y el costo de un objeto `CafeBase`.

**Código:**

\`\`\`python
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
\`\`\`

## 5. Chain of Responsibility

**Descripción:** El patrón Chain of Responsibility permite pasar una petición a través de una cadena de objetos hasta que uno de ellos la maneje. Cada objeto en la cadena decide si puede procesar la petición o si debe pasarla al siguiente. En este ejemplo, `Mesero` y `Barista` forman una cadena para manejar pedidos.

**Código:**

\`\`\`python
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
\`\`\`

## 6. Strategy

**Descripción:** El patrón Strategy define una familia de algoritmos, encapsula cada uno y los hace intercambiables. Esto permite al algoritmo variar independientemente de los clientes que lo utilizan. Aquí, diferentes estrategias de pago (`PagoEfectivo`, `PagoTarjeta`) pueden ser utilizadas por el `Cliente`.

**Código:**

\`\`\`python
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
\`\`\`

## ✅ Conclusión

Este ejemplo muestra cómo diferentes patrones de diseño pueden aplicarse en un contexto común como una cafetería virtual para resolver distintos problemas de diseño y mejorar la flexibilidad y mantenibilidad del código.

class BebidaPersonalizada:
    def __init__(self):
        self.ingredientes = []

    def mostrar(self):
        print("🧋 Bebida con:", ", ".join(self.ingredientes))

# Constructor paso a paso
class BebidaBuilder:
    def __init__(self):
        self.bebida = BebidaPersonalizada()

    def añadir_agua(self):
        self.bebida.ingredientes.append("agua");
        return self
    def añadir_café(self):
        self.bebida.ingredientes.append("café");
        return self
    def añadir_leche(self):
        self.bebida.ingredientes.append("leche"); 
        return self
    def añadir_azúcar(self):
        self.bebida.ingredientes.append("azúcar");
        return self
    def obtener(self):
        return self.bebida

# Cliente
builder = BebidaBuilder()
bebida = builder.añadir_agua().añadir_café().añadir_leche().añadir_azúcar().obtener()
bebida.mostrar()  # Output: 🧋 Bebida con: agua, café, leche, azúcar
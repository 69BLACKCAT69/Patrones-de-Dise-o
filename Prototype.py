import copy

class RecetaBebida:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar(self):
        print(f"🍶 {self.nombre} con:", ", ".join(self.ingredientes))

# Receta original
receta_base = RecetaBebida("Latte", ["leche", "café", "azúcar"])
receta_base.mostrar()

# Clon personalizado
receta_con_canela = receta_base.clonar()
receta_con_canela.nombre = "Latte con canela"
receta_con_canela.ingredientes.append("canela")
receta_con_canela.mostrar()
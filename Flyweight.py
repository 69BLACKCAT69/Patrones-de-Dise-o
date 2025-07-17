class IngredienteFlyweight:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self):
        return f"Usando ingrediente: {self.nombre}"

# Flyweight Factory (gestiona instancias compartidas)
class IngredienteFactory:
    _ingredientes = {}

    @classmethod
    def obtener(cls, nombre):
        if nombre not in cls._ingredientes:
            cls._ingredientes[nombre] = IngredienteFlyweight(nombre)
        return cls._ingredientes[nombre]

# Clase que representa una bebida (usa ingredientes compartidos)
class Bebida:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = []

    def añadir_ingrediente(self, nombre_ingrediente):
        ingrediente = IngredienteFactory.obtener(nombre_ingrediente)
        self.ingredientes.append(ingrediente)

    def mostrar(self):
        print(f"🧋 {self.nombre} contiene:")
        for ing in self.ingredientes:
            print(f"  - {ing.usar()}")

# Cliente
latte = Bebida("Latte")
latte.añadir_ingrediente("leche")
latte.añadir_ingrediente("café")
latte.añadir_ingrediente("azúcar")

moka = Bebida("Moka")
moka.añadir_ingrediente("leche")
moka.añadir_ingrediente("café")
moka.añadir_ingrediente("chocolate")

latte.mostrar()
moka.mostrar()
class SingletonMeta(type):
    """
    Metaclase para implementar el patrón Singleton.
    Se asegura de que solo haya una instancia de la clase.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Creando nueva instancia de {cls.__name__}")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"Usando instancia existente de {cls.__name__}")
        return cls._instances[cls]


class Configuracion(metaclass=SingletonMeta):
    """
    Clase que representa una configuración global del sistema.
    Usa la metaclase SingletonMeta para garantizar una única instancia.
    """
    def __init__(self):
        self._datos = {}

    def establecer(self, clave, valor):
        self._datos[clave] = valor

    def obtener(self, clave):
        return self._datos.get(clave)

    def mostrar_configuracion(self):
        print("Configuración actual:", self._datos)


# ================================
# Ejemplo de uso del Singleton
# ================================

if __name__ == "__main__":
    config1 = Configuracion()
    config1.establecer("modo", "producción")
    config1.establecer("debug", False)

    config2 = Configuracion()
    config2.establecer("host", "localhost")

    config1.mostrar_configuracion()
    config2.mostrar_configuracion()

    print("¿config1 es config2?", config1 is config2)  # True

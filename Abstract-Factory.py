from abc import ABC, abstractmethod

# Productos abstractos
class Vaso(ABC):
    @abstractmethod
    def usar(self): pass

class Tapa(ABC):
    @abstractmethod
    def tapar(self): pass

# Productos concretos
class VasoCafé(Vaso):
    def usar(self): return "Vaso de cartón para café ☕"

class TapaCafé(Tapa):
    def tapar(self): return "Tapa negra para café ☕"

class VasoJugo(Vaso):
    def usar(self): return "Vaso transparente para jugo 🧃"

class TapaJugo(Tapa):
    def tapar(self): return "Tapa con popote para jugo 🧃"

# Fábrica abstracta
class KitBebidaFactory(ABC):
    @abstractmethod
    def crear_vaso(self): pass
    @abstractmethod
    def crear_tapa(self): pass

# Fábricas concretas
class CaféFactory(KitBebidaFactory):
    def crear_vaso(self): return VasoCafé()
    def crear_tapa(self): return TapaCafé()

class JugoFactory(KitBebidaFactory):
    def crear_vaso(self): return VasoJugo()
    def crear_tapa(self): return TapaJugo()

# Cliente
def entregar_kit(factory: KitBebidaFactory):
    vaso = factory.crear_vaso()
    tapa = factory.crear_tapa()
    print(vaso.usar())
    print(tapa.tapar())

entregar_kit(CaféFactory())
entregar_kit(JugoFactory())
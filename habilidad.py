# =========================
# INTERFAZ / CLASE ABSTRACTA: HABILIDAD
# =========================
# Esta clase define qué acciones básicas debe tener cualquier
# personaje jugable del juego.
# No se usa directamente para crear objetos.
# Sirve como "norma" que las clases hijas deben cumplir.

from abc import ABC, abstractmethod

class Habilidad(ABC):
    # =========================
    # 1) ATACAR
    # =========================
    # Obliga a las clases hijas a implementar un método atacar.
    # Recibe un enemigo y ejecuta el ataque correspondiente.
    @abstractmethod
    def atacar(self, enemigo) -> None:
        pass

    # =========================
    # 2) DEFENDER
    # =========================
    # Obliga a implementar el método defender.
    # Devuelve un booleano para indicar si el personaje
    # se ha defendido en ese turno.
    @abstractmethod
    def defender(self) -> bool:
        pass


    # =========================
    # 3) HABILIDAD ESPECIAL
    # =========================
    # Cada personaje debe tener una habilidad especial.
    # Recibe un enemigo y aplica un efecto especial.
    @abstractmethod
    def habilidad_especial(self, enemigo) -> None:
        pass


# CAMBIOS RECIENTES (2026-01-02)
# - Ajustado interfaz para que coincidan:
#   atacar(self, enemigo) -> None, defender(self) -> bool, habilidad_especial(self, enemigo) -> None
# CAMBIOS RECIENTES (2026-01-02)
# - 'defender' ahora devuelve bool explícitamente para cumplir la interfaz Habilidad.

from habilidad import Habilidad
from personaje import Personaje

class Mago(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque mágico", vida: int = 110, daño: int = 40, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self, enemigo) -> None:
        print(f"El mago {self.nombre} ataca con su magia.")
        enemigo.recibir_daño(self.daño)

    def defender(self) -> bool:
        print(f"El mago {self.nombre} ha generado un escudo mágico.")
        return True

    def habilidad_especial(self, enemigo) -> None:
        print(f"¡El mago {self.nombre} conjura un hechizo muy poderoso!")
        self.daño += 20
        self.atacar(enemigo)
        self.daño -= 20

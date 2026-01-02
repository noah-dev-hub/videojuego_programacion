# CAMBIOS RECIENTES (2026-01-02)
# - 'defender' ahora devuelve bool explícitamente para cumplir la interfaz Habilidad.

from habilidad import Habilidad
from personaje import Personaje

class Ladron(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque rápido", vida: int = 90, daño: int = 20, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self, enemigo) -> None:
        print(f"El ladrón {self.nombre} ataca con su daga.")
        enemigo.recibir_daño(self.daño)

    def defender(self) -> bool:
        print(f"El ladrón {self.nombre} esquiva el ataque enemigo.")
        return True

    def habilidad_especial(self, enemigo) -> None:
        print(f"¡El ladrón {self.nombre} ha envenenado su arma!")
        self.daño += 30
        self.atacar(enemigo)
        self.daño -= 30

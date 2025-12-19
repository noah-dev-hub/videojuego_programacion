
from habilidad import Habilidad
from personaje import Personaje

class Guerrero(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque melé", vida: int = 110, daño: int = 30, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self) -> str:
        return f"El guerrero {self.nombre} ataca con su espada."

    def defender(self) -> str:
        return f"El guerrero {self.nombre} se defiende con su escudo."

    def tomar_pocion(self) -> str:
        self.vida += 20
        return f"El guerrero {self.nombre} se toma una poción de recuperación de vida. Recupera 20 puntos."
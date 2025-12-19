
from habilidad import Habilidad
from personaje import Personaje

class Ladron(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque rápido", vida: int = 100, daño: int = 20, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self) -> str:
        return f"El ladrón {self.nombre} ataca con su daga."

    def defender(self) -> str:
        return f"El ladrón {self.nombre} se defiende esquivando."

    def tomar_pocion(self) -> str:
        self.vida += 20
        return f"El ladrón {self.nombre} se toma una poción de recuperación de vida. Recupera 20 puntos."
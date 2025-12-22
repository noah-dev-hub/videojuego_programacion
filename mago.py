
from habilidad import Habilidad
from personaje import Personaje

class Mago(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque mágico", vida: int = 80, daño: int = 40, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self) -> str:
        return f"El mago {self.nombre} ataca con su magia."

    def defender(self) -> str:
        return f"El mago {self.nombre} se defiende con su magia."

    def tomar_pocion(self) -> str:
        self.vida += 20
        return f"El mago {self.nombre} se toma una poción de recuperación de vida. Recupera 20 puntos."
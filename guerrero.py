
from habilidad import Habilidad
from personaje import Personaje
import pocion

class Guerrero(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque melé", vida: int = 110, daño: int = 30, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self) -> str:
        return f"El guerrero {self.nombre} ataca con su espada."

    def defender(self) -> str:
        return f"El guerrero {self.nombre} se defiende con su escudo."

    # Recordar modificar
    def habilidad_especial(self) -> str:
        self.daño += 5
        return f"El orco {self.nombre} entra en furia y aumenta su daño."



from enemigo import Enemigo

class Arpia(Enemigo):
    def __init__(self, nombre: str = "Arpía", vida: int = 90, daño: int = 20, nivel: int = 1)
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self) -> str:
        return f"La arpía {self.nombre} ataca desde el aire con sus garras."

    def habilidad_especial(self) -> str:
        self.vida += 10
        return f"La arpía {self.nombre} se recupera y gana +10 de vida."

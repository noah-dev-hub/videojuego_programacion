from enemigo import Enemigo

class Orco(Enemigo):
    def __init__(self, nombre: str = "Orco", vida: int = 120, daño: int = 25, nivel: int = 1) -> None:
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self) -> str:
        return f"El orco {self.nombre} ataca con su garrote."

    def habilidad_especial(self) -> str:
        self.daño += 5
        return f"El orco {self.nombre} entra en furia y aumenta su daño."

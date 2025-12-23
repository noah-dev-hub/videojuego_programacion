
from habilidad import Habilidad
from personaje import Personaje
from enemigo import Enemigo

class Ladron(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque rápido", vida: int = 90, daño: int = 20, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self) -> None:
        Enemigo.recibir_daño(self.daño)
        print(f"El ladrón {self.nombre} ataca con su daga.")

    def defender(self) -> None:
        self.recibir_daño(-Enemigo.daño)
        print(f"El ladrón {self.nombre} esquiva el ataque enemigo.")

    def habilidad_especial(self) -> None:
        self.daño += 30
        self.atacar
        self.daño -= 30
        print(f"¡El ladrón {self.nombre} ha lanzado una bomba!")
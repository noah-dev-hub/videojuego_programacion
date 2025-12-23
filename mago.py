
from habilidad import Habilidad
from personaje import Personaje
from enemigo import Enemigo

class Mago(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque mágico", vida: int = 70, daño: int = 40, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self, enemigo) -> None:
        enemigo.recibir_daño(self.daño)
        print(f"El mago {self.nombre} ataca con su magia.")
        print(f"Enemigo: {enemigo.vida}")

    def defender(self, enemigo) -> None:
        self.recibir_daño(-enemigo.daño)
        print(f"El mago {self.nombre} ha generado un escudo mágico.")

    def habilidad_especial(self, enemigo) -> None:
        self.daño += 20
        self.atacar(enemigo)
        self.daño -= 20
        print(f"¡El mago {self.nombre} ha usado un hechizo muy poderoso!")
        print(f"Enemigo: {enemigo.vida}")
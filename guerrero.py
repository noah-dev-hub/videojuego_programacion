
from habilidad import Habilidad
from personaje import Personaje
import pocion

class Guerrero(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque melé", vida: int = 110, daño: int = 30, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self, enemigo) -> None:
        print(f"El guerrero {self.nombre} ataca con su espada.")
        enemigo.recibir_daño(self.daño) # Enlaza el ataque con el enemigo

    def defender(self) -> bool:
        print(f"El guerrero {self.nombre} se defiende con su escudo.")
        return True # Devuelve un booleano que se pasará a la función 'recibir_daño()' para evitar que lo reciba

    def habilidad_especial(self, enemigo) -> None:
        print(f"¡El guerrero {self.nombre} se carga de rabia!")
        self.daño += 10
        self.atacar(enemigo) # Llama a la función 'atacar'
        self.daño -= 10 # Devuelve el daño a su valor inicial después de un ataque especial
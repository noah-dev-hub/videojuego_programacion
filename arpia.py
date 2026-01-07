from enemigo import Enemigo
from habilidad import Habilidad

class Arpia(Enemigo, Habilidad):
    def __init__(self, nombre: str = "Arpía", vida: int = 90, daño: int = 20, nivel: int = 2) -> None:
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self, personaje, defensa) -> None:
        # Ataca al personaje y le quita vida según el daño de la arpía
        print(f"La {self.nombre} ataca desde el aire con sus garras.")
        personaje.recibir_daño(self.daño, defensa)

    def defender(self):
        return super().defender()

    def habilidad_especial(self) -> None:
        # Se cura un poco para aguantar más
        self.vida += 10
        print(f"La arpía {self.nombre} se eleva y recupera 10 de vida.")
        print(f"{self.nombre}: {self.vida}")

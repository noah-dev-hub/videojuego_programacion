from enemigo import Enemigo

class Oscar(Enemigo):
    def __init__(self, nombre: str = "Óscar (Jefe final)", vida: int = 200, daño: int = 35, nivel: int = 3)
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self) -> str:
        return f"{self.nombre} lanza un ataque devastador."

    def habilidad_especial(self) -> str:
        self.nivel += 1
        self.daño += 10
        return f"{self.nombre} entra en fase 2: nivel +1 y daño +10."

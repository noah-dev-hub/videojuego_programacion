from enemigo import Enemigo
# Los ataques y habilidades de los enemigos son esencialmente propios de cada uno. No heredan de la clase 'Habilidad' como los personajes jugables
# porque no comparten el mismo sistema que éstos.

class Orco(Enemigo):
    def __init__(self, nombre: str = "Orco", vida: int = 120, daño: int = 25, nivel: int = 1) -> None:
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self, personaje, defensa) -> None: # Recibe la variable 'defensa' y se la manda a la función 'recibir_daño()'
        # El orco pega al personaje
        print(f"El {self.nombre} ataca con su garrote.")
        personaje.recibir_daño(self.daño, defensa)

    def habilidad_especial(self) -> None:
        # Se enfurece: sube daño
        self.daño += 5
        print(f"El orco {self.nombre} entra en furia y aumenta su daño en +5.")
        print(f"Daño actual del orco: {self.daño}")

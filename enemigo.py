class Enemigo:
    def __init__(self, nombre: str, vida: int, daño: int, nivel: int) -> None:
        self._nombre = nombre
        self.vida = vida
        self._daño = daño
        self._nivel = nivel

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def daño(self) -> int:
        return self._daño
    
    @daño.setter
    def daño(self, daño: int) -> None:
        self._daño = daño

    @property
    def nivel(self) -> int:
        return self._nivel
    
    @nivel.setter
    def nivel(self, nivel: int) -> None:
        self._nivel = nivel

    def esta_vivo(self) -> bool: 
        return self.vida > 0

    def recibir_daño(self, cantidad: int) -> None:
        self.vida = max(0, self.vida - cantidad) #Max 0, para que si quitan 15 de daño y tenemos 10 de vida, no salga la vida en negativo.  La funcion de arriba es reutilizable mas adelante.

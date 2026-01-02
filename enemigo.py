# =========================
# CLASE ENEMIGO
# =========================
# Esta clase representa a cualquier enemigo del juego.

class Enemigo:
    def __init__(self, nombre: str, vida: int, daño: int, nivel: int) -> None:
        self._nombre = nombre
        self.vida = vida
        self._daño = daño
        self._nivel = nivel
        # print("El enemigo ha sido creado.")  # Ya sabemos que funciona. La quito para que no salga en el juego.


    # =========================
    # GETTERS Y SETTERS
    # =========================
    # Permiten acceder y modificar atributos privados
    # de forma controlada.

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
        
    # Devuelve True si el enemigo sigue vivo.
    def esta_vivo(self) -> bool:
        return self.vida > 0
    
    # Reduce la vida del enemigo cuando es atacado.
    # Se asegura de que la vida no baje de 0.
    def recibir_daño(self, cantidad: int) -> None:
        self.vida = max(0, self.vida - cantidad)

    def __str__(self) -> str:  # Lo voy a dejar opcional por si quiero imprimir el enemigo. Mas adelante si no hace falta lo quito.
        return f"{self.nombre} - Vida: {self.vida} - Daño: {self.daño} - Nivel: {self.nivel}"

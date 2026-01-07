# =========================
# CLASE PERSONAJE
# =========================
# Esta clase representa a cualquier personaje controlado por el jugador.
# Define sus atributos básicos (vida, daño, nivel, etc.)
# y el comportamiento común que todos los personajes comparten.

class Personaje:
    def __init__(self, nombre: str, rol: str, vida: int, daño: int, nivel: int) -> None:
        self._nombre = nombre
        self._rol = rol
        self.vida = vida
        self._daño = daño
        self._nivel = nivel
        self.escudo = 0  # Puntos de armadura/escudo que absorben daño antes de la vida

    # =========================
    # GETTERS Y SETTERS
    # =========================
    # Se usan para acceder y modificar atributos "privados"
    # de forma controlada.

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def rol(self) -> str:
        return self._rol
    
    @rol.setter
    def rol(self, rol: str) -> None:
        self._rol = rol

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

    # Devuelve True si el personaje sigue vivo.
    def esta_vivo(self) -> bool: 
        return self.vida > 0

    """
    Guía de la función 'recibir_daño': (Para mi futuro yo en la exposicion :=D)    
    Esta función se llama cuando un enemigo ataca al personaje.
    Su trabajo es decidir cuánta vida pierde el personaje, teniendo en cuenta:
    El escudo (armadura que absorbe daño).
    Si el personaje se defendió ese turno.
    Si el personaje muere o sobrevive.
    """
    def recibir_daño(self, cantidad: int, defensa: bool) -> None:
        
        """Aplica daño al personaje teniendo en cuenta escudo y defensa.
        Orden:
        1) El escudo absorbe primero.
        2) Si el jugador se defendió, el daño restante se reduce a la mitad.
        3) Lo que quede reduce la vida.
        """
        
        daño = max(0, int(cantidad))

        # 1) Absorción por escudo
        # El escudo absorbe el daño antes de que llegue a la vida.
        if self.escudo > 0 and daño > 0:
            absorbido = min(self.escudo, daño)
            self.escudo -= absorbido
            daño -= absorbido
            print(f"El escudo absorbe {absorbido} de daño. Escudo restante: {self.escudo}")
        elif self.escudo > 0 and daño == 0:
            print(f"El escudo permanece intacto. Escudo actual: {self.escudo}")

        # 2) Reducción por defensa 
        # Si el jugador se defendió, el daño restante se reduce a la mitad.
        if defensa and daño > 0:
            reducido = (daño + 1) // 2  # redondeo hacia arriba para que se note
            print(f"¡{self.nombre} se defiende! Daño reducido de {daño} a {reducido}.")
            daño = reducido
        elif defensa and daño == 0:
            print(f"¡{self.nombre} se defiende! No recibe daño.")

        # 3) Aplicación a vida
        if daño > 0:
            self.vida = max(0, self.vida - daño)
            if not self.esta_vivo():
                print(f"¡Oh, no! ¡{self.nombre} ha muerto!")
            else:
                print(f"¡{self.nombre} ha sido herido!")
        else:
            if self.esta_vivo():
                print(f"{self.nombre} no recibe daño. Vida: {self.vida}")

    def __str__(self) -> str:  # Copio aquí lo que hiciste en 'Enemigo' para mostrar los datos antes de elegir personaje
        return f"{self.nombre} - Vida: {self.vida} - Daño: {self.daño} - Nivel: {self.nivel}"

# CAMBIOS RECIENTES (2026-01-02)
# - Añadido atributo 'escudo' al personaje (armadura que absorbe daño).
# - 'recibir_daño' ahora aplica: escudo -> defensa (reduce a la mitad) -> vida, con mensajes de feedback.
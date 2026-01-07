# =========================
# CLASE POCIÓN (CLASE BASE)
# =========================
# Esta clase representa el concepto general de una poción.
# No se usa directamente, sino que sirve como base para
# las distintas pociones del juego (vida, daño, escudo).

class Pocion():
    def __init__(self, tipo: str, efecto: int) -> None:
        # Atributos privados
        self.__tipo = tipo
        self.__efecto = efecto

    # =========================
    # GETTERS Y SETTERS
    # =========================
    # Permiten acceder y modificar los atributos privados
    # de forma controlada.

    @property
    def tipo(self) -> str:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo) -> str:
        self.__tipo = tipo

    @property
    def efecto(self) -> int:
        return self.__efecto
    
    @efecto.setter
    def efecto(self, efecto) -> int:
        self.__efecto = efecto
    # =========================
    # MÉTODO GENERAL
    # =========================
    # Este método se sobrescribe en las clases hijas.
    # La clase base no define un comportamiento concreto.
    
    def tomar_pocion(self):
        pass
            
# Las pociones son objetos que heredan de 'Pocion'
class Vida(Pocion):
    def  __init__(self, tipo = "Recuperación de vida", efecto = 30):
        super().__init__(tipo, efecto)

    def tomar_pocion(self, personaje):
        print(f"{personaje.nombre} se toma una poción de {self.tipo}.")
        personaje.vida += self.efecto
        print(f"{personaje.nombre} recupera {self.efecto} puntos de vida")

class Daño(Pocion):
    def  __init__(self, tipo = "Aumento de daño", efecto = 15):
        super().__init__(tipo, efecto)

    def tomar_pocion(self, personaje):
        print(f"{personaje.nombre} se toma una poción de {self.tipo}.")
        personaje.daño += self.efecto
        print(f"{personaje.nombre} aumenta su daño en {self.efecto} puntos.")

class Escudo(Pocion): # Le quita daño al enemigo, pero se lo quita para siempre. Si queremos que sea así, perfecto. Si no, hay que encontrar la forma de arreglarlo.
    # CAMBIO (2026-01-02): Se ha 'arreglado' para que el escudo sea una armadura que absorbe X puntos de daño (no modifica al enemigo).
    def  __init__(self, tipo = "Generación de escudo", efecto = 50):
        super().__init__(tipo, efecto)

    def tomar_pocion(self, personaje):
        print(f"{personaje.nombre} se toma una poción de {self.tipo}.")
        personaje.escudo += self.efecto
        print(f"{personaje.nombre} obtiene un escudo de {self.efecto} puntos.")
        print(f"Escudo total: {personaje.escudo}")

# CAMBIOS RECIENTES (2026-01-02)
# - 'Poción Escudo' ahora crea armadura en el personaje: absorbe daño antes de restar vida (no altera el daño del enemigo).
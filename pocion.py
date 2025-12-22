class Pocion:
    def __init__(self, tipo: str, efecto: int) -> None:
        # Atributos privados
        self.__tipo = tipo
        self.__efecto = efecto

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

    def tomar_pocion(self, personaje):
        if self.__tipo == "Recuperación de vida":
            personaje.vida += self.__efecto
            print(f"{personaje.nombre} recupera {self.__efecto} de vida")

        elif self.__tipo == "Daño":
            personaje.daño += self.__efecto
            print(f"{personaje.nombre} aumenta su daño en {self.__efecto}")

        elif self.__tipo == "Escudo":
            personaje.vida += self.__efecto
            print(f"{personaje.nombre} obtiene un escudo de {self.__efecto}")

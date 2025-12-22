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
    def tipo(self, efecto) -> int:
        self.__efecto = efecto

    def tomar_pocion(self):
        pass


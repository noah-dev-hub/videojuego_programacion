
from abc import ABC
from abc import abstractmethod

class Habilidad(ABC):
# Devuelve none, en los modulos guerrero, ladron, mago, devuelve str. Es confuso
    @abstractmethod
    def atacar(self) -> None:   
        pass

    @abstractmethod
    def defender(self) -> None:
        pass

    @abstractmethod
    def tomar_pocion(self) -> None: 
        pass
    

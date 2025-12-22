
from abc import ABC
from abc import abstractmethod

class Habilidad(ABC):
# Devuelve none, en los modulos guerrero, ladron, mago, devuelve str. Es confuso
    @abstractmethod
    def atacar(self) -> str:   
        pass

    @abstractmethod
    def defender(self) -> str:
        pass

    @abstractmethod
    def habilidad_especial(self) -> str:
        pass

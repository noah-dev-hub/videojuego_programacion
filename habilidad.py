
from abc import ABC
from abc import abstractmethod

class Habilidad(ABC):
    @abstractmethod
    def atacar(self) -> None:   
        pass

    @abstractmethod
    def defender(self) -> None:
        pass

    @abstractmethod
    def habilidad_especial(self) -> None:
        pass

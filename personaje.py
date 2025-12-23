
class Personaje:
    def __init__(self, nombre: str, rol: str, vida: int, daño: int, nivel: int) -> None:
        self._nombre = nombre
        self._rol = rol
        self.vida = vida
        self._daño = daño
        self._nivel = nivel
        print("El personaje ha sido creado.")

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
        
# Podemos usar esta funcion para mas adelante. 
    def esta_vivo(self) -> bool:
        return self.vida > 0

    def recibir_daño(self, cantidad: int) -> None: # Añade feedbback
        self.vida = max(0, self.vida - cantidad)
        if not self.esta_vivo(): # Implementa la función 'esta_vivo()'
            print(f"¡Oh, no!¡{self.nombre} ha muerto!")
        else:
            print(f"¡{self.nombre} ha sido herido!\nVida: {self.vida}")


    
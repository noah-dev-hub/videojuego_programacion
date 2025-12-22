# Archivo principal del videojuego

from guerrero import Guerrero
from mago import Mago
from ladron import Ladron

from orco import Orco
from arpia import Arpia
from oscar import Oscar

import pocion

vida = pocion.Pocion("Recuperación de vida", 10)
daño = pocion.Pocion("Daño", 10)
escudo = pocion.Pocion("Escudo", 10)

# Pruebas para ver si las pociones funcionan. La poción tiene el método tomar_pocion, recibe un personaje y modifica directamente sus atributos según el tipo de poción.
guerrero = Guerrero("Cadalas")

print("Vida antes:", guerrero.vida)
vida.tomar_pocion(guerrero)
print("Vida después:", guerrero.vida)

"""
def menu():
    while True:
        print("\n------ MENÚ PRINCIPAL ------")
        print("| 1. Elegir personaje        |")
        print("| 2. Iniciar juego        |")
        print("| 3. Salir                  |")
        print("-----------------------------")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                elegir_personaje()

            case "2":
                iniciar_juego()

            case "3":
                print("Saliendo del juego...")
                break
            case _:
                print("Opción no válida")
                continue
                
if __name__ == "__main__":
    menu()
"""
# Archivo principal del videojuego

from guerrero import Guerrero
from mago import Mago
from ladron import Ladron

from orco import Orco
from arpia import Arpia
from oscar import Oscar

from pocion import Pocion

    def menu():
        while True:
            print("\n------ MENÚ PRINCIPAL ------")
            print("| 1. Crear personaje        |")
            print("| 2. Iniciar combate        |")
            print("| 3. Usar poción            |")
            print("| 4. Mostrar estado         |")
            print("| 5. Salir                  |")
            print("-----------------------------")

            opcion = input("Elige una opción: ")

            match opcion:
                case "1":
                    crear_personaje()

                case "2":
                    iniciar_combate()

                case "3":
                    usar_pocion()

                case "4":
                    mostrar_estado()

                case "5":
                    print("Saliendo del juego...")
                    break

                case _:
                    print("Opción no válida")
                    continue
                
if __name__ == "__main__":
    menu()
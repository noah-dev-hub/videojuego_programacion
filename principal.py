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
orco = Orco()
arpia = Arpia()
boss = Oscar()

# Prueba de las habilidades de los personajes. Funcionan, pero a veces imprimen frases que no quiero. Revisar.
guerrero = Guerrero("Cadalas")
print(f"Primer combate: \n¡{guerrero.nombre} se va a enfrentar a un {orco.nombre}!\nVida {orco.nombre}: {orco.vida}")
while guerrero.esta_vivo() and orco.esta_vivo():
    print("1- Atacar\n2- Defender\n3- Habilidad especial")
    opcion = ""
    while opcion != range(1,4):
        opcion = input(f"¿Qué va a hacer {guerrero.nombre}? ")
        match opcion:
            case "1":
                guerrero.atacar(orco)
            case "2":
                guerrero.defender(orco)
            case "3":
                guerrero.habilidad_especial(orco)
            case _:
                print(f"{guerrero.nombre} no sabe hacer eso.")
                opcion = input(f"¿Qué va a hacer {guerrero.nombre}?")
    if orco.vida <= 60:
        orco.habilidad_especial() # Habría que pasar el personaje como parámetro una vez modificada la función en la clase Orco.
    orco.atacar()



"""
# Pruebas para ver si las pociones funcionan. La poción tiene el método tomar_pocion, recibe un personaje y modifica directamente sus atributos según el tipo de poción.
print("Vida antes:", guerrero.vida)
vida.tomar_pocion(guerrero)
print("Vida después:", guerrero.vida)
"""

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
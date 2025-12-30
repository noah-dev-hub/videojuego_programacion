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

"""
# Pruebas para ver si las pociones funcionan. La poción tiene el método tomar_pocion, recibe un personaje y modifica directamente sus atributos según el tipo de poción.
print("Vida antes:", guerrero.vida)
vida.tomar_pocion(guerrero)
print("Vida después:", guerrero.vida)
"""

# Notas:
# - Defensa implementada.
# - Pendiente implementar pociones. Al avanzar de combate, el personaje no tiene vida suficiente y muere en seguida. Tal vez haya que hacer que las pociones recuperen más vida

def combate(personaje, enemigo) -> bool:
    contador_habilidad_enemigo = 0 # Sirve para conseguir que la habilidad del enemigo solo actúe una vez
    print(f"\n¡{personaje.nombre} se enfrenta a {enemigo.nombre}!")
    print(f"Vida {enemigo.nombre}: {enemigo.vida}")

    while personaje.esta_vivo() and enemigo.esta_vivo():
        defensa = False  # Resetea la variable defensa a False en cada turno con tal de que no se esté defendiendo para siempre
        print("1- Atacar")
        print("2- Defender")
        print("3- Habilidad especial")
        print("---------------------------")
        
        opcion = input(f"¿Qué va a hacer {personaje.nombre}? ")

        match opcion:
            case "1":
                personaje.atacar(enemigo)
            case "2":
                defensa = personaje.defender() # Se guarda aquí el return de la función
            case "3":
                personaje.habilidad_especial(enemigo)
            case _:
                print(f"{personaje.nombre} no sabe hacer eso.")
                continue

        print(f"Enemigo: {enemigo.vida}") # He sacado este print aquí para no tener que repetir esta línea en cada ataque de cada personajee
        # Si el enemigo muere, termina el combate
        if not enemigo.esta_vivo():
            print(f"\n{enemigo.nombre} ha sido derrotado.")
            return True

        # Habilidad especial del enemigo (ejemplo: cuando baja de la mitad)
        # La habilidad especial del enemigo se acumulaba cada turno. Añado una variable para hacer que solo actúe una vez.
        if enemigo.vida <= 60 and contador_habilidad_enemigo == 0:
            enemigo.habilidad_especial()
            contador_habilidad_enemigo = 1

        # Turno del enemigo
        enemigo.atacar(personaje, defensa) # Es aquí donde se manda la variable 'defensa' para que cumpla su función final
        print(f"{personaje.nombre}: {personaje.vida}") # Ésta igual que con el enemigo

    return personaje.esta_vivo()
                
def iniciar_juego():
    # Prueba de combate completo
    personaje = Guerrero("Cadalas")

    enemigos = [Orco(), Arpia(), Oscar()]

    for enemigo in enemigos:
        gana = combate(personaje, enemigo)
        if not gana:
            print("\nGAME OVER.")
            return # ?

    print("\n¡Has derrotado a todos los enemigos! ¡Victoria!")

if __name__ == "__main__":
    iniciar_juego()
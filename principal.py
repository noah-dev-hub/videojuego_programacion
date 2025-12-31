# Archivo principal del videojuego

from guerrero import Guerrero
from mago import Mago
from ladron import Ladron

from orco import Orco
from arpia import Arpia
from oscar import Oscar

from pocion import Vida, Daño, Escudo

# Notas:
# - Defensa implementada.
# - Pociones implementadas. Fíjate especialmente en la de escudo a ver si te gusta. Te la he descrito en su clase
# - Elección de personajes implementada
# - Pendiente implementar las subidas de nivel

def combate(personaje, enemigo) -> bool:
    # Cada tipo de poción es ahora un objeto distinto que hereda de 'Pocion'
    pocion_vida = Vida()
    pocion_daño = Daño()
    pocion_escudo = Escudo()
    cantidad_pociones = 3 # Variable para que las pociones no sean infinitas
    contador_habilidad_enemigo = 0 # Sirve para conseguir que la habilidad del enemigo solo actúe una vez
    print(f"\n¡{personaje.nombre} se enfrenta a {enemigo.nombre}!")
    print(f"Vida {enemigo.nombre}: {enemigo.vida}")

    while personaje.esta_vivo() and enemigo.esta_vivo():
        defensa = False  # Resetea la variable defensa a False en cada turno con tal de que no se esté defendiendo para siempre
        print("1- Atacar")
        print("2- Defender")
        print("3- Habilidad especial")
        print("4- Tomar poción")
        print("---------------------------")
        
        opcion = input(f"¿Qué va a hacer {personaje.nombre}? ")

        match opcion:
            case "1":
                personaje.atacar(enemigo)
            case "2":
                defensa = personaje.defender() # Se guarda aquí el return de la función
            case "3":
                personaje.habilidad_especial(enemigo)
            case "4": # Hace otro match-case para elegir la poción
                if cantidad_pociones > 0:
                    print("1- Vida\n2- Daño\n3- Escudo")
                    elegir_pocion = input("¿Qué poción deseas tomar? ")
                    match elegir_pocion: 
                        case "1":
                            pocion_vida.tomar_pocion(personaje)
                        case "2":
                            pocion_daño.tomar_pocion(personaje)
                        case "3":
                            pocion_escudo.tomar_pocion(personaje, enemigo)
                        case _:
                            print("No tienes esa poción")
                            continue
                    cantidad_pociones -= 1 # Resta una poción
                    print(f"Pociones restantes: {cantidad_pociones}")
                else:
                    print("No quedan pociones disponibles.")
                    continue
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

# Prueba de combate completo
def iniciar_juego():
    enemigos = [Orco(), Arpia(), Oscar()]
    while True:
        print("1- Guerrero\n2- Mago\n3- Ladrón")
        opcion = input("¿Qué personaje elegirás? ")
        nombre = input("¿Qué nombre le pondrás? ")
        match opcion:
            case "1":
                personaje = Guerrero(nombre)
                break
            case "2":
                personaje = Mago(nombre)
                break
            case "3":
                personaje = Ladron(nombre)
                break
            case _:
                print("Ese personaje no está disponible.")

    for enemigo in enemigos:
        gana = combate(personaje, enemigo)
        if not gana:
            print("\nGAME OVER.")
            return # ?

    print("\n¡Has derrotado a todos los enemigos! ¡Victoria!")

if __name__ == "__main__":
    iniciar_juego()
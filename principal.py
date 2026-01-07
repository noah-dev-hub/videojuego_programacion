# Archivo principal del videojuego
# =========================
# 1) IMPORTS
# =========================

from guerrero import Guerrero
from mago import Mago
from ladron import Ladron

from orco import Orco
from arpia import Arpia
from oscar import Oscar

from pocion import Vida, Daño, Escudo

# =========================
# 2) COMBATE
# =========================
# Esta función representa 1 combate completo:
# - Recibe un personaje (jugador) y un enemigo.
# - Devuelve True si el jugador gana y False si pierde.

def combate(personaje, enemigo) -> bool:
    # Cada tipo de poción es ahora un objeto distinto que hereda de 'Pocion'
    pocion_vida = Vida()
    pocion_daño = Daño()
    pocion_escudo = Escudo()
    cantidad_pociones = 3 # Variable para que las pociones no sean infinitas. Al estar generadas en esta parte del programa, se rellenan al inicio de cada combate.
    contador_habilidad_enemigo = 0 # Sirve para conseguir que la habilidad del enemigo solo actúe una vez
    vida_inicial_enemigo = enemigo.vida  # Guardamos la vida inicial del enemigo para activar su habilidad especial al 50% de su vida inicial

    # Mensajes de inicio del combate
    print(f"\n¡{personaje.nombre} se enfrenta a {enemigo.nombre}!")
    print(f"Vida {enemigo.nombre}: {enemigo.vida}")
    print(f"Vida {personaje.nombre}: {personaje.vida}")
    
    # =========================
    # 2.1) BUCLE DE TURNOS
    # =========================
    # Mientras los dos estén vivos, se repiten turnos:
    
    while personaje.esta_vivo() and enemigo.esta_vivo():
        defensa = False  # Resetea la variable defensa a False en cada turno con tal de que no se esté defendiendo para siempre
        # =========================
        # 2.2) MENÚ DEL JUGADOR
        # =========================
        print("---------------------------")
        print("1- Atacar")
        print("2- Defender")
        print("3- Habilidad especial")
        print("4- Tomar poción")
        print("---------------------------")
        
        opcion = input(f"\n¿Qué va a hacer {personaje.nombre}? ")
        
        # =========================
        # 2.3) ACCIÓN DEL JUGADOR
        # =========================
        
        match opcion:
            case "1":
                personaje.atacar(enemigo)
            case "2":
                # Se defiende: devuelve True y se guarda en la variable defensa
                # para usarla luego cuando el enemigo ataque.
                defensa = personaje.defender() # Se guarda aquí el return de la función
            case "3":
                personaje.habilidad_especial(enemigo)
            case "4": # Hace otro match-case para elegir la poción
                # =========================
                # 2.4) SUBMENÚ DE POCIONES
                # =========================
                if cantidad_pociones > 0:
                    print("1- Vida\n2- Daño\n3- Escudo")
                    elegir_pocion = input("¿Qué poción deseas tomar? ")
                    match elegir_pocion: 
                        case "1":
                            pocion_vida.tomar_pocion(personaje)
                        case "2":
                            pocion_daño.tomar_pocion(personaje)
                        case "3":
                            pocion_escudo.tomar_pocion(personaje)
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
        if enemigo.vida <= (vida_inicial_enemigo // 2) and contador_habilidad_enemigo == 0:
            enemigo.habilidad_especial()
            contador_habilidad_enemigo = 1

        # Turno del enemigo
        enemigo.atacar(personaje, defensa) # Es aquí donde se manda la variable 'defensa' para que cumpla su función final
        print(f"{personaje.nombre}: {personaje.vida}") # Ésta igual que con el enemigo
    
    # Si se sale del while, es porque uno de los dos ha muerto.
    # Devuelve True si el personaje sigue vivo, False si no.
    return personaje.esta_vivo()

# =========================
# 3) SUBIR DE NIVEL
# =========================
# Función para subir de nivel después de cada combate. Amplía vida y sube el daño.
def subir_nivel(personaje, vida_extra: int = 15, daño_extra: int = 10) -> None:
    personaje.nivel += 1
    personaje.vida += vida_extra
    personaje.daño += daño_extra
    print(f"¡{personaje.nombre} ha subido de nivel!")
    print(f"Nivel: {personaje.nivel}, Vida: {personaje.vida}, Daño: {personaje.daño}")

# =========================
# 4) INICIAR JUEGO (menú inicial + secuencia de combates)
# =========================
# Prueba de combate completo
def iniciar_juego():
    # Lista de enemigos en orden
    enemigos = [Orco(), Arpia(), Oscar()]
    # Lista de personajes no utilizables para poder mostrar sus estadísticas antes de elegir uno de ellos.
    personajes_muestra = [Guerrero("Guerrero"), Mago("Mago"), Ladron("Ladrón")]
    for muestra in personajes_muestra:
        print(str(muestra))
    
    while True:
        print("\n1- Guerrero\n2- Mago\n3- Ladrón")
        opcion = input("¿Qué personaje elegirás? ")
        nombre = input("¿Qué nombre le pondrás? ").capitalize()
        match opcion:
            case "1":
                personaje = Guerrero(nombre)
                print(str(personaje))
                break
            case "2":
                personaje = Mago(nombre)
                break
            case "3":
                personaje = Ladron(nombre)
                break
            case _:
                print("Ese personaje no está disponible.")

    print("El personaje ha sido creado.")
                
    # =========================
    # 4.2) SECUENCIA DE COMBATES
    # =========================
    # Se lucha contra cada enemigo. Si pierdes, acaba el juego.
    for enemigo in enemigos:
        gana = combate(personaje, enemigo)
        if not gana:
            print("\nGAME OVER.")
            return # ?
        else:
            subir_nivel(personaje)
            
    # Si derrotas a todos los enemigos, ganas
    print("\n¡Has derrotado a todos los enemigos! ¡Victoria!")

if __name__ == "__main__":
    iniciar_juego()
    
# Notas:
# - Defensa implementada.
# - Pociones implementadas. Fíjate especialmente en la de escudo a ver si te gusta. Te la he descrito en su clase.
# - Elección de personajes implementada.
# - Subida de nivel implementada.

# HECHO. Podría considerarse que el juego está terminado, aunque hay detalles de los que me gustaría saber tu opinión en cuanto a nivelar el juego:
#   1) El efecto de las pociones, la función de la de escudo y el hecho de que se rellenen en cada combate.
#   2) La función de subida de nivel, en concreto la parte en la que recupera la vida por completo al iniciar cada combate.


# CAMBIOS RECIENTES (2026-01-02)
# - Interfaz Habilidad corregida: ahora los métodos (atacar, defender
#   y habilidad_especial) están definidos tal y como se usan en el juego.
#   Antes la interfaz no coincidía con el código real y podía llevar
#   a confusión al leer o mantener el programa.
#
# - 'Escudo' ahora es armadura que absorbe daño (ver pocion.py + personaje.py).
# - Defensa ahora reduce daño y muestra feedback (ver personaje.py).
# - Habilidad especial del enemigo se activa al 50% de su vida inicial (no valor fijo).
# - Subida de nivel: suma vida/daño (+15/+10 por defecto) sin resetear vida a un máximo fijo.
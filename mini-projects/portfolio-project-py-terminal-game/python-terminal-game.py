# ==============================
# SURVIVE THE FIRST NIGHT
# Portfolio Project Python Terminal Game Codecademy
# ==============================

# Bloque 0
# Función principal que contiene todo el juego
def jugar():

    # Bloque 1
    # Muestra el título y la bienvenida
    print("=== SURVIVE THE FIRST NIGHT ===")
    print()
    print("Bienvenido a esta aventura de terminal inspirada en Minecraft.")

    # Bloque 2
    # Presenta el contexto inicial del juego
    print("\nApareciste en medio de un campo abierto...")
    print("A tu alrededor hay árboles y algunos recursos que podrías usar.")
    print("El sol está bajando lentamente en el horizonte...")
    print("La noche se acerca y, con ella, cosas peligrosas.")
    print("Si no haces nada, puede que no sobrevivas...")

    # Bloque 3
    # Pide el nombre del jugador
    nombre = input("\nIndicá tu gamertag: ")

    # Bloque 4
    # Usa el nombre del jugador en pantalla
    print("\nBuena suerte,", nombre, "...")

    # Bloque 5
    # Primera decisión del jugador (qué hacer primero)
    print("\n¿Qué querés hacer primero?")
    print("1) Cortar madera")
    print("2) Explorar la zona")
    print("3) Quedarte quieto")

    # Inicializa la cantidad de madera del jugador
    wood = 0

    # Captura la decisión del jugador
    decision1 = input("Elegí una opción (1, 2 o 3): ")

    # Bloque 6
    # Lógica según la decisión tomada
    if decision1 == "2":
        print("\nDecidiste explorar la zona...")
        print("Después de caminar un poco, encontrás árboles útiles.")
        print("Recolectás madera rápidamente.")
        print("Ahora tenés madera para construir algo antes de que anochezca.")
        wood = 3

    elif decision1 == "1":
        print("\nDecidiste cortar madera directamente.")
        print("Recolectás algunos recursos básicos.")
        wood = 5

    elif decision1 == "3":
        print("\nTe quedaste quieto...")
        print("Perdiste tiempo valioso.")
        wood = 0

    else:
        print("\nOpción inválida.")

    # Bloque 7
    # Decide qué puede hacer el jugador según la madera obtenida
    if wood >= 5:
        print("\nTenés suficiente madera para construir un refugio.")
        print("Construís un refugio básico antes de que caiga la noche.")

    elif wood >= 3:
        print("\nTenés algo de madera, pero no alcanza para un refugio completo.")
        print("Usás la madera para fabricar una espada de madera.")

    else:
        print("\nNo tenés suficiente madera para construir ni fabricar algo útil.")
        print("Necesitás seguir explorando si querés sobrevivir.")

    # Bloque 8
    # Evento final: llega la noche y se determina el resultado
    print("\nLa noche finalmente cae sobre el mundo...")
    print("Se escuchan ruidos en la oscuridad...")

    if wood >= 5:
        print("Entrás en tu refugio y esperás hasta el amanecer.")
        print("¡Sobreviviste a tu primera noche!")

    elif wood >= 3:
        print("Sostenés tu espada de madera y te defendés durante la noche.")
        print("Con esfuerzo, lográs sobrevivir hasta el amanecer.")

    else:
        print("No tenés refugio ni herramientas para defenderte.")
        print("Las criaturas de la noche te encuentran...")
        print("No sobreviviste la primera noche.")


# ==============================
# Bloque 9
# Loop principal del juego (replay)
# ==============================

while True:
    jugar()  # Ejecuta el juego

    # Pregunta si quiere volver a jugar
    respuesta = input("\n¿Querés volver a jugar? (si/no): ")

    # Si la respuesta no es "si", termina el juego
    if respuesta.lower() != "si":
        print("Gracias por jugar!")
        break
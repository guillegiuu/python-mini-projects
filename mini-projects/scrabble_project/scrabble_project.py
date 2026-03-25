# ==========================================
# PROYECTO: SCRABBLE
# Módulo: Python Dictionaries
# ==========================================

# Diccionario base:
# cada número representa una puntuación
# y la lista contiene las letras que valen eso
letters = [
    "AEILNORSTU",   # 1 punto
    "DG",           # 2 puntos
    "BCMP",         # 3 puntos
    "FHVWY",        # 4 puntos
    "K",            # 5 puntos
    "JX",           # 8 puntos
    "QZ"            # 10 puntos
]

points = [1, 2, 3, 4, 5, 8, 10]

# ------------------------------------------
# 1) Crear el diccionario letra -> puntos
# ------------------------------------------
# Acá vamos a guardar algo como:
# {"A": 1, "B": 3, "C": 3, ...}
letter_to_points = {}

# Recorremos ambas listas al mismo tiempo:
# "letters" tiene grupos de letras
# "points" tiene el puntaje correspondiente
for i in range(len(points)):
    # Guardamos el grupo de letras actual
    group = letters[i]

    # Guardamos el puntaje actual
    point_value = points[i]

    # Recorremos cada letra dentro del grupo
    for letter in group:
        # Asignamos esa letra a su puntaje
        letter_to_points[letter] = point_value

# En Scrabble el espacio también puede existir en algunas palabras/frases
# Le damos valor 0 para evitar errores
letter_to_points[" "] = 0

# Mostrar el diccionario de letras y puntos
print("Diccionario de letras y puntos:")
print(letter_to_points)
print()


# ------------------------------------------
# 2) Palabras de ejemplo con su posible score
# ------------------------------------------
# Este diccionario se suele usar en el proyecto
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Acá vamos a guardar:
# palabra -> puntaje
word_to_points = {}


# ------------------------------------------
# 3) Función para calcular el puntaje
#    de una palabra
# ------------------------------------------
def score_word(word):
    # Arrancamos el puntaje total en 0
    point_total = 0

    # Recorremos cada letra de la palabra
    for letter in word:
        # Sumamos el valor de la letra
        # .get(letter, 0) evita errores si algo no existe
        point_total += letter_to_points.get(letter, 0)

    # Devolvemos el puntaje final
    return point_total


# ------------------------------------------
# 4) Calcular el puntaje de cada palabra
# ------------------------------------------
# Recorremos cada jugador y su lista de palabras
for player, words in player_to_words.items():
    # Recorremos cada palabra de ese jugador
    for word in words:
        # Guardamos en el diccionario
        # la palabra como clave
        # y su score como valor
        word_to_points[word] = score_word(word)

print("Puntaje de cada palabra:")
print(word_to_points)
print()


# ------------------------------------------
# 5) Función para calcular el puntaje total
#    de un jugador
# ------------------------------------------
def score_player(player_words):
    # Empezamos en 0
    player_points = 0

    # Recorremos la lista de palabras del jugador
    for word in player_words:
        # Sumamos el puntaje de esa palabra
        player_points += score_word(word)

    # Devolvemos el total
    return player_points


# ------------------------------------------
# 6) Crear un diccionario jugador -> puntaje
# ------------------------------------------
player_to_points = {}

# Recorremos el diccionario de jugadores
for player, words in player_to_words.items():
    # Calculamos el total del jugador
    player_to_points[player] = score_player(words)

print("Puntaje total de cada jugador:")
print(player_to_points)
print()


# ------------------------------------------
# 7) Buscar al jugador ganador
# ------------------------------------------
# Empezamos suponiendo que nadie ganó todavía
winner = ""
high_score = 0

# Recorremos cada jugador con su puntaje
for player, points_total in player_to_points.items():
    # Si encontramos un puntaje mayor, actualizamos
    if points_total > high_score:
        high_score = points_total
        winner = player

print("Resultado final:")
print("El jugador ganador es:", winner)
print("Con un puntaje total de:", high_score)
print()


# ------------------------------------------
# 8) Pruebas extra
# ------------------------------------------
# Probamos la función score_word()
print("Prueba de score_word():")
print("La palabra BLUE vale:", score_word("BLUE"))
print("La palabra EARTH vale:", score_word("EARTH"))
print("La palabra ZAP vale:", score_word("ZAP"))

# ==========================================
# 📤 OUTPUT ESPERADO (ejemplo)
# ==========================================

# Diccionario de letras y puntos:
# {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
#  'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
#  'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#  'K': 5,
#  'J': 8, 'X': 8,
#  'Q': 10, 'Z': 10,
#  ' ': 0}

# Puntaje de cada palabra:
# {'BLUE': 6, 'TENNIS': 6, 'EXIT': 11,
#  'EARTH': 8, 'EYES': 7, 'MACHINE': 14,
#  'ERASER': 6, 'BELLY': 10, 'HUSKY': 15,
#  'ZAP': 14, 'COMA': 8, 'PERIOD': 9}

# Puntaje total de cada jugador:
# {'player1': 23, 'wordNerd': 29, 'Lexi Con': 31, 'Prof Reader': 31}

# Resultado final:
# El jugador ganador es: Lexi Con
# Con un puntaje total de: 31

# Prueba de score_word():
# La palabra BLUE vale: 6
# La palabra EARTH vale: 8
# La palabra ZAP vale: 14
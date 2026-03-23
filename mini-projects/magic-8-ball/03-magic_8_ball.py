# ============================================
# Proyecto: Magic 8 Ball
# Tema: Variables, strings, control flow (if/elif/else),
#       números aleatorios (random), validaciones y output
# ============================================

import random

# 1. Variables principales
name = "Guille"
question = "¿Voy a terminar Codecademy?"
answer = ""

# 2. Número aleatorio (1 a 12)
random_number = random.randint(1, 12)

# 3. Respuestas posibles (control flow)
if random_number == 1:
    answer = "Sí, definitivamente"
elif random_number == 2:
    answer = "Es muy probable"
elif random_number == 3:
    answer = "Sin dudas"
elif random_number == 4:
    answer = "Respuesta poco clara, intenta de nuevo"
elif random_number == 5:
    answer = "Preguntá más tarde"
elif random_number == 6:
    answer = "Mejor no decirte ahora"
elif random_number == 7:
    answer = "Mis fuentes dicen que no"
elif random_number == 8:
    answer = "No pinta bien"
elif random_number == 9:
    answer = "Muy dudoso"
elif random_number == 10:
    answer = "Los astros no están alineados"
elif random_number == 11:
    answer = "Preguntate a vos mismo, ya sabés la respuesta"
elif random_number == 12:
    answer = "La suerte se revelará pronto"
else:
    answer = "Error"

# ============================================
# 4. Validaciones
# ============================================

# ❌ Si no hay pregunta
if question == "":
    print("Te olvidaste de hacer una pregunta!")

# ✅ Si hay pregunta
else:
    # Si hay nombre
    if name != "":
        print(f"{name} pregunta: {question}")
    else:
        print(f"Pregunta: {question}")

    # Mostramos la respuesta final
    print(f"Respuesta de la bola mágica: {answer}")

# ============================================
# Ejemplo de output (puede variar)
# ============================================

# Guille pregunta: ¿Voy a terminar Codecademy?
# Respuesta de la bola mágica: Sí, definitivamente

# Nota:
# La respuesta es aleatoria, por lo que cambia en cada ejecución.
# =======================
# Proyecto: Magic 8-Ball 🎱
# Temas : variables, strings, control flow (if/elif/else), random numbers (random.randint), validación de inputs y console output


# Simula una bola mágica que responde preguntas de forma aleatoria


# 📌 1. Importamos el módulo random
# Esto nos permite generar números aleatorios
import random


# 📌 2. Variables principales

# Nombre de la persona que hace la pregunta
name = "Guille"

# Pregunta que queremos hacerle a la bola mágica
question = "Will I finish Codecademy?"

# Variable donde se va a guardar la respuesta final
answer = ""


# 📌 3. Generamos un número aleatorio entre 1 y 12
# Este número decide qué respuesta va a salir
random_number = random.randint(1, 12)


# 📌 4. Control Flow (if / elif / else)
# Dependiendo del número, asignamos una respuesta distinta

if random_number == 1:
    answer = "Yes - definitely"

elif random_number == 2:
    answer = "It is decidedly so"

elif random_number == 3:
    answer = "Without a doubt"

elif random_number == 4:
    answer = "Reply hazy, try again"

elif random_number == 5:
    answer = "Ask again later"

elif random_number == 6:
    answer = "Better not tell you now"

elif random_number == 7:
    answer = "My sources say no"

elif random_number == 8:
    answer = "Outlook not so good"

elif random_number == 9:
    answer = "Very doubtful"

elif random_number == 10:
    answer = "The stars are not aligned yet"

elif random_number == 11:
    answer = "Ask yourself, you already know the answer"

elif random_number == 12:
    answer = "Luck will reveal itself soon"

else:
    # Esto es por seguridad (no debería pasar nunca)
    answer = "Error"


# ============================================
# 📌 5. Validaciones (muy importante)
# ============================================

# ❌ Si no hay pregunta
if question == "":
    print("⚠️ You forgot to ask a question!")

# ✅ Si hay pregunta
else:

    # 📌 Si hay nombre → mostramos quién pregunta
    if name != "":
        print(name + " asks: " + question)

    # 📌 Si no hay nombre
    else:
        print("Question: " + question)

    # 📌 Mostramos la respuesta final
    print("Magic 8-Ball's answer: " + answer)

# Posibles respuestas incluyen:
# - Yes - definitely
# - Ask again later
# - Outlook not so good
# - Very doubtful
    
# =========================================
# Ejemplo de output (resultado aleatorio)
# =========================================
#
# Guille asks: Will I finish Codecademy?
# Magic 8-Ball's answer: Yes - definitely
#
# Nota:
# La respuesta es aleatoria, por lo que puede variar en cada ejecución.

# =========================================
# Proyecto: Manhattan Zoo
# Este script lee el archivo meal-regimens.txt
# y muestra la información en consola.
# =========================================

# Abrimos el archivo en modo lectura
with open("meal-regimens.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Título en consola
print("=== MANHATTAN ZOO - MEAL REGIMENS ===\n")

# Mostramos el contenido
print(content)
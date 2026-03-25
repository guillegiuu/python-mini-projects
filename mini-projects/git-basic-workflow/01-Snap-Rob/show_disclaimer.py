# =========================================
# Proyecto: SnapFit Robots, Inc.
# Este script lee el archivo disclaimer.txt
# y muestra su contenido en consola.
# =========================================

# Abrimos el archivo en modo lectura
with open("disclaimer.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Mostramos un título en consola
print("=== SNAPFIT ROBOTS DISCLAIMER ===\n")

# Mostramos el contenido del archivo
print(content)
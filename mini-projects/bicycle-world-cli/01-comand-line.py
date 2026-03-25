# ======================================================
# 🖥️ PROYECTO: BICYCLE WORLD - COMMAND LINE
# ======================================================
# Este archivo es un resumen práctico de los comandos
# usados en la terminal (bash).
# NO es un programa funcional, sino una guía explicada.
# ======================================================


# ------------------------------------------------------
# 📍 1. pwd → mostrar ubicación actual
# ------------------------------------------------------

# Comando:
# pwd

# Explicación:
# Muestra la ruta donde estás parado en el sistema.

# Ejemplo:
# /home/ccuser/workspace/bicycle-world-ii


# ------------------------------------------------------
# 📂 2. ls → listar archivos y carpetas
# ------------------------------------------------------

# Comando:
# ls

# Explicación:
# Muestra todo lo que hay dentro del directorio actual.

# Ejemplo:
# brands.txt  freight  mountain  racing


# ------------------------------------------------------
# 📁 3. cd → moverse entre carpetas
# ------------------------------------------------------

# Comando:
# cd freight

# Explicación:
# Entra a la carpeta "freight".

# Ejemplo:
# Ahora estás dentro de freight/


# ------------------------------------------------------
# 🔙 4. cd .. → subir un nivel
# ------------------------------------------------------

# Comando:
# cd ..

# Explicación:
# Te mueve a la carpeta anterior (nivel superior).


# ------------------------------------------------------
# ⬆️ 5. cd ../.. → subir dos niveles
# ------------------------------------------------------

# Comando:
# cd ../..

# Explicación:
# Sube dos carpetas hacia arriba.


# ------------------------------------------------------
# 📄 6. touch → crear archivos
# ------------------------------------------------------

# Comando:
# touch dirt.txt

# Explicación:
# Crea un archivo vacío llamado "dirt.txt".


# ------------------------------------------------------
# 📁 7. mkdir → crear carpetas
# ------------------------------------------------------

# Comando:
# mkdir bmx

# Explicación:
# Crea una carpeta llamada "bmx".


# ------------------------------------------------------
# 📄 8. crear archivo dentro de otra carpeta
# ------------------------------------------------------

# Comando:
# touch bmx/tricks.txt

# Explicación:
# Crea un archivo dentro de la carpeta bmx sin entrar en ella.


# ------------------------------------------------------
# 🧠 IDEA CLAVE
# ------------------------------------------------------

# mkdir → crea carpetas
# touch → crea archivos

# El nombre no define el tipo, el comando sí.


# ------------------------------------------------------
# 🧪 EJEMPLO DE OUTPUT (simulado)
# ------------------------------------------------------

print("📍 Directorio actual:")
print("/home/ccuser/workspace/bicycle-world-ii")

print("\n📂 Contenido:")
print("brands.txt  freight  mountain  racing")

print("\n📁 Dentro de freight:")
print("messenger  porteur")

print("\n📁 Dentro de mountain/downhill:")
print("heavyweight  lightweight")

print("\n📄 Archivos creados:")
print("dirt.txt  mud.txt")

print("\n📁 Carpeta creada:")
print("bmx/")

print("\n📄 Archivo dentro de bmx:")
print("tricks.txt")

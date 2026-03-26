# Proyecto: Hacking The Fender
# Descripción: Este script simula un ataque a un sistema de seguridad
# Temas : Files, CSV, JSON, ASCII Art, os.replace()

# Importamos los módulos necesarios
import csv
import json
import os

# Lista donde vamos a guardar los usuarios comprometidos
compromised_users = []

# ----------------------------------------
# PARTE 1: Leer el archivo passwords.csv
# ----------------------------------------

# Abrimos el archivo CSV en modo lectura
with open('passwords.csv', newline='', encoding='utf-8') as password_file:
    # DictReader convierte cada fila en un diccionario
    password_csv = csv.DictReader(password_file)

    # Recorremos cada fila del archivo
    for password_row in password_csv:
        # Algunas veces la columna puede llamarse "Username"
        # y otras veces "username", así que chequeamos ambas opciones
        if 'username' in password_row:
            compromised_users.append(password_row['username'])
        elif 'Username' in password_row:
            compromised_users.append(password_row['Username'])

# ----------------------------------------
# PARTE 2: Guardar usuarios comprometidos
# ----------------------------------------

# Creamos un archivo .txt para guardar los usernames
with open('compromised_users.txt', 'w', encoding='utf-8') as compromised_user_file:
    # Recorremos la lista de usuarios comprometidos
    for compromised_user in compromised_users:
        # Escribimos cada usuario en una línea nueva
        compromised_user_file.write(compromised_user + '\n')

# ----------------------------------------
# PARTE 3: Crear mensaje para el jefe
# ----------------------------------------

# Abrimos un archivo JSON en modo escritura
with open('boss_message.json', 'w', encoding='utf-8') as boss_message:
    # Creamos un diccionario con el mensaje
    boss_message_dict = {
        "recipient": "The Boss",
        "message": "Mission Success"
    }

    # Guardamos el diccionario en formato JSON dentro del archivo
    json.dump(boss_message_dict, boss_message)

# ----------------------------------------
# PARTE 4: Crear la firma de Slash Null
# ----------------------------------------

# Guardamos la firma ASCII en una cadena multilínea
slash_null_sig = """
 _  _     ___   __    ___  _  _  
( \/ )   / __) / _\\  / __)( )/ ) 
 \\  / _ ( (__ /    \\( (__  )  (  
  \\/ (_) \\___)\\_/\\_/ \\___)(_ )_) 
   _  _     __   __    __ _  __   
  / )( \\   / _\\ (  )  (  ( \\(  )  
  \\ /\\ /  /    \\/ (_/\\ /    / )(__ 
  (_/\\_)  \\_/\\_/\\____/\\_)__)(____)
"""

# ----------------------------------------
# PARTE 5: Crear un nuevo archivo CSV
# ----------------------------------------

# Creamos un archivo nuevo donde vamos a escribir la firma
with open('new_passwords.csv', 'w', encoding='utf-8') as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)

# ----------------------------------------
# PARTE 6: Reemplazar el archivo original
# ----------------------------------------

# Reemplazamos passwords.csv por new_passwords.csv
# Lo hacemos dentro de un try por si ocurre algún error
try:
    os.replace('new_passwords.csv', 'passwords.csv')
except Exception as e:
    print(f"Error al reemplazar el archivo: {e}")

# ----------------------------------------
# EJEMPLO DE OUTPUT
# ----------------------------------------

# Archivo: compromised_users.txt
# ------------------------------
# jean49
# haydenashley
# michaelastephens
# denisephillips


# Archivo: boss_message.json
# --------------------------
# {
#   "recipient": "The Boss",
#   "message": "Mission Success"
# }


# Archivo: new_passwords.csv
# --------------------------
# (contiene la firma ASCII de Slash Null)

# Luego de ejecutar:
# passwords.csv es reemplazado por new_passwords.csv

# ⚠️ IMPORTANTE:
# Si ejecutás el script nuevamente sin restaurar el passwords.csv original,
# se producirá un error porque ya no será un CSV válido.
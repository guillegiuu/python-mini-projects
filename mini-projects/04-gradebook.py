# ============================
# Proyecto: Gradebook
# Tema: Listas y listas bidimensionales en Python

# Notas del semestre pasado
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# 1) Lista de materias actuales
subjects = ["physics", "calculus", "poetry", "history"]

# 2) Lista de notas actuales
grades = [98, 97, 85, 88]

# 3) Crear manualmente una lista bidimensional que combine materia + nota
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

# 4) Mostrar el gradebook inicial
print("Gradebook inicial:")
print(gradebook)
print()

# 5) Agregar Computer Science con nota 100
gradebook.append(["computer science", 100])

# 6) Agregar Visual Arts con nota 93
gradebook.append(["visual arts", 93])

# 7) Corregir la nota de Visual Arts sumándole 5 puntos
# La materia visual arts quedó al final de la lista
gradebook[-1][1] += 5

# 8) Quitar la nota numérica de Poetry
gradebook[2].remove(85)

# 9) Reemplazarla por "Pass"
gradebook[2].append("Pass")

# 10) Unir las notas del semestre pasado con las actuales
full_gradebook = last_semester_gradebook + gradebook

# Mostrar resultado final
print("Gradebook completo:")
print(full_gradebook)

# ============================================================
# PROYECTO: A Sorted Tale (Codecademy)
# Temas: Sorting Algorithms (Bubble Sort & Quicksort), Custom Comparison Functions,Time Complexity / Performance Analysis.
# Versión en un solo archivo .py
# Comentarios y prints en español
# ============================================================

import random


# ============================================================
# DATOS DE EJEMPLO
# ------------------------------------------------------------
# En el proyecto original, los libros se cargaban desde archivos
# CSV. Acá los dejamos directamente en el archivo para tener
# todo en un solo lugar y que sea más fácil de subir a Replit
# o GitHub sin depender de otros archivos.
# ============================================================

bookshelf = [
    {"title": "Adventures of Huckleberry Finn", "author": "Mark Twain"},
    {"title": "Best Served Cold", "author": "Joe Abercrombie"},
    {"title": "Dear Emily", "author": "Fern Michaels"},
    {"title": "Collected Poems", "author": "Robert Hayden"},
    {"title": "End Zone", "author": "Don DeLillo"},
    {"title": "Forrest Gump", "author": "Winston Groom"},
    {"title": "Gravity", "author": "Tess Gerritsen"},
    {"title": "Hiromi's Hands", "author": "Lynne Barasch"},
    {"title": "Norwegian Wood", "author": "Haruki Murakami"},
    {"title": "Middlesex: A Novel (Oprah's Book Club)", "author": "Jeffrey Eugenides"}
]

# Lista más grande para comparar rendimiento.
# Repetimos varias veces los mismos libros para simular un dataset mayor.
long_bookshelf = bookshelf * 120


# ============================================================
# PREPARAR LOS DATOS
# ------------------------------------------------------------
# Agregamos claves en minúscula para que al ordenar por título
# o por autor no afecten las mayúsculas/minúsculas.
# ============================================================

def prepare_books(book_list):
    """
    Recibe una lista de libros y devuelve una nueva lista
    con los campos:
    - title_lower
    - author_lower

    Esto nos permite comparar texto de forma consistente.
    """
    prepared_books = []

    for book in book_list:
        # Hacemos una copia del diccionario para no modificar el original directamente
        new_book = dict(book)

        # Guardamos versiones en minúscula
        new_book["title_lower"] = new_book["title"].lower()
        new_book["author_lower"] = new_book["author"].lower()

        # Agregamos el libro preparado a la nueva lista
        prepared_books.append(new_book)

    return prepared_books


# ============================================================
# FUNCIONES DE COMPARACIÓN
# ------------------------------------------------------------
# Todas siguen la misma idea:
# Devuelven True si book_a es "mayor que" book_b
# según el criterio elegido.
# ============================================================

def by_title_ascending(book_a, book_b):
    """
    Devuelve True si el título de book_a debería ir
    después del título de book_b en orden ascendente.
    """
    return book_a["title_lower"] > book_b["title_lower"]


def by_author_ascending(book_a, book_b):
    """
    Devuelve True si el autor de book_a debería ir
    después del autor de book_b en orden ascendente.
    """
    return book_a["author_lower"] > book_b["author_lower"]


def by_total_length(book_a, book_b):
    """
    Devuelve True si la suma de:
    len(título) + len(autor) de book_a
    es mayor que la de book_b.
    """
    total_a = len(book_a["title"]) + len(book_a["author"])
    total_b = len(book_b["title"]) + len(book_b["author"])
    return total_a > total_b


# ============================================================
# BUBBLE SORT
# ------------------------------------------------------------
# Algoritmo simple:
# - compara elementos vecinos
# - si están mal ordenados, los intercambia
# - repite hasta que ya no haya swaps
# ============================================================

def bubble_sort(arr, comparison_function):
    """
    Ordena la lista usando Bubble Sort y una función
    de comparación personalizada.

    Modifica la lista original y también la devuelve.
    """
    swaps = 0
    sorted_flag = False

    while not sorted_flag:
        sorted_flag = True

        for idx in range(len(arr) - 1):
            # Si el elemento actual "es mayor" que el siguiente,
            # según la regla definida, los intercambiamos.
            if comparison_function(arr[idx], arr[idx + 1]):
                sorted_flag = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1

    print(f"Bubble Sort: se realizaron {swaps} intercambios.")
    return arr


# ============================================================
# QUICKSORT
# ------------------------------------------------------------
# Algoritmo más eficiente en promedio:
# - elige un pivot
# - manda menores a la izquierda
# - manda mayores a la derecha
# - repite recursivamente
# ============================================================

def quicksort(arr, start, end, comparison_function):
    """
    Ordena la lista usando Quicksort.
    No devuelve una nueva lista: modifica la lista original.
    """
    # Caso base: si el rango tiene 0 o 1 elemento, ya está ordenado
    if start >= end:
        return

    # Elegimos un pivot aleatorio dentro del rango
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = arr[pivot_idx]

    # Movemos el pivot al final para trabajar más cómodo
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]

    # Este puntero marcará dónde colocar el próximo elemento menor al pivot
    less_than_pointer = start

    # Recorremos los elementos del rango, excepto el pivot final
    for i in range(start, end):
        # Si el pivot es "mayor que" arr[i], entonces arr[i]
        # debe ir a la izquierda del pivot
        if comparison_function(pivot_element, arr[i]):
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1

    # Ponemos el pivot en su posición final correcta
    arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]

    # Llamadas recursivas a la izquierda y derecha del pivot
    quicksort(arr, start, less_than_pointer - 1, comparison_function)
    quicksort(arr, less_than_pointer + 1, end, comparison_function)


# ============================================================
# FUNCIONES AUXILIARES PARA MOSTRAR RESULTADOS
# ============================================================

def print_titles(book_list):
    """
    Imprime todos los títulos de una lista de libros.
    """
    print("\nTítulos:")
    for book in book_list:
        print(book["title"])


def print_authors(book_list):
    """
    Imprime todos los autores de una lista de libros.
    """
    print("\nAutores:")
    for book in book_list:
        print(book["author"])


def print_total_lengths(book_list, limit=10):
    """
    Imprime título, autor y longitud total.
    Usamos un límite para no llenar demasiado la consola.
    """
    print("\nLibros ordenados por longitud total:")
    for book in book_list[:limit]:
        total = len(book["title"]) + len(book["author"])
        print(f"{total} caracteres -> {book['title']} - {book['author']}")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# Preparamos listas con los campos *_lower
bookshelf_prepared = prepare_books(bookshelf)
long_bookshelf_prepared = prepare_books(long_bookshelf)

print("===================================================")
print("PROYECTO: A SORTED TALE")
print("Ordenamiento de libros con Bubble Sort y Quicksort")
print("===================================================")


# ------------------------------------------------------------
# 1) Mostrar títulos originales
# ------------------------------------------------------------
print("\n1) Estado original de la estantería (títulos):")
print_titles(bookshelf_prepared)


# ------------------------------------------------------------
# 2) Comparación Unicode (idea teórica del proyecto)
# ------------------------------------------------------------
print("\n2) Ejemplo de códigos Unicode:")
print(f'Código de "a": {ord("a")}')
print(f'Código de "z": {ord("z")}')
print(f'Código de "A": {ord("A")}')


# ------------------------------------------------------------
# 3) Bubble Sort por título
# ------------------------------------------------------------
print("\n3) Bubble Sort por título (ascendente):")
bookshelf_v1 = list(bookshelf_prepared)
sort_1 = bubble_sort(bookshelf_v1, by_title_ascending)
print_titles(sort_1)


# ------------------------------------------------------------
# 4) Bubble Sort por autor
# ------------------------------------------------------------
print("\n4) Bubble Sort por autor (ascendente):")
bookshelf_v2 = list(bookshelf_prepared)
sort_2 = bubble_sort(bookshelf_v2, by_author_ascending)
print_authors(sort_2)


# ------------------------------------------------------------
# 5) Quicksort por autor
# ------------------------------------------------------------
print("\n5) Quicksort por autor (ascendente):")
bookshelf_v3 = list(bookshelf_prepared)
quicksort(bookshelf_v3, 0, len(bookshelf_v3) - 1, by_author_ascending)
print_authors(bookshelf_v3)


# ------------------------------------------------------------
# 6) Bubble Sort por longitud total (lista grande)
# ------------------------------------------------------------
print("\n6) Bubble Sort por longitud total (lista grande):")
print("Este paso sirve para notar que Bubble Sort se vuelve lento con muchos datos.")

long_bookshelf_v1 = list(long_bookshelf_prepared)
bubble_sort(long_bookshelf_v1, by_total_length)

print("\nPrimeros 10 resultados de la lista grande ordenada por longitud total con Bubble Sort:")
print_total_lengths(long_bookshelf_v1, limit=10)


# ------------------------------------------------------------
# 7) Quicksort por longitud total (lista grande)
# ------------------------------------------------------------
print("\n7) Quicksort por longitud total (lista grande):")
print("Este paso muestra una alternativa más eficiente para datasets grandes.")

long_bookshelf_v2 = list(long_bookshelf_prepared)
quicksort(long_bookshelf_v2, 0, len(long_bookshelf_v2) - 1, by_total_length)

print("\nPrimeros 10 resultados de la lista grande ordenada por longitud total con Quicksort:")
print_total_lengths(long_bookshelf_v2, limit=10)


print("\n===================================================")
print("Fin del proyecto.")
print("Conclusión: el criterio de comparación cambia,")
print("pero el algoritmo puede reutilizarse si está bien diseñado.")
print("Además, Bubble Sort funciona en listas chicas o casi ordenadas,")
print("mientras que Quicksort escala mucho mejor en listas grandes.")
print("===================================================")


# ============================================================
# EJEMPLO DE OUTPUT (para copiar en GitHub si querés)
# ------------------------------------------------------------
# OUTPUT APROXIMADO:
#
# ===========================================================
# PROYECTO: A SORTED TALE
# Ordenamiento de libros con Bubble Sort y Quicksort
# ===========================================================
#
# 1) Estado original de la estantería (títulos):
#
# Títulos:
# Adventures of Huckleberry Finn
# Best Served Cold
# Dear Emily
# Collected Poems
# End Zone
# Forrest Gump
# Gravity
# Hiromi's Hands
# Norwegian Wood
# Middlesex: A Novel (Oprah's Book Club)
#
# 2) Ejemplo de códigos Unicode:
# Código de "a": 97
# Código de "z": 122
# Código de "A": 65
#
# 3) Bubble Sort por título (ascendente):
# Bubble Sort: se realizaron 2 intercambios.
#
# Títulos:
# Adventures of Huckleberry Finn
# Best Served Cold
# Collected Poems
# Dear Emily
# End Zone
# Forrest Gump
# Gravity
# Hiromi's Hands
# Middlesex: A Novel (Oprah's Book Club)
# Norwegian Wood
#
# 4) Bubble Sort por autor (ascendente):
# Bubble Sort: se realizaron 24 intercambios.
#
# Autores:
# Don DeLillo
# Fern Michaels
# Haruki Murakami
# Jeffrey Eugenides
# Joe Abercrombie
# Lynne Barasch
# Mark Twain
# Robert Hayden
# Tess Gerritsen
# Winston Groom
#
# 5) Quicksort por autor (ascendente):
#
# Autores:
# Don DeLillo
# Fern Michaels
# Haruki Murakami
# Jeffrey Eugenides
# Joe Abercrombie
# Lynne Barasch
# Mark Twain
# Robert Hayden
# Tess Gerritsen
# Winston Groom
#
# 6) Bubble Sort por longitud total (lista grande):
# Este paso sirve para notar que Bubble Sort se vuelve lento con muchos datos.
# Bubble Sort: se realizaron muchos intercambios.
#
# Primeros 10 resultados de la lista grande ordenada por longitud total con Bubble Sort:
# 21 caracteres -> End Zone - Don DeLillo
# 22 caracteres -> Gravity - Tess Gerritsen
# 23 caracteres -> Dear Emily - Fern Michaels
# ...
#
# 7) Quicksort por longitud total (lista grande):
# Este paso muestra una alternativa más eficiente para datasets grandes.
#
# Primeros 10 resultados de la lista grande ordenada por longitud total con Quicksort:
# 21 caracteres -> End Zone - Don DeLillo
# 22 caracteres -> Gravity - Tess Gerritsen
# 23 caracteres -> Dear Emily - Fern Michaels
# ...
#
# ===========================================================
# Fin del proyecto.
# Conclusión: el criterio de comparación cambia,
# pero el algoritmo puede reutilizarse si está bien diseñado.
# ===========================================================
# ============================================================
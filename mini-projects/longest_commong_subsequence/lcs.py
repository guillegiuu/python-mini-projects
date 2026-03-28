# ============================================================
# PROYECTO: Longest Common Subsequence (LCS)
# TEMA: Dynamic Programming (Programación Dinámica)
# ============================================================

# ------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------------
def longest_common_subsequence(string_1, string_2):
    """
    Calcula la longitud de la subsecuencia común más larga
    entre dos strings usando programación dinámica.
    """

    # Mensaje de inicio para saber qué strings estamos comparando
    print("Buscando la subsecuencia común más larga entre:")
    print("string_1 =", string_1)
    print("string_2 =", string_2)
    print()

    # --------------------------------------------------------
    # PASO 1: Crear la grilla llena de ceros
    # --------------------------------------------------------
    # +1 porque agregamos una fila y columna extra para el caso base
    # (string vacía / sin caracteres)
    grid = [[0 for _ in range(len(string_1) + 1)]
            for _ in range(len(string_2) + 1)]

    # --------------------------------------------------------
    # PASO 2: Recorrer la grilla
    # --------------------------------------------------------
    # row representa las filas -> string_2
    # col representa las columnas -> string_1
    for row in range(1, len(string_2) + 1):
        for col in range(1, len(string_1) + 1):

            # Letra actual de cada string
            letra_string_2 = string_2[row - 1]
            letra_string_1 = string_1[col - 1]

            # ------------------------------------------------
            # CASO 1: Las letras coinciden
            # ------------------------------------------------
            if letra_string_1 == letra_string_2:
                # Tomamos la diagonal y sumamos 1
                grid[row][col] = grid[row - 1][col - 1] + 1

            # ------------------------------------------------
            # CASO 2: Las letras NO coinciden
            # ------------------------------------------------
            else:
                # Elegimos el mayor entre arriba e izquierda
                grid[row][col] = max(
                    grid[row - 1][col],   # arriba
                    grid[row][col - 1]    # izquierda
                )

    # --------------------------------------------------------
    # PASO 3: Mostrar la grilla final
    # --------------------------------------------------------
    print("Grilla final de Programación Dinámica:")
    for fila in grid:
        print(fila)

    print()

    # --------------------------------------------------------
    # PASO 4: Resultado final
    # --------------------------------------------------------
    resultado = grid[-1][-1]

    print("La longitud de la subsecuencia común más larga es:", resultado)

    return resultado


# ------------------------------------------------------------
# PRUEBA DEL PROYECTO
# ------------------------------------------------------------
dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

resultado_final = longest_common_subsequence(dna_1, dna_2)

# -----------------------------
# EJEMPLO DE OUTPUT
# -----------------------------
# Buscando la subsecuencia común más larga entre:
# string_1 = ABCDEF
# string_2 = AECDF

# Grilla final de programación dinámica:
# [0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 2, 2, 2]
# [0, 1, 1, 1, 2, 2, 2]
# [0, 1, 2, 2, 2, 2, 2]
# [0, 1, 2, 2, 2, 2, 3]

# La longitud de la subsecuencia común más larga es: 3

# ------------------------------------------------------------
# NOTA FINAL
# ------------------------------------------------------------
# Este proyecto devuelve la LONGITUD del LCS.
# No reconstruye las letras exactas de la subsecuencia.
# Eso sería una mejora extra más avanzada.
# ------------------------------------------------------------

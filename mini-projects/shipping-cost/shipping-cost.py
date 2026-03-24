# ============================================
# Proyecto: Sal's Shipping
# Tema: Control Flow, Variables, Conditional Logic


# Este programa calcula el costo de envío de un paquete
# usando tres métodos:
# 1) Envío terrestre normal
# 2) Envío terrestre premium
# 3) Envío con dron
# Después compara los tres costos y muestra cuál es el más barato.


# Peso del paquete en libras
# Podés cambiar este valor para probar otros casos
weight = 4.8


# ---------------------------
# Envío terrestre normal
# ---------------------------

# Si el paquete pesa 2 lb o menos
if weight <= 2:
    cost_ground = weight * 1.50 + 20

# Si pesa más de 2 lb y hasta 6 lb
elif weight <= 6:
    cost_ground = weight * 3.00 + 20

# Si pesa más de 6 lb y hasta 10 lb
elif weight <= 10:
    cost_ground = weight * 4.00 + 20

# Si pesa más de 10 lb
else:
    cost_ground = weight * 4.75 + 20

# Mostramos el costo del envío terrestre normal
print("El costo del envío terrestre es de: $", cost_ground)


# ---------------------------
# Envío terrestre premium
# ---------------------------

# Este envío tiene un precio fijo, no importa el peso
cost_ground_premium = 125.00

# Mostramos el costo del envío terrestre premium
print("El costo del envío terrestre premium es de: $", cost_ground_premium)


# ---------------------------
# Envío con dron
# ---------------------------

# Si el paquete pesa 2 lb o menos
if weight <= 2:
    cost_drone = weight * 4.50

# Si pesa más de 2 lb y hasta 6 lb
elif weight <= 6:
    cost_drone = weight * 9.00

# Si pesa más de 6 lb y hasta 10 lb
elif weight <= 10:
    cost_drone = weight * 12.00

# Si pesa más de 10 lb
else:
    cost_drone = weight * 14.25

# Mostramos el costo del envío con dron
print("El costo del envío con dron es de: $", cost_drone)


# ---------------------------
# Comparar cuál es el más barato
# ---------------------------

# Verificamos si el envío terrestre normal es el más barato
if cost_ground < cost_ground_premium and cost_ground < cost_drone:
    cheapest_method = "Envío terrestre"
    cheapest_cost = cost_ground

# Verificamos si el envío terrestre premium es el más barato
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
    cheapest_method = "Envío terrestre premium"
    cheapest_cost = cost_ground_premium

# Si no se cumplieron las condiciones anteriores,
# entonces el más barato es el envío con dron
else:
    cheapest_method = "Envío con dron"
    cheapest_cost = cost_drone


# Mostramos el método más barato
print()
print("El método de envío más barato es:", cheapest_method)
print("Su costo total es de: $", cheapest_cost)

# ---------------------------
# Ejemplo de output
# ---------------------------

"""
Ejemplo usando:
weight = 4.8

Salida esperada en consola:

El costo del envío terrestre es de: $ 34.4
El costo del envío terrestre premium es de: $ 125.0
El costo del envío con dron es de: $ 43.199999999999996

El método de envío más barato es: Envío terrestre
Su costo total es de: $ 34.4
"""
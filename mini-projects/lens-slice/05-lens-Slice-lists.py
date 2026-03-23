# ============================================
# Proyecto: Len's Slice
# Tema: Listas, listas bidimensionales, sort, pop, insert y slicing


# --------------------------------------------
# 1) Lista con los toppings (ingredientes)
# --------------------------------------------
toppings = [
    "pepperoni",
    "pineapple",
    "cheese",
    "sausage",
    "olives",
    "anchovies",
    "mushrooms"
]

# --------------------------------------------
# 2) Lista con los precios de cada topping
#    Cada posición coincide con la lista toppings
# --------------------------------------------
prices = [2, 6, 1, 3, 2, 7, 2]

# --------------------------------------------
# 3) Contar cuántas pizzas cuestan 2 dólares
# --------------------------------------------
num_two_dollar_slices = prices.count(2)

print("Cantidad de slices de $2:", num_two_dollar_slices)

# --------------------------------------------
# 4) Guardar cuántos tipos de pizza vendemos
# --------------------------------------------
num_pizzas = len(toppings)

# --------------------------------------------
# 5) Mostrar ese dato en pantalla
# --------------------------------------------
print("Vendemos " + str(num_pizzas) + " tipos diferentes de pizza!")

# ============================================
# LISTA BIDIMENSIONAL
# Cada sublista tiene esta forma:
# [precio, nombre_del_topping]
# ============================================

pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

print("\nLista original:")
print(pizza_and_prices)

# --------------------------------------------
# 6) Ordenar la lista por precio de menor a mayor
#    sort() ordena por el primer valor de cada sublista
# --------------------------------------------
pizza_and_prices.sort()

print("\nLista ordenada por precio:")
print(pizza_and_prices)

# --------------------------------------------
# 7) Guardar la pizza más barata
#    Está en la primera posición luego del sort
# --------------------------------------------
cheapest_pizza = pizza_and_prices[0]

# --------------------------------------------
# 8) Guardar la pizza más cara
#    Está en la última posición luego del sort
# --------------------------------------------
priciest_pizza = pizza_and_prices[-1]

print("\nPizza más barata:")
print(cheapest_pizza)

print("\nPizza más cara:")
print(priciest_pizza)

# --------------------------------------------
# 9) Eliminar la pizza más cara
#    pop() sin índice elimina el último elemento
# --------------------------------------------
pizza_and_prices.pop()

print("\nLista después de eliminar la pizza más cara:")
print(pizza_and_prices)

# --------------------------------------------
# 10) Agregar una nueva pizza: peppers
#     Tiene precio 2.5
#     Se inserta en una posición que mantenga el orden
# --------------------------------------------
pizza_and_prices.insert(3, [2.5, "peppers"])

print("\nLista después de agregar peppers:")
print(pizza_and_prices)

# --------------------------------------------
# 11) Obtener las 3 pizzas más baratas
#     slicing: desde el índice 0 hasta el 2
# --------------------------------------------
three_cheapest = pizza_and_prices[:3]

print("\nLas 3 pizzas más baratas son:")
print(three_cheapest)

# =========================================
# Ejemplo de output esperado
# =========================================
#
# Cantidad de slices de $2: 3
# Vendemos 7 tipos diferentes de pizza!
#
# Lista original:
# [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
#
# Lista ordenada por precio:
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]
#
# Pizza más barata:
# [1, 'cheese']
#
# Pizza más cara:
# [7, 'anchovies']
#
# Las 3 pizzas más baratas son:
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives']]

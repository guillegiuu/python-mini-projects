# =========================
# Proyecto: Carly's Clippers
# Tema: Loops, listas y manipulación de datos


# Lista de cortes de pelo disponibles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Lista de precios correspondientes a cada corte
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Cantidad de veces que se realizó cada corte la semana pasada
last_week = [2, 3, 5, 8, 4, 4, 6, 2]


# =========================
# 1. PRECIO PROMEDIO
# =========================

# Variable acumuladora para sumar todos los precios
total_price = 0

# Recorremos la lista de precios
for price in prices:
    total_price += price  # sumamos cada precio al total

# Calculamos el promedio dividiendo por la cantidad de elementos
average_price = total_price / len(prices)

# Mostramos el resultado
print("Average Haircut Price:", average_price)


# =========================
# 2. NUEVOS PRECIOS (-5)
# =========================

# Creamos una nueva lista restando 5 a cada precio (list comprehension)
new_prices = [price - 5 for price in prices]

# Mostramos los nuevos precios
print("New Prices:", new_prices)


# =========================
# 3. RECAUDACIÓN TOTAL
# =========================

# Variable acumuladora para la recaudación total
total_revenue = 0

# Recorremos las listas usando índices
for i in range(len(hairstyles)):
    # Multiplicamos precio * cantidad vendida y lo sumamos al total
    total_revenue += prices[i] * last_week[i]

# Mostramos la recaudación total
print("Total Revenue:", total_revenue)


# =========================
# 4. PROMEDIO DIARIO
# =========================

# Calculamos el ingreso promedio por día (7 días)
average_daily_revenue = total_revenue / 7

# Mostramos el resultado
print("Average Daily Revenue:", average_daily_revenue)


# =========================
# 5. CORTES MENORES A $30
# =========================

# Creamos una lista con los cortes cuyo precio nuevo es menor a 30
cuts_under_30 = [
    hairstyles[i]                # agregamos el nombre del corte
    for i in range(len(new_prices))  # recorremos los índices
    if new_prices[i] < 30            # condición: precio menor a 30
]

# Mostramos los cortes filtrados
print("Cuts under $30:", cuts_under_30)

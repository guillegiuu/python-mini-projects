# =======================================================
# Proyecto: Getting Ready for Physics Class
# Tema: funciones en Python aplicadas a formulas de fisica

# Datos dados por el proyecto
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Convierte Fahrenheit a Celsius
def f_to_c(f_temp):
    return (f_temp - 32) * 5 / 9


# Probamos la funcion con 100 F
f100_in_celsius = f_to_c(100)
print(f"100 grados Fahrenheit son {f100_in_celsius} grados Celsius.")


# Convierte Celsius a Fahrenheit
def c_to_f(c_temp):
    return c_temp * (9 / 5) + 32


# Probamos la funcion con 0 C
c0_in_fahrenheit = c_to_f(0)
print(f"0 grados Celsius son {c0_in_fahrenheit} grados Fahrenheit.")


# Calcula la fuerza
def get_force(mass, acceleration):
    return mass * acceleration


# Fuerza del tren
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Mostramos el resultado en una frase
print(f"The GE train supplies {train_force} Newtons of force.")


# Calcula la energia
# c tiene un valor por defecto: velocidad de la luz
def get_energy(mass, c=3 * 10**8):
    return mass * c**2


# Energia de una bomba de 1 kg
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")


# Calcula el trabajo
# Trabajo = fuerza * distancia
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance


# Trabajo realizado por el tren
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")

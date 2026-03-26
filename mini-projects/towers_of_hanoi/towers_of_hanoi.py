# ==========================================
# PROYECTO: TOWERS OF HANOI

# Temas: Clases y objetos, Node, Stack, LIFO, Linked List simple, Métodos de clase, Bucles while, Condicionales if / elif / else, Validación de inputs, Lógica de juego en consola.
# ==========================================

# -----------------------------
# CLASE NODE
# -----------------------------
# Representa un nodo de una linked list.
# Cada nodo guarda:
# - un valor
# - una referencia al siguiente nodo

class Node:
    def __init__(self, value, next_node=None):
        # Valor que guarda el nodo
        self.value = value

        # Referencia al siguiente nodo
        self.next_node = next_node

    def get_value(self):
        # Devuelve el valor del nodo
        return self.value

    def get_next_node(self):
        # Devuelve el siguiente nodo
        return self.next_node

    def set_next_node(self, next_node):
        # Cambia la referencia al siguiente nodo
        self.next_node = next_node


# -----------------------------
# CLASE STACK
# -----------------------------
# Representa una pila (LIFO: Last In, First Out)
# El último elemento en entrar es el primero en salir.

class Stack:
    def __init__(self, name):
        # Cantidad actual de elementos
        self.size = 0

        # Nodo que está arriba de todo
        self.top_item = None

        # Límite máximo de elementos
        self.limit = 1000

        # Nombre de la pila
        self.name = name

    def push(self, value):
        # Agrega un elemento arriba de la pila
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No hay más espacio en la pila.")

    def pop(self):
        # Saca y devuelve el elemento de arriba
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Esta pila está vacía.")
            return None

    def peek(self):
        # Devuelve el valor de arriba sin eliminarlo
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            return None

    def has_space(self):
        # Verifica si todavía hay espacio
        return self.size < self.limit

    def is_empty(self):
        # Verifica si la pila está vacía
        return self.size == 0

    def get_size(self):
        # Devuelve el tamaño actual de la pila
        return self.size

    def get_name(self):
        # Devuelve el nombre de la pila
        return self.name

    def print_items(self):
        # Recorre la pila y arma una lista con sus elementos
        pointer = self.top_item
        print_list = []

        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()

        # Damos vuelta la lista para mostrarla desde la base hasta la cima
        print_list.reverse()
        print(f"{self.name}: {print_list}")


# -----------------------------
# FUNCIÓN AUXILIAR:
# ELEGIR UNA PILA
# -----------------------------
# Muestra las opciones disponibles y devuelve
# la pila elegida por el usuario.

def get_input(stacks):
    choices = [stack.get_name()[0].upper() for stack in stacks]

    while True:
        print("\nElegí una torre:")
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Ingresá {letter} para {name}")

        user_input = input("> ").upper()

        for i in range(len(choices)):
            if user_input == choices[i]:
                return stacks[i]

        print("Opción inválida. Probá de nuevo.")


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------

print("\n¡Vamos a jugar Towers of Hanoi!")

# Creamos las 3 pilas / torres
left_stack = Stack("Izquierda")
middle_stack = Stack("Medio")
right_stack = Stack("Derecha")

# Guardamos las torres en una lista para trabajarlas más fácil
stacks = [left_stack, middle_stack, right_stack]

# Pedimos cuántos discos quiere usar el usuario
while True:
    try:
        num_disks = int(input("\n¿Con cuántos discos querés jugar? "))
        if num_disks >= 3:
            break
        else:
            print("Ingresá un número mayor o igual a 3.")
    except ValueError:
        print("Por favor, ingresá un número válido.")

# Cargamos los discos en la torre izquierda
# Van del más grande al más chico
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

# Calculamos la cantidad mínima de movimientos:
# fórmula = 2^n - 1
num_optimal_moves = (2 ** num_disks) - 1

print(f"\nLa cantidad mínima de movimientos para resolverlo es: {num_optimal_moves}")

# Contador de movimientos del usuario
num_user_moves = 0

# El juego termina cuando todos los discos estén en la torre derecha
while right_stack.get_size() != num_disks:
    print("\n--- Estado actual de las torres ---")
    for stack in stacks:
        stack.print_items()

    print("\n¿Desde qué torre querés mover?")
    from_stack = get_input(stacks)

    print("\n¿Hacia qué torre querés mover?")
    to_stack = get_input(stacks)

    # Caso 1: la torre de origen está vacía
    if from_stack.is_empty():
        print("Movimiento inválido. Esa torre está vacía.")

    # Caso 2: la torre destino está vacía
    elif to_stack.is_empty():
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1

    # Caso 3: el disco de arriba del origen es más chico que el del destino
    elif from_stack.peek() < to_stack.peek():
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1

    # Caso 4: intentó poner un disco grande sobre uno más chico
    else:
        print("Movimiento inválido. No podés poner un disco grande sobre uno más chico.")

# Mensaje final
print("\n¡Felicitaciones! Resolviste el juego.")
print(f"Lo resolviste en {num_user_moves} movimientos.")
print(f"La cantidad mínima posible era {num_optimal_moves} movimientos.")

# =======================================

# Ejemplo de Output

# ¡Vamos a jugar Towers of Hanoi!

# ¿Con cuántos discos querés jugar? 3

# La cantidad mínima de movimientos para resolverlo es: 7

# --- Estado actual de las torres ---
# Izquierda: [3, 2, 1]
# Medio: []
# Derecha: []

# ¿Desde qué torre querés mover?

# Elegí una torre:
# Ingresá I para Izquierda
# Ingresá M para Medio
# Ingresá D para Derecha
# > I

# ¿Hacia qué torre querés mover?

# Elegí una torre:
# Ingresá I para Izquierda
# Ingresá M para Medio
# Ingresá D para Derecha
# > D

# --- Estado actual de las torres ---
# Izquierda: [3, 2]
# Medio: []
# Derecha: [1]

# ¿Desde qué torre querés mover?

# Elegí una torre:
# Ingresá I para Izquierda
# Ingresá M para Medio
# Ingresá D para Derecha
# > I

# ¿Hacia qué torre querés mover?

# Elegí una torre:
# Ingresá I para Izquierda
# Ingresá M para Medio
# Ingresá D para Derecha
# > M

# --- Estado actual de las torres ---
# Izquierda: [3]
# Medio: [2]
# Derecha: [1]

# ...

# ¡Felicitaciones! Resolviste el juego.
# Lo resolviste en 7 movimientos.
# La cantidad mínima posible era 7 movimientos.
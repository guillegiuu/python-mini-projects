# ==============================
# PROYECTO BLOSSOM - HASH MAPS
# Temas: Hashing | Compresión | Colisiones | Separate Chaining | HashMap
# ==============================


# ------------------------------
# CLASE NODE
# Representa un nodo de la LinkedList
# ------------------------------
class Node:
    def __init__(self, value, next_node=None):
        # valor que guarda el nodo
        self.value = value
        # referencia al siguiente nodo
        self.next_node = next_node


# ------------------------------
# CLASE LINKED LIST
# Se usa para manejar colisiones
# en el HashMap (separate chaining)
# ------------------------------
class LinkedList:
    def __init__(self):
        # al principio la lista está vacía
        self.head_node = None

    def insert(self, new_node):
        # insertamos al principio de la lista
        new_node.next_node = self.head_node
        self.head_node = new_node

    def __iter__(self):
        # esto permite recorrer la lista con un for
        current_node = self.head_node

        while current_node is not None:
            # devolvemos el valor del nodo actual
            yield current_node.value
            # avanzamos al siguiente nodo
            current_node = current_node.next_node

    def __str__(self):
        # esto es solo para mostrar la lista de forma linda
        values = []
        current_node = self.head_node

        while current_node is not None:
            values.append(str(current_node.value))
            current_node = current_node.next_node

        return " -> ".join(values)


# ------------------------------
# CLASE HASH MAP
# Guarda pares key-value
# usando un array de LinkedLists
# ------------------------------
class HashMap:
    def __init__(self, size):
        # tamaño del array interno
        self.array_size = size

        # cada posición del array tendrá una LinkedList vacía
        self.array = [LinkedList() for _ in range(size)]

    def hash(self, key):
        # convierte la key (texto) en un número
        return sum(key.encode())

    def compress(self, hash_code):
        # reduce el hash a un índice válido del array
        return hash_code % self.array_size

    def assign(self, key, value):
        # obtenemos el número hash de la key
        hash_code = self.hash(key)

        # obtenemos el índice del array
        array_index = self.compress(hash_code)

        # obtenemos la LinkedList en ese índice
        list_at_array = self.array[array_index]

        # recorremos la lista para ver si la key ya existe
        for item in list_at_array:
            if item[0] == key:
                # si existe, actualizamos el valor
                item[1] = value
                return

        # si no existe, creamos un nodo nuevo y lo insertamos
        payload = Node([key, value])
        list_at_array.insert(payload)

    def retrieve(self, key):
        # obtenemos el número hash de la key
        hash_code = self.hash(key)

        # obtenemos el índice del array
        array_index = self.compress(hash_code)

        # obtenemos la LinkedList en ese índice
        list_at_index = self.array[array_index]

        # recorremos la lista buscando la key
        for item in list_at_index:
            if item[0] == key:
                return item[1]

        # si no la encontramos, devolvemos None
        return None

    def mostrar_tabla(self):
        # muestra cómo quedó armado el hash map por dentro
        print("\n--- Estado interno del HashMap ---")
        for index in range(self.array_size):
            print(f"Índice {index}: {self.array[index]}")


# ------------------------------
# DATOS DEL PROYECTO BLOSSOM
# Lista de flores y sus significados
# ------------------------------
flower_definitions = [
    ["rose", "amor"],
    ["lily", "pureza"],
    ["tulip", "confianza"],
    ["daisy", "inocencia"],
    ["orchid", "belleza"],
    ["sunflower", "felicidad"],
    ["violet", "modestia"],
    ["jasmine", "dulzura"]
]


# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------

# creamos el hash map con el tamaño de la lista de flores
blossom = HashMap(len(flower_definitions))

print("Cargando flores en el HashMap...\n")

# cargamos cada flor en el hash map
for flower in flower_definitions:
    key = flower[0]
    value = flower[1]
    blossom.assign(key, value)
    print(f"Se agregó: {key} -> {value}")

# probamos búsquedas
print("\n==============================")
print("PRUEBAS DE BÚSQUEDA")
print("==============================")

print("Significado de 'daisy':", blossom.retrieve("daisy"))
print("Significado de 'rose':", blossom.retrieve("rose"))
print("Significado de 'orchid':", blossom.retrieve("orchid"))

# probamos una flor que no existe
print("\nBuscando una flor que no existe...")
print("Significado de 'lavender':", blossom.retrieve("lavender"))

# agregamos una flor nueva
print("\nAgregando una nueva flor personalizada...")
blossom.assign("lavender", "calma")
print("Significado de 'lavender':", blossom.retrieve("lavender"))

# actualizamos una flor existente
print("\nActualizando el valor de una flor existente...")
blossom.assign("rose", "amor profundo")
print("Nuevo significado de 'rose':", blossom.retrieve("rose"))

# mostramos la estructura interna para entender colisiones
blossom.mostrar_tabla()

# ==== Ejemplo de Output:

# Cargando flores en el HashMap...

# Se agregó: rose -> amor
# Se agregó: lily -> pureza
# Se agregó: tulip -> confianza
# Se agregó: daisy -> inocencia
# Se agregó: orchid -> belleza
# Se agregó: sunflower -> felicidad
# Se agregó: violet -> modestia
# Se agregó: jasmine -> dulzura

# ==============================
# PRUEBAS DE BÚSQUEDA
# ==============================
# Significado de 'daisy': inocencia
# Significado de 'rose': amor
# Significado de 'orchid': belleza

# Buscando una flor que no existe...
# Significado de 'lavender': None

# Agregando una nueva flor personalizada...
# Significado de 'lavender': calma

# Actualizando el valor de una flor existente...
# Nuevo significado de 'rose': amor profundo
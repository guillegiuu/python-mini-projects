# =========================================================
# Proyecto: The Boredless Tourist
# =========================================================

# Lista de destinos disponibles
destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt"
]

# Viajero de prueba:
# [nombre, destino, intereses]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# =========================================================
# Función: get_destination_index()
# Busca el índice de un destino dentro de la lista destinations
# =========================================================
def get_destination_index(destination):
    # Guardamos la posición del destino dentro de la lista
    destination_index = destinations.index(destination)

    # Devolvemos esa posición
    return destination_index


# =========================================================
# Función: get_traveler_location()
# Obtiene el destino del viajero y devuelve su índice
# =========================================================
def get_traveler_location(traveler):
    # El destino del viajero está en la posición 1
    traveler_destination = traveler[1]

    # Buscamos el índice de ese destino en la lista destinations
    traveler_destination_index = get_destination_index(traveler_destination)

    # Devolvemos el índice encontrado
    return traveler_destination_index


# Probamos la función con el viajero de prueba
test_destination_index = get_traveler_location(test_traveler)

# Mostramos el índice del destino del viajero
print("Índice del destino del viajero de prueba:")
print(test_destination_index)


# =========================================================
# Lista de atracciones
# Cada sublista representa las atracciones de un destino
# =========================================================
attractions = [[], [], [], [], []]


# =========================================================
# Función: add_attraction()
# Agrega una atracción al destino correcto
# =========================================================
def add_attraction(destination, attraction):
    # Buscamos el índice del destino
    destination_index = get_destination_index(destination)

    # Accedemos a la sublista de atracciones de ese destino
    attractions_for_destination = attractions[destination_index]

    # Agregamos la nueva atracción a esa sublista
    attractions_for_destination.append(attraction)

    # Finalizamos la función
    return


# =========================================================
# Cargamos atracciones para cada destino
# Cada atracción tiene esta estructura:
# [nombre_de_la_atraccion, [lista_de_tags]]
# =========================================================
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])

add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])

add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])

add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])

add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# =========================================================
# Función: find_attractions()
# Busca atracciones en una ciudad según intereses del viajero
# =========================================================
def find_attractions(destination, interests):
    # Obtenemos el índice del destino
    destination_index = get_destination_index(destination)

    # Obtenemos las atracciones de esa ciudad
    attractions_in_city = attractions[destination_index]

    # Creamos una lista vacía para guardar coincidencias
    attractions_with_interest = []

    # Recorremos cada atracción posible de la ciudad
    for possible_attraction in attractions_in_city:
        # Los tags de la atracción están en la posición 1
        attraction_tags = possible_attraction[1]

        # Recorremos cada interés del viajero
        for interest in interests:
            # Si el interés aparece dentro de los tags de la atracción
            if interest in attraction_tags:
                # Agregamos solo el nombre de la atracción
                attractions_with_interest.append(possible_attraction[0])

    # Devolvemos la lista de atracciones encontradas
    return attractions_with_interest


# Probamos la función find_attractions()
la_arts = find_attractions("Los Angeles, USA", ["art"])

# Mostramos el resultado de la prueba
print("\nAtracciones de arte en Los Angeles:")
print(la_arts)


# =========================================================
# Función: get_attractions_for_traveler()
# Genera un mensaje personalizado para el viajero
# =========================================================
def get_attractions_for_traveler(traveler):
    # Guardamos el destino del viajero
    traveler_destination = traveler[1]

    # Guardamos los intereses del viajero
    traveler_interests = traveler[2]

    # Buscamos las atracciones que coincidan con sus intereses
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    # Empezamos a construir el mensaje final
    interests_string = "Hola "

    # Agregamos el nombre del viajero
    interests_string = interests_string + traveler[0]

    # Agregamos texto descriptivo
    interests_string = interests_string + ", creemos que te van a gustar estos lugares cerca de "

    # Agregamos el destino del viajero
    interests_string = interests_string + traveler_destination

    # Recorremos las atracciones encontradas
    for attraction in traveler_attractions:
        # Agregamos cada atracción al mensaje
        interests_string = interests_string + ": " + attraction

    # Devolvemos el mensaje completo
    return interests_string


# =========================================================
# Prueba final del proyecto
# =========================================================
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

# Mostramos el mensaje final
print("\nMensaje final para el viajero:")
print(smills_france)


# =========================================================
# Ejemplo de output esperado
# =========================================================
# Índice del destino del viajero de prueba:
# 1
#
# Atracciones de arte en Los Angeles:
# ['LACMA']
#
# Mensaje final para el viajero:
# Hola Dereck Smill, creemos que te van a gustar estos lugares cerca de Paris, France: Arc de Triomphe
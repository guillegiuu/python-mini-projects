"""
============================================================
PROYECTO: SkyRoute - Sistema de Rutas con Grafos
TEMA: BFS (Breadth-First Search) y DFS (Depth-First Search)
============================================================
"""

# Importamos BFS y DFS desde otro archivo
from graph_search import bfs, dfs

# Importamos el grafo del metro
from vc_metro import vc_metro

# Importamos landmark -> estaciones cercanas
from vc_landmarks import vc_landmarks

# Importamos letra -> landmark
from landmark_choices import landmark_choices


# ==========================================
# Armamos un string con la lista de landmarks
# ==========================================
landmark_string = ""

for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}\n".format(letter, landmark)


# Lista de estaciones cerradas por mantenimiento
stations_under_construction = []


# =====================
# Funcion de bienvenida
# =====================
def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)


# ==========================================
# Pedir origen y validarlo
# ==========================================
def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")

    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_start()


# ==========================================
# Pedir destino y validarlo
# ==========================================
def get_end():
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")

    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_end()


# ======================================================
# Elegir origen y destino o cambiarlos si ya existian
# ======================================================
def set_start_and_end(start_point, end_point):

    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

        if change_point == "b":
            start_point = get_start()
            end_point = get_end()

        elif change_point == "o":
            start_point = get_start()

        elif change_point == "d":
            end_point = get_end()

        else:
            print("Oops, that isn't 'o', 'd', or 'b'...")
            return set_start_and_end(start_point, end_point)

    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point


# =====================================================
# Crear una version actualizada del grafo del metro
# quitando conexiones de estaciones en mantenimiento
# =====================================================
def get_active_stations():
    updated_metro = vc_metro

    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():

            # Si la estacion actual NO esta en mantenimiento,
            # le quitamos de sus vecinos las estaciones cerradas
            if current_station != station_under_construction:
                updated_metro[current_station] = neighboring_stations - set(stations_under_construction)

            # Si la estacion actual SI esta en mantenimiento,
            # la dejamos sin conexiones
            else:
                updated_metro[current_station] = set([])

    return updated_metro


# =====================================================
# Buscar la mejor ruta entre dos landmarks
# =====================================================
def get_route(start_point, end_point):

    # Convertimos landmarks en estaciones cercanas
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]

    # Guardamos todas las rutas posibles
    routes = []

    # Probamos todas las combinaciones
    for start_station in start_stations:
        for end_station in end_stations:

            # Si hay estaciones cerradas, usamos el grafo actualizado
            # si no, usamos el normal
            metro_system = get_active_stations() if stations_under_construction else vc_metro

            # Si hay estaciones cerradas, primero verificamos con DFS
            # si existe algun camino posible
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)

                # Si no existe camino, pasamos a la siguiente combinacion
                if not possible_route:
                    continue

            # Buscamos la ruta mas corta con BFS
            route = bfs(metro_system, start_station, end_station)

            # Si existe la agregamos a la lista
            if route:
                routes.append(route)

    # Si encontramos al menos una ruta, devolvemos la mas corta
    if routes:
        shortest_route = min(routes, key=len)
        return shortest_route


# ==========================================
# Mostrar landmarks otra vez si el usuario quiere
# ==========================================
def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == "y":
        print(landmark_string)


# =========
# Despedida
# =========
def goodbye():
    print("Thanks for using SkyRoute!")


# =====================================================
# Funcion principal para pedir nueva ruta
# =====================================================
def new_route(start_point=None, end_point=None):

    # Elegimos origen y destino
    start_point, end_point = set_start_and_end(start_point, end_point)

    # BONUS 1:
    # Si origen y destino son iguales, avisamos y salimos
    if start_point == end_point:
        print("You are already at your destination!")
        return

    # Buscamos la mejor ruta
    shortest_route = get_route(start_point, end_point)

    # Si existe ruta, la mostramos
    if shortest_route:
        shortest_route_string = "\n".join(shortest_route)

        print(
            "The shortest metro route from {0} to {1} is:\n{2}".format(
                start_point, end_point, shortest_route_string
            )
        )

    # Si no existe ruta, avisamos
    else:
        print(
            "Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(
                start_point, end_point
            )
        )

    # Preguntamos si quiere otra ruta
    again = input("Would you like to see another route? Enter y/n: ")

    if again == "y":
        show_landmarks()
        new_route(start_point, end_point)


# ==========================
# Funcion principal del programa
# ==========================
def skyroute():
    greet()
    new_route()
    goodbye()


# Ejecutamos el programa
skyroute()

# 🚇 SkyRoute (Graphs)

🟡 Nivel: Medio  

---

## 📖 Descripción

SkyRoute es un proyecto enfocado en la implementación de **grafos (Graphs)** para construir un sistema de rutas entre estaciones de metro.

El objetivo principal es encontrar caminos entre distintos puntos utilizando algoritmos de búsqueda como:

- **BFS (Breadth-First Search)** → encuentra el camino más corto  
- **DFS (Depth-First Search)** → explora caminos posibles  

Este proyecto simula cómo un sistema real de transporte podría calcular rutas entre estaciones.


⬅️ [Proyecto anterior](../Wilderness_Escape_Trees/README.md)

🏠 [Volver al menú de proyectos](https://github.com/guillegiuu/python-mini-projects/blob/main/README.md)


---

## 🧠 Conceptos utilizados

- Grafos (Graphs)
- Nodos (Stations)
- Conexiones (Edges)
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Diccionarios en Python
- Listas
- Lógica condicional

---

## 🧩 Idea teórica clave

Un grafo representa conexiones entre elementos:

A --- B --- C

||

D --- E

En este proyecto:

- Cada nodo = una estación  
- Cada conexión = una ruta posible  
- El objetivo = encontrar un camino entre dos estaciones  

---

## ⚔️ BFS vs DFS (clave de entrevista)

- **BFS**  
  - Recorre nivel por nivel  
  - Encuentra el camino más corto  
  - Usa cola (Queue)  
  - Complejidad: O(V + E)

- **DFS**  
  - Va profundo primero  
  - No garantiza camino más corto  
  - Usa recursión o stack  
  - Complejidad: O(V + E)

---

## 💻 Código

👉 [Ver código](./sky_graph_search.py)

---

## 🧪 Ejemplo de output
```
 =============================
 EJEMPLO DE OUTPUT
 =============================

 Starting point: Vancouver Aquarium
 Destination: Central Station

 Calculating route...

 Ruta encontrada:
 Vancouver Aquarium -> Burrard -> Granville -> Stadium-Chinatown -> Central Station

 (El camino puede variar dependiendo del grafo)

```

---

## 🧠 Qué aprendí

- Cómo representar problemas reales con grafos  
- Diferencia práctica entre BFS y DFS  
- Cómo encontrar rutas en estructuras complejas  
- Cómo usar diccionarios como grafos en Python  
- Cómo pensar en términos de nodos y conexiones



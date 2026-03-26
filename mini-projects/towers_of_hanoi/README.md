# 🗼 Towers of Hanoi

🟡 Nivel: Medio  

---

## 📖 Descripción

**Towers of Hanoi** es un juego clásico implementado en Python utilizando estructuras de datos como pilas (*stacks*) y nodos (*nodes*).

El objetivo es mover todos los discos desde la torre izquierda hasta la torre derecha respetando las reglas del juego:

- Solo se puede mover un disco a la vez  
- Solo se puede tomar el disco superior  
- No se puede colocar un disco grande sobre uno más chico  

Este proyecto permite entender cómo funcionan las estructuras LIFO y cómo se aplican en un caso real.

⬅️ [Proyecto anterior](../portfolio-project-py-terminal-game/README.md)

🏠 [Volver al menú de proyectos](https://github.com/guillegiuu/python-mini-projects/blob/main/README.md)

---

## 💻 Ver código

[Ver código](https://github.com/guillegiuu/python-mini-projects/blob/main/mini-projects/towers_of_hanoi/towers_of_hanoi.py)

---

## 🧪 Ejemplo de output
```
¡Vamos a jugar Towers of Hanoi!

¿Con cuántos discos querés jugar? 3

La cantidad mínima de movimientos para resolverlo es: 7

--- Estado actual de las torres ---
Izquierda: [3, 2, 1]
Medio: []
Derecha: []

Elegí una torre:
Ingresá I para Izquierda
Ingresá M para Medio
Ingresá D para Derecha
> I

Elegí una torre:
> D

--- Estado actual de las torres ---
Izquierda: [3, 2]
Medio: []
Derecha: [1]

Elegí una torre:
> I

Elegí una torre:
> M

--- Estado actual de las torres ---
Izquierda: [3]
Medio: [2]
Derecha: [1]

...

¡Felicitaciones! Resolviste el juego.
Lo resolviste en 7 movimientos.
La cantidad mínima posible era 7 movimientos.
```



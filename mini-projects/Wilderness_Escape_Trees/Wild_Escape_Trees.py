"""
========================================================
PROYECTO: Wilderness Escape (Trees / Árboles en Python)
TEMA: (Trees / Árboles en Python)
========================================================

¿QUÉ HICIMOS EN ESTE PROYECTO?
------------------------------
Armamos una historia interactiva tipo "Choose Your Own Adventure"
(usá 1 o 2 para elegir caminos), utilizando la estructura de datos TREE.

IDEA TEÓRICA CLAVE
------------------
Un árbol está formado por nodos.

En este proyecto:
- Cada nodo representa una parte de la historia.
- Cada nodo guarda:
  1) story_piece -> el texto de ese capítulo
  2) choices -> una lista con los caminos posibles (nodos hijos)

ESTRUCTURA MENTAL
-----------------
story_root
├── choice_a
│   ├── choice_a_1
│   └── choice_a_2
└── choice_b
    ├── choice_b_1
    └── choice_b_2

CONCEPTOS IMPORTANTES
---------------------
1) __init__
   Sirve para inicializar cada objeto cuando se crea.

2) self
   Representa al objeto actual.
   Ejemplo:
   self.story_piece = story_piece
   -> guardamos dentro del objeto el texto recibido.

3) choices = []
   Cada nodo arranca con una lista vacía de hijos.

4) add_child()
   Agrega un nodo hijo a la lista choices.

5) traverse()
   Recorre la historia.
   - Arranca desde el nodo actual
   - Imprime el texto
   - Mientras haya choices:
       * pide input
       * valida que sea "1" o "2"
       * convierte a int
       * resta 1 porque Python indexa desde 0
       * avanza al hijo elegido

¿POR QUÉ USAMOS while?
----------------------
Porque no sabemos cuántos pasos va a dar el usuario.
La historia sigue MIENTRAS haya choices.
Cuando el nodo actual no tiene hijos, la historia termina.

¿POR QUÉ input() SE VALIDA COMO STRING?
---------------------------------------
Porque input() SIEMPRE devuelve texto.
Si el usuario escribe 1, Python guarda "1", no 1.

Por eso validamos:
if choice not in ["1", "2"]:

Después recién convertimos:
chosen_index = int(choice)

¿POR QUÉ RESTAMOS 1?
--------------------
Porque el usuario ve:
1 o 2

Pero las listas en Python usan índices:
0 o 1

Entonces:
1 -> 0
2 -> 1

REGLAS DE ORO DEL PROYECTO
--------------------------
- Cada capítulo = un nodo
- Cada choice = un hijo
- choices guarda los caminos posibles
- while mantiene viva la historia
- input() devuelve string
- int() convierte a número
- restar 1 adapta opción humana a índice Python
- si choices == [], la historia terminó
"""


# ========================================================
# CLASE TREENODE
# ========================================================

class TreeNode:
    def __init__(self, story_piece):
        # Guardamos el texto de este nodo/capítulo
        self.story_piece = story_piece

        # Lista de hijos/caminos posibles
        self.choices = []

    def add_child(self, node):
        # Agregamos un nodo hijo a la lista de choices
        self.choices.append(node)

    def traverse(self):
        """
        Recorre la historia desde el nodo actual.
        Mientras haya choices, pide al usuario una opción
        y avanza al nodo hijo correspondiente.
        """

        # story_node representa en qué parte de la historia estamos
        story_node = self

        # Mostramos el texto inicial
        print(story_node.story_piece)

        # Mientras existan caminos posibles, seguimos
        while story_node.choices != []:
            # Pedimos al usuario que elija 1 o 2
            choice = input("Enter 1 or 2 to continue the story: ")

            # Validamos que el usuario escriba una opción válida
            if choice not in ["1", "2"]:
                print("Enter a valid choice: 1 or 2.")
            else:
                # Convertimos el string a entero
                chosen_index = int(choice)

                # Restamos 1 para adaptarlo al índice de Python
                chosen_index -= 1

                # Elegimos el nodo hijo correcto
                chosen_child = story_node.choices[chosen_index]

                # Mostramos el texto del nodo elegido
                print(chosen_child.story_piece)

                # Avanzamos en la historia
                story_node = chosen_child


# ========================================================
# ARMADO DEL ÁRBOL DE LA HISTORIA
# ========================================================

# Nodo raíz: inicio de la historia
story_root = TreeNode("""
You are in a forest clearing.
There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...
""")

# Dos caminos principales desde la raíz
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers.
The bear follows you and asks
'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared
you.
""")

# Conectamos los dos primeros hijos al nodo raíz
story_root.add_child(choice_a)
story_root.add_child(choice_b)

# --------------------------------------------------------
# Hijos de choice_a
# --------------------------------------------------------

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After
making peace with a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.

YOU REMAIN LOST.
""")

# Conectamos choice_a con sus dos finales
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

# --------------------------------------------------------
# Hijos de choice_b
# --------------------------------------------------------

choice_b_1 = TreeNode("""
The bear is unamused. After
smelling the flowers, it turns
around and leaves you alone.

YOU REMAIN LOST.
""")

choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

# Conectamos choice_b con sus dos finales
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)


# ========================================================
# EJECUCIÓN DEL PROGRAMA
# ========================================================

# Arrancamos la historia desde la raíz
story_root.traverse()


"""
========================================================
EJEMPLO DE OUTPUT
========================================================

You are in a forest clearing.
There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...

Enter 1 or 2 to continue the story: 1

The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'

Enter 1 or 2 to continue the story: 1

The bear returns and tells you it's been a rough week. After
making peace with a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.

--------------------------------------------------------

Otro posible camino:

You are in a forest clearing.
There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...

Enter 1 or 2 to continue the story: 2

You come across a clearing full of flowers.
The bear follows you and asks
'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared
you.

Enter 1 or 2 to continue the story: 2

The bear understands and apologizes for startling you. Your new friend shows you a path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
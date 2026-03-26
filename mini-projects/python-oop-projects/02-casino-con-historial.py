# Proyecto 2: Casino simple con historial
# Temas: Clases, objetos, atributos, métodos

import random


# Clase Jugador
class Jugador:
    def __init__(self, nombre, saldo):
        # Atributos
        self.nombre = nombre
        self.saldo = saldo
        self.historial = []

    def puede_apostar(self, monto):
        # Verifica si el jugador puede apostar
        return monto > 0 and monto <= self.saldo

    def apostar(self, monto):
        # Descuenta el monto del saldo
        if self.puede_apostar(monto):
            self.saldo -= monto
        else:
            print("Saldo insuficiente.")

    def cobrar(self, monto):
        # Suma dinero al saldo
        self.saldo += monto

    def guardar_historial(self, mensaje):
        # Agrega un mensaje al historial
        self.historial.append(mensaje)

    def __repr__(self):
        return f"Jugador(nombre='{self.nombre}', saldo={self.saldo}, historial={self.historial})"


# Clase JuegoCaraOCruz
class JuegoCaraOCruz:
    def __init__(self, nombre="Cara o Cruz", multiplicador_pago=2):
        # Atributos
        self.nombre = nombre
        self.multiplicador_pago = multiplicador_pago
        self.ultimo_resultado = None

    def lanzar(self):
        # Lanza la moneda
        self.ultimo_resultado = random.choice(["cara", "cruz"])
        return self.ultimo_resultado

    def mostrar_info(self):
        # Muestra información del juego
        print(f"Juego: {self.nombre} | Pago: x{self.multiplicador_pago}")

    def jugar(self, jugador, apuesta, eleccion):
        # Interacción entre jugador y juego
        if not jugador.puede_apostar(apuesta):
            print(f"{jugador.nombre} no tiene saldo suficiente para apostar {apuesta}.")
            return

        jugador.apostar(apuesta)
        resultado = self.lanzar()

        print(f"{jugador.nombre} eligió {eleccion}.")
        print(f"La moneda cayó en {resultado}.")

        if eleccion == resultado:
            ganancia = apuesta * self.multiplicador_pago
            jugador.cobrar(ganancia)
            print(f"¡{jugador.nombre} ganó {ganancia}!")
            jugador.guardar_historial(f"Ganó apostando {apuesta} a {eleccion}")
        else:
            print(f"{jugador.nombre} perdió la apuesta.")
            jugador.guardar_historial(f"Perdió apostando {apuesta} a {eleccion}")

    def __repr__(self):
        return f"JuegoCaraOCruz(nombre='{self.nombre}', multiplicador_pago={self.multiplicador_pago}, ultimo_resultado={self.ultimo_resultado})"


# Programa principal
if __name__ == "__main__":
    # Dos jugadores
    jugador1 = Jugador("Guille", 100)
    jugador2 = Jugador("Lucas", 80)

    # Dos juegos
    juego1 = JuegoCaraOCruz()
    juego2 = JuegoCaraOCruz("Cara o Cruz VIP", 3)

    # Mostrar objetos
    print(jugador1)
    print(juego1)

    print("\n--- Partida 1 ---")
    juego1.mostrar_info()
    juego1.jugar(jugador1, 20, "cara")

    print("\n--- Partida 2 ---")
    juego2.mostrar_info()
    juego2.jugar(jugador2, 10, "cruz")

    print("\n--- Estado final de los jugadores ---")
    print(jugador1)
    print(jugador2)

# Ejemplo de Output:

# Jugador(nombre='Guille', saldo=100, historial=[])
# JuegoCaraOCruz(nombre='Cara o Cruz', multiplicador_pago=2, ultimo_resultado=None)
#
# --- Partida 1 ---
# Juego: Cara o Cruz | Pago: x2
# Guille eligió cara.
# La moneda cayó en cara.
# ¡Guille ganó 40!
#
# --- Partida 2 ---
# Juego: Cara o Cruz VIP | Pago: x3
# Lucas eligió cruz.
# La moneda cayó en cara.
# Lucas perdió la apuesta.
#
# --- Estado final de los jugadores ---
# Jugador(nombre='Guille', saldo=120, historial=['Ganó apostando 20 a cara'])
# Jugador(nombre='Lucas', saldo=70, historial=['Perdió apostando 10 a cruz'])
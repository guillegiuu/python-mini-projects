# Proyecto 1: Cara o Cruz básico
# Temas : Clases, objetos, atributos, métodos

import random


# Clase Jugador
class Jugador:
    def __init__(self, nombre, saldo):
        # Atributos
        self.nombre = nombre
        self.saldo = saldo
        self.historial = []

    def puede_apostar(self, monto):
        # Devuelve True si el monto es válido
        return monto > 0 and monto <= self.saldo

    def apostar(self, monto):
        # Resta la apuesta del saldo
        if self.puede_apostar(monto):
            self.saldo -= monto
        else:
            print("No tienes saldo suficiente para apostar.")

    def agregar_ganancia(self, monto):
        # Suma la ganancia al saldo
        self.saldo += monto

    def __repr__(self):
        # Muestra la información del objeto
        return f"Jugador(nombre='{self.nombre}', saldo={self.saldo}, historial={self.historial})"


# Clase CaraOCruz
class CaraOCruz:
    def __init__(self, nombre="Cara o Cruz", pago=2):
        # Atributos
        self.nombre = nombre
        self.pago = pago
        self.ultimo_resultado = None

    def lanzar_moneda(self):
        # Guarda y devuelve cara o cruz
        self.ultimo_resultado = random.choice(["cara", "cruz"])
        return self.ultimo_resultado

    def jugar_ronda(self, jugador, apuesta, eleccion):
        # Hace interactuar al jugador con el juego
        if not jugador.puede_apostar(apuesta):
            print("La apuesta es mayor que el saldo.")
            return

        jugador.apostar(apuesta)
        resultado = self.lanzar_moneda()

        print(f"La moneda cayó en: {resultado}")

        if eleccion == resultado:
            ganancia = apuesta * self.pago
            jugador.agregar_ganancia(ganancia)
            print(f"¡Ganaste! Tu ganancia fue de {ganancia}")
            jugador.historial.append("Ganó")
        else:
            print("Perdiste la apuesta.")
            jugador.historial.append("Perdió")

    def __repr__(self):
        # Muestra la información del objeto
        return f"CaraOCruz(nombre='{self.nombre}', pago={self.pago}, ultimo_resultado={self.ultimo_resultado})"


# Pruebas del proyecto
if __name__ == "__main__":
    # Dos instancias de Jugador
    jugador1 = Jugador("Guille", 100)
    jugador2 = Jugador("Ana", 50)

    # Dos instancias de CaraOCruz
    juego1 = CaraOCruz()
    juego2 = CaraOCruz("Cara o Cruz Pro", 3)

    # Mostrar objetos
    print(jugador1)
    print(juego1)

    # Ronda 1
    print("\n--- Ronda 1 ---")
    juego1.jugar_ronda(jugador1, 20, "cara")

    # Ronda 2
    print("\n--- Ronda 2 ---")
    juego2.jugar_ronda(jugador2, 10, "cruz")

    # Resultados finales
    print("\n--- Resultados finales ---")
    print(jugador1)
    print(jugador2)


# Ejemplo de Output:
    
# Jugador(nombre='Guille', saldo=100, historial=[])
# CaraOCruz(nombre='Cara o Cruz', pago=2, ultimo_resultado=None)
#
# --- Ronda 1 ---
# La moneda cayó en: cruz
# Perdiste la apuesta.
#
# --- Ronda 2 ---
# La moneda cayó en: cruz
# ¡Ganaste! Tu ganancia fue de 30
#
# --- Resultados finales ---
# Jugador(nombre='Guille', saldo=80, historial=['Perdió'])
# Jugador(nombre='Ana', saldo=70, historial=['Ganó'])
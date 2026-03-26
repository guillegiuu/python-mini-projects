# Proyecto 3: Casino interactivo
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
        # Verifica si el monto es válido
        return monto > 0 and monto <= self.saldo

    def apostar(self, monto):
        # Descuenta dinero del saldo
        if self.puede_apostar(monto):
            self.saldo -= monto
        else:
            print("No puedes apostar ese monto.")

    def cobrar(self, monto):
        # Suma dinero al saldo
        self.saldo += monto

    def __repr__(self):
        return f"Jugador(nombre='{self.nombre}', saldo={self.saldo}, historial={self.historial})"


# Clase CaraOCruz
class CaraOCruz:
    def __init__(self, nombre="Cara o Cruz", multiplicador=2):
        # Atributos
        self.nombre = nombre
        self.multiplicador = multiplicador
        self.ultimo_resultado = None

    def lanzar_moneda(self):
        # Devuelve cara o cruz
        self.ultimo_resultado = random.choice(["cara", "cruz"])
        return self.ultimo_resultado

    def mostrar_reglas(self):
        # Muestra reglas simples
        print(f"Bienvenido a {self.nombre}.")
        print(f"Si ganas, cobras x{self.multiplicador} tu apuesta.")

    def jugar_ronda(self, jugador, apuesta, eleccion):
        # Ronda completa entre jugador y juego
        if not jugador.puede_apostar(apuesta):
            print("La apuesta no es válida.")
            return

        jugador.apostar(apuesta)
        resultado = self.lanzar_moneda()

        print(f"La moneda cayó en: {resultado}")

        if eleccion == resultado:
            ganancia = apuesta * self.multiplicador
            jugador.cobrar(ganancia)
            print(f"¡Ganaste {ganancia}!")
            jugador.historial.append("Ganó")
        else:
            print("Perdiste la ronda.")
            jugador.historial.append("Perdió")

    def __repr__(self):
        return f"CaraOCruz(nombre='{self.nombre}', multiplicador={self.multiplicador}, ultimo_resultado={self.ultimo_resultado})"


# Programa principal
if __name__ == "__main__":
    # Crear dos instancias de jugadores para cumplir el task
    jugador1 = Jugador("Jugador 1", 100)
    jugador2 = Jugador("Jugador 2", 100)

    # Crear dos instancias del juego para cumplir el task
    juego1 = CaraOCruz()
    juego2 = CaraOCruz("Cara o Cruz Especial", 3)

    # Mostrar objetos
    print(jugador1)
    print(juego1)

    print("\n--- Juego interactivo ---")
    nombre = input("Ingresa tu nombre: ")
    saldo_inicial = int(input("Ingresa tu saldo inicial: "))

    jugador_real = Jugador(nombre, saldo_inicial)
    juego = CaraOCruz()

    juego.mostrar_reglas()

    apuesta = int(input("Ingresa tu apuesta: "))
    eleccion = input("Elige cara o cruz: ").lower()

    juego.jugar_ronda(jugador_real, apuesta, eleccion)

    print("\n--- Estado final ---")
    print(jugador_real)

# Ejemplo de Output:

# Jugador(nombre='Jugador 1', saldo=100, historial=[])
# CaraOCruz(nombre='Cara o Cruz', multiplicador=2, ultimo_resultado=None)
#
# --- Juego interactivo ---
# Ingresa tu nombre: Guille
# Ingresa tu saldo inicial: 100
# Bienvenido a Cara o Cruz.
# Si ganas, cobras x2 tu apuesta.
# Ingresa tu apuesta: 20
# Elige cara o cruz: cara
# La moneda cayó en: cruz
# Perdiste la ronda.
#
# --- Estado final ---
# Jugador(nombre='Guille', saldo=80, historial=['Perdió'])
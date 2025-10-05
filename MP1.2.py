import random
from gpiozero import RGBLED, Button, Buzzer
import time

# Configuración de componentes

# Ajustamos los pines a nuestra conexión.
rgb1 = RGBLED(red=20, green=21, blue=17)

rgb2 = RGBLED(red=19, green=26, blue=16)   # Segundo RGB

botones = [Button(5), Button(6), Button(22), Button(23), Button(18)]

buzzer = Buzzer(25)

# Lista de letras del alfabeto

alfabeto = list('abcdefghijklmnopqrstuvwxyz')
letra_actual = 0

# Función para actualizar color según vidas


def mostrar_vidas(vidas):

    if vidas == 3:
        color = (0, 1, 0)   # Verde

    elif vidas == 2:
        color = (1, 1, 0)   # Amarillo

    elif vidas == 1:
        color = (1, 0, 0)   # Rojo

    else:
        color = (0, 0, 0)   # Apagado

    rgb1.color = color
    rgb2.color = color

# Bucle principal


while True:

    palabras = [
        "raton", "escritorio", "teclado", "botella", "lluvia",
        "estuche", "lapiz", "celular", "videojuego", "ventana", "planeta",
        "guitarra", "musica", "calculadora", "aventura", "secreto"
    ]

    num_letras = int(input("cantidad de letras: "))

    intentos_permitidos = min(
        3, int(input("cantidad de intentos (máximo 3): ")))

    palabra_posibles = [p for p in palabras if len(p) == num_letras]

    if not palabra_posibles:

        print(f"No hay palabras con {num_letras} letras.")

        continue

    palabra_adiv = random.choice(palabra_posibles)

    palabra_oculta = ["_"] * len(palabra_adiv)

    intentos_restantes = intentos_permitidos

    letras_usadas = []

    mostrar_vidas(intentos_restantes)

    print(f"Tienes {num_letras} letras y {intentos_permitidos} intentos.")

    while intentos_restantes > 0 and "_" in palabra_oculta:

        print(f"\nPalabra: {' '.join(palabra_oculta)}")

        print(f"Letra actual: {alfabeto[letra_actual]}")

        print(f"Intentos restantes: {intentos_restantes}")

        print(f"Letras usadas: {', '.join(letras_usadas)}")

        accion = None
        while accion is None:
            if botones[0].is_pressed:
                accion = "1"
            elif botones[1].is_pressed:
                accion = "2"
            elif botones[2].is_pressed:
                accion = "3"
            elif botones[3].is_pressed:
                accion = "4"
            elif botones[4].is_pressed:
                accion = "5"
            time.sleep(0.1)

        if accion == "1":
            letra_actual = (letra_actual + 1) % len(alfabeto)

        elif accion == "2":
            letra_actual = (letra_actual - 1) % len(alfabeto)

        elif accion == "3":
            letra_actual = (letra_actual + 5) % len(alfabeto)

        elif accion == "4":
            letra_actual = (letra_actual - 5) % len(alfabeto)

        elif accion == "5":
            letra = alfabeto[letra_actual]

            if letra in letras_usadas:

                print("Ya usaste esta letra")

                buzzer.beep(0.1, 0.1, 1)

            else:

                letras_usadas.append(letra)

                if letra in palabra_adiv:

                    print(f"¡Correcto! '{letra}' está en la palabra")

                    for i in range(len(palabra_adiv)):
                        if palabra_adiv[i] == letra:
                            palabra_oculta[i] = letra

                    buzzer.beep(0.2, 0.1, 1)

                else:

                    print(f"'{letra}' no está")

                    intentos_restantes -= 1

                    mostrar_vidas(intentos_restantes)

                    buzzer.beep(0.5, 0.1, 1)

    # Fin

    if "_" not in palabra_oculta:

        print("\n¡GANASTE!")

        print(f"La palabra era: {palabra_adiv}")

        buzzer.beep(0.2, 0.2, 3)

    else:

        print("Perdiste :(")

        print(f"La palabra era: {palabra_adiv}")

        buzzer.beep(0.5, 0.2, 2)

    mostrar_vidas(0)  # Apagar al final

    respuesta = input("¿Quieres jugar otra partida? (si/no): ").lower()

    if respuesta != "si":

        break

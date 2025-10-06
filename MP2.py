from gpiozero import LED, Button, Buzzer, LightSensor
import random
import time

leds = [
    LED(17),  # LED para botón 1

    LED(27),  # LED para botón 2

    LED(22),  # LED para botón 3
]
# Botones conectados a los pines GPIO
botones = [

    Button(23),  # Botón 1

    Button(24),  # Botón 2

    Button(25),  # Botón 3
]
# Buzzer y sensor
buzzer = Buzzer(18)  # Buzzer conectado al pin GPIO18
sensor = LightSensor(4)  # Fotoresistencia conectada al pin GPIO4
laser = LED(21)


def main():

    while True:

        # 1. Configuración inicial

        tiempo_total = int(
            input("Ingrese el tiempo total del juego (en segundos): "))

        permitir_repeticion = input(
            "¿Permitir repetición de botones? (si/no): ").lower() == "si"

        # Generar secuencia aleatoria

        secuencia = []

        if permitir_repeticion:

            secuencia = [random.randint(0, 2) for _ in range(3)]

        else:

            nums = list(range(3))

            random.shuffle(nums)

            secuencia = nums[:3]
        laser.on()
        print("\nEsperando la interrupción del láser para comenzar...")
        # 2. Esperar que se interrumpa el láser
        while sensor.value > 0.5:
            time.sleep(0.1)
        print("\n¡Juego iniciado!")
        tiempo_inicio = time.time()
        paso_actual = 0
        while tiempo_inicio + tiempo_total > time.time() and paso_actual < 3:
            tiempo_restante = tiempo_total - (time.time() - tiempo_inicio)
            print(f"\rTiempo restante: {tiempo_restante:.1f}s", end="")

            # Revisar cada botón

            for i, boton in enumerate(botones):

                if boton.is_pressed:

                    leds[i].on()  # Encender LED correspondiente

                    if i == secuencia[paso_actual]:

                        buzzer.beep(0.1, 0.1, 1)  # Tono de acierto

                        paso_actual += 1

                        print(f"\n¡Correcto! Paso {paso_actual} de 3")

                    else:

                        # Botón incorrecto

                        buzzer.beep(0.2, 0.2, 1)  # Tono de error

                        paso_actual = 0

                        print("\n¡Error! Volviendo al inicio de la secuencia")

                        tiempo_inicio -= 1  # Penalización de 1 segundo

                    # Pequeña pausa para evitar múltiples lecturas
                    time.sleep(0.3)

                    leds[i].off()

        # 4. Cierre de la partida

        if paso_actual == 3:

            print("\n¡Victoria! Has completado la secuencia")

            # Melodía de victoria no la alcanzamos a hacer

            for _ in range(3):

                buzzer.beep(0.1, 0.1, 1)

        else:

            print("\n¡Tiempo agotado!")

            # Melodía de game over no la alcanzamos a hacer

            buzzer.beep(0.5, 0.5, 1)

        # Preguntar si quiere jugar de nuevo

        if input("\n¿Desea jugar otra vez? (si/no): ").lower() != "si":

            break


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nJuego terminado.")

    finally:

        # Limpiar los componentes

        for led in leds:

            led.off()
        laser.off()
        buzzer.off()

import random


# bucle principal
while True:
 # Lista de palabras directamente en el código
    palabras = [
        "raton", "escritorio", "teclado", "botella", "lluvia",
        "estuche", "lapiz", "celular", "videojuego", "ventana", "planeta",
        "guitarra", "musica", "calculadora", "aventura", "secreto"
    ]

 # pedimos la configuración
    num_letras = int(input("cantidad de letras: "))
    intentos_permitidos = int(input("cantidad de intentos: "))

 # Filtramos la lista para obtener solo palabras con la longitud que se quiera
    palabras_posibles = []
    for p in palabras:
        if len(p) == num_letras:
            palabras_posibles.append(p)

 # Si no hay palabras de esa longitud, se avisa y se pide nuevamente el ingreso de la palabra
    if not palabras_posibles:
        print(
            f"Lo siento, no hay palabras con {num_letras} letras en nuestra listas. Intenta con otra longitud.")
        continue

 # acá elegimos la palabra al azar del diccionario lista que acabamos de hacer
    palabra_adiv = random.choice(palabras_posibles)

 # se inician las variables para la partida
    palabra_oculta = ["_"] * len(palabra_adiv)
    intentos_restantes = intentos_permitidos
    letras_usadas = []

    print(f"tienes {num_letras} letras! Tienes {intentos_permitidos} intentos.")

 # El juego continúa mientras queden intentos Y queden letras por adivinar
    while intentos_restantes > 0 and "_" in palabra_oculta:
     # vamos mostrando el estado actual

        print(f"Palabra: {' '.join(palabra_oculta)}")
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras ya usadas: {', '.join(letras_usadas)}")

     # Pedir una letra o la palabra al jugador
        intento = input(
            "Ingresa una letra o la palabra COMPLETA en caso de saber cual es! ").lower()

     # acá podemos tener 3 casos posibles, ir adivinando una por una, adivinar directamente la palabra
     # o ingresar algo inválido, que no esté en la lista o no cumpla con el largo

     # caso 1: se adivina la palabra completa
        if len(intento) == len(palabra_adiv):
            if intento == palabra_adiv:
                print("Qué crack")
                palabra_oculta = list(palabra_adiv)  # Autocompleta para ganar
            else:
                print(f"'{intento}' casi!,pero no es la palabra")
                intentos_restantes -= 1

     # caso 2: se ingresa letra por letra
        elif len(intento) == 1:
            letra = intento
            if letra in letras_usadas:
                print(" Ya intentaste con esa letra, tienes que intentar con otra")
            else:
                letras_usadas.append(letra)
                if letra in palabra_adiv:
                    print(f"bien! La letra '{letra}' es correcta.")
                    for i in range(len(palabra_adiv)):
                        if palabra_adiv[i] == letra:
                            palabra_oculta[i] = letra
                else:
                    print(f"cueck! La letra '{letra}' no está.")
                    intentos_restantes -= 1

     # CASO 3: El jugador ingresa algo inválido
        else:
            print(
                "Entrada no válida, tienes que intentar con una sola letra o tener el largo correcto.")

    if "_" not in palabra_oculta:
        print("palabra correcta")
        print(f"la palabra era: {palabra_adiv}")
    else:
        print(
            f"Perdiste! Se acabaron los intentos :( La palabra era: {palabra_adiv}")

    respuesta = input("¿quieres jugar otra partida? (si/no): ").lower()
    if respuesta != "si":

        break

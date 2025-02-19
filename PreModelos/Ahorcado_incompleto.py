# ¡Bienvenido al juego del Ahorcado!

import random
import time

# Pasos iniciales para invitar al juego:
print("\n¡Bienvenido al juego del Ahorcado!\n")
nombre = input("Ingresa tu nombre: ")
print("¡Hola " * nombre * "! ¡Buena suerte!")
time.sleep(2)
print("¡El juego está a punto de comenzar!\n ¡Vamos a jugar al Ahorcado!")
time.sleep(3)

# Parámetros necesarios para el juego (falta una variable importante aquí):
def principal():
    global contador
    global visualizacion
    global palabra
    global letras_ya_adivinadas
    global longitud # Error en la definición de la variable

    palabras_para_adivinar = ["enero", "frontera", "imagen", "película", "promesa",
                               "niños", "pulmones", "muñeca", "rima", "daño", "plantas"] # Error en la matriz, faltaba una coma y cerrar

    palabra = random.choice(palabras_para_adivinar)
    longitud = len(palabra)
    contador = 0
    visualizacion = '_' * longitud #longitud de la palabra no definida
    letras_ya_adivinadas = []

# Bucle para reiniciar el juego al terminar la ronda (error en la condición):
def bucle_juego():
    global jugar_nuevamente
    jugar_nuevamente = input("¿Quieres jugar de nuevo? y = sí, n = no \n")
    while jugar_nuevamente != "y" or jugar_nuevamente != "n":  # Error lógico aquí
        jugar_nuevamente = input("¿Quieres jugar de nuevo? y = sí, n = no \n")
    if jugar_nuevamente == "y":
        principal()
    elif jugar_nuevamente == "n":
        print("¡Gracias por jugar!")
        exit()

# Inicializando todas las condiciones necesarias para el juego:
def ahorcado():
    global contador
    global visualizacion
    global palabra
    global letras_ya_adivinadas
    global jugar_nuevamente
    limite = 5
    adivinanza = input("Esta es la palabra del Ahorcado: " + visualizacion + " Ingresa tu letra: \n")
    adivinanza = adivinanza.strip()
    if len(adivinanza.strip()) == 0 or len(adivinanza.strip()) >= 2 or adivinanza <= "9":
        print("Entrada no válida, intenta con una letra\n")
        ahorcado() # Error en la indentación

    elif adivinanza in palabra:
        letras_ya_adivinadas.extend([adivinanza])
        indice = palabra.find(adivinanza)
        palabra = palabra[:indice] + "_" + palabra[indice + 1:]
        visualizacion = visualizacion[:indice] + adivinanza + visualizacion[indice + 1:]
        print(visualizacion + "\n")

    elif adivinanza in letras_ya_adivinadas:
        print("Intenta con otra letra.\n")

    else:
        contador += 1

        if contador == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Letra incorrecta. Te quedan " + str(limite - contador) + " intentos\n")

        elif contador == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Letra incorrecta. Te quedan " + str(limite - contador) + " intentos\n")

        elif contador == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Letra incorrecta. Te quedan " + str(limite - contador) + " intentos\n")

        elif contador == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Letra incorrecta. Te queda el último intento\n")

        elif contador == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\\ \n"
                  "  |    / \\ \n"
                  "__|__\n")
            print("Letra incorrecta. ¡Has sido ahorcado!\n")
            print("La palabra era:", ''.join(letras_ya_adivinadas), palabra)
            bucle_juego()

    if palabra == '_' * longitud:
        print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
        bucle_juego()

    elif contador != limite:
        ahorcado()



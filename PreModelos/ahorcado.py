# ¡Bienvenido al juego del Ahorcado!
import random
import time

# Pasos iniciales para invitar al juego:
print("\n¡Bienvenido al juego del Ahorcado!\n")
nombre = input("Ingresa tu nombre: ")
print("¡Hola ", nombre, "! ¡Buena suerte!")
time.sleep(2)

print("¡El juego está a punto de comenzar!\n ¡Vamos a jugar al Ahorcado!")
time.sleep(3)

# Parámetros necesarios para el juego
def principal():
    global contador
    global visualizacion
    global palabra
    global letras_ya_adivinadas
    # Error en la definición de la variable
    global longitud 

    # Error en la matriz, faltaba una coma y cerrar
    palabras_para_adivinar = ["enano", "frontera", "mentalmente", "película", "promesas",
                               "palindromo", "elefante", "perro", "rara", "terraza", "peleas"]
    
    palabra = random.choice(palabras_para_adivinar)
    longitud = len(palabra)
    contador = 0
    visualizacion = '_' * longitud  # longitud de la palabra
    letras_ya_adivinadas = []

# Bucle para reiniciar el juego al terminar la ronda
def bucle_juego():
    global jugar_nuevamente
    jugar_nuevamente = input("¿Quieres jugar de nuevo? y = sí, n = no \n")
    while jugar_nuevamente == "y":
        principal()
        ahorcado()
        jugar_nuevamente = input("¿Quieres jugar de nuevo? y = sí, n = no \n")
    if jugar_nuevamente == "n":
        print("¡Gracias por jugar!")
        exit()

# Inicializando todas las condiciones necesarias para el juego
def ahorcado():
    global contador
    global visualizacion
    global palabra
    global letras_ya_adivinadas

    limite = 5
    adivinanza = input("Esta es la palabra del Ahorcado: " + visualizacion + " Ingresa tu letra: \n")
    adivinanza = adivinanza.strip()

    # Error en la condición y en la identación
    if len(adivinanza) == 0 or len(adivinanza) > 1 or not adivinanza.isalpha():
        print("Entrada no válida, intenta con una letra\n")
        ahorcado()
        return

    if adivinanza in letras_ya_adivinadas:
        print("Ya has adivinado esa letra, intenta con otra.\n")
        ahorcado()
        return

    letras_ya_adivinadas.append(adivinanza)
    
    if adivinanza in palabra:
        visualizacion = ''.join([adivinanza if letra == adivinanza else visualizacion[i] 
                                 for i, letra in enumerate(palabra)])
        print("¡Bien hecho!", visualizacion + "\n")
        
    else:
        contador += 1
        print("Letra incorrecta. Te quedan " + str(limite - contador) + " intentos\n")

    # Dibuja el ahorcado
    if contador == 1:
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif contador == 2:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif contador == 3:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif contador == 4:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif contador == 5:
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\\ \n"
              "  |    / \\ \n"
              "__|__\n")
        print("¡Has sido ahorcado!\n")
        print("La palabra era:", palabra)
        bucle_juego()

    if visualizacion == palabra:
        print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
        bucle_juego()
    else:
        ahorcado()

# Inicio del juego
principal()
ahorcado()
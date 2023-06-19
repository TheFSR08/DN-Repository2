import random

# Palabras para el juego de ahorcado
palabras = ["gato", "perro", "elefante", "jirafa", "leon"]

# Función para seleccionar una palabra al azar
def seleccionar_palabra():
    return random.choice(palabras)

# Función para mostrar el estado actual de la palabra
def mostrar_palabra(palabra, letras_correctas):
    mostrado = ""
    for letra in palabra:
        if letra in letras_correctas:
            mostrado += letra + " "
        else:
            mostrado += "_ "
    return mostrado

# Función para verificar si se ha adivinado la palabra completa
def verificar_adivinanza(palabra, letras_correctas):
    for letra in palabra:
        if letra not in letras_correctas:
            return False
    return True

# Juego de ahorcado
def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_correctas = []
    intentos_restantes = 6

    print("¡Bienvenido al juego de ahorcado!")
    print("Adivina la palabra. ¡Buena suerte!")

    while intentos_restantes > 0:
        print("\n" + mostrar_palabra(palabra_secreta, letras_correctas))
        letra = input("Ingresa una letra: ")

        if letra in letras_correctas:
            print("Ya has ingresado esa letra. ¡Intenta con otra!")
            continue

        if letra in palabra_secreta:
            letras_correctas.append(letra)
            if verificar_adivinanza(palabra_secreta, letras_correctas):
                print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
                break
        else:
            intentos_restantes -= 1
            print("Letra incorrecta. Te quedan", intentos_restantes, "intentos.")

    if intentos_restantes == 0:
        print("\n¡Oh no! Has perdido. La palabra era:", palabra_secreta)

# Ejecutar el juego
jugar_ahorcado()

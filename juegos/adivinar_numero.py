import random

def adivinar_numero(respuesta):
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    numero = random.randint(1,10)
    seguir = True
    while seguir: 
        if numero == respuesta:
            print("BIEN!! ADIVINASTE")
            seguir = False
        else:
            print("fallaste :( Intentalo de nuevo")
            respuesta = int(input("Ingresa el numero que crees que estoy pensando: ...."))

    pass

print("HOLA! BIENVENID@")
respuesta = int(input("Ingresa el numero que crees que estoy pensando: ...."))
adivinar_numero(respuesta)


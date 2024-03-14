import random 

def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    seguir = True
    puntuacion = 0
    puntuacion_comp = 0
    while seguir:

        print("Por favor presione ENTER para lanzar el dado")
        enter = input("  ")

        numero = random.randint(1, 6)
        puntuacion = puntuacion + numero
        numero_comp = numero = random.randint(1, 6)
        puntuacion_comp = puntuacion_comp + numero_comp
        print("Tu puntuación es:" + puntuacion)

        if puntuacion >= 30 and puntuacion_comp >= 30: 
            print("EMPATE")
            seguir = False
        elif puntuacion >= 30 and puntuacion_comp < 30: 
            print("GANASTE!")
            seguir = False
        elif puntuacion < 30 and puntuacion_comp >= 30:
            print("PERDISTE :()") 
            seguir = False


    pass

print("BIENVENID@")
juego_del_dado()
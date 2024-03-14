import random
def cachipun():
    print("Bienvenido al juego de la selva. Cazador(1) mata a escopeta(2), escopeta(2) mata a tigre(3) y tigre(3) mata a cazador(1).")
    print("1. Cazador")
    print("2. Escopeta")
    print("3. Tigre")
    jugador = input("Elige un numero del 1 al 3")
    if jugador == 1:
        print("Has elegido Cazador")
    elif jugador == 2:
        print("Has elegido Escopeta")
    else:
        print("Has elegido Tigre")
    
    computadora = random.randint(1,3)
    if computadora == 1:
        print("La computadora ha elegido Cazador")
    elif computadora == 2:
        print("La computadora ha elegido Escopeta")
    else:
        print("La computadora ha elegido Tigre")
    if jugador == 1:
        if computadora == 1:
            print("Has empatado")
        elif computadora == 2:
            print("Has ganado!")
        else:
            print("Has perdido:(")
    elif jugador == 2:
        if computadora == 2:
            print("Has empatado")
        elif computadora == 3:
            print("Has ganado!")
        else:
            print("Has perdido:(")
    elif jugador == 3:
        if computadora == 3:
            print("Has empatado")
        elif computadora == 1:
            print("Has ganado!")
        else:
            print("Has perdido:(")
        
    pass


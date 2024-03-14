def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    print("Hola!, acabas de entrar al juego de memoria mas increible del mundo!!!")
    print("Te mostraremos una secuencia de 7 numeros y debes memorizarla, luego te pediremos que nos des la secuencia.")
    n = random.randint(1000000,9999999)
    a = input("Estas listo? (1. si ; 2. no) ")
    if a == 1:
        print("Vamos!")
    else:
        print("No me importa, Vamos!")
    for i in range(20):
        print("MEMORIZA")
    
    b = int(input("Inserta el numero: "))
    if b == n:
        print("Has ganado!")
    else:
        print("Perdiste fracasado")
    pass
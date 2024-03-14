def adivinar_par_o_impar():
    import random
    n = random.randint(1, 100)
    par = False
    if n%2 == 0:
        par = True
    print(n, "es par o impar?")
    a = input("Ingrese su respuesta: ")
    if (a == "par" and par) or (a == "impar" and par == False):
        print("Adivinaste! Felicitaciones!")
        return("")
    print("Fallaste, ;(")    

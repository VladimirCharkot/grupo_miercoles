from random import randint 

def tirada(cuantos, caras):
    suma = 0
    for i in range(cuantos):
        suma += randint(1, caras)
    return suma

def promediar(veces):
    total = 0
    for i in range(veces):
        total += tirada(4, 6)
    return total / veces

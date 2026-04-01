def saludar(nombre):
    print(f'Hola {nombre}')

def despedir(nombre):
    print(f'Chau {nombre}')

# Funciones de primer orden
# Higher order functions
def a_vla(f):
    f('vla')

# -----
from time import time

def medir(f):
    t0 = time()
    f()
    t1 = time()
    print(f'La función demoró {t1-t0} ms')
    
def saludar_a_ren():
    saludar('ren')

def saludar_a_luki():
    saludar('luki')

def mapear(lista, funcion):
    nueva = []
    for elem in lista:
        nueva.append(funcion(elem))
    return nueva

def filtrar(lista, funcion):
    nueva = []
    for elem in lista:
        if funcion(elem):
            nueva.append(elem)
    return nueva




    

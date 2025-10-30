from random import randint

def tirar(veces):
    numeros = []
    for i in range(veces):
        numeross = randint(1,6)
        numeros.append(numeross)
    return numeros

# Falta implementar
def poker(numeros):
  return False

# Falta implementar: 
def foul(numeros): 
  return False

def generala(numeros):
    for i in numeros:
        if i != numeros[0]:
            return False
    return True

def escalera(ns):
  # ns = sorted(numeros)
  ns.sort()
  for n in range(len(ns) - 1):
    if ns[n] + 1 != ns[n + 1]:
      return False
  return True


def estadistica():
  num = 0
  veces = int(input("Cuantas tiradas quieres hacer?  -"))
  for i in range(veces):
    if generala(tirar(5)): 
      num += 1

  porcentaje = (num / veces) * 100
  porcentaje = round(porcentaje, 3)
  print(f"Se repite {porcentaje}%")
  
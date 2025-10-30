from random import randint


def bold(text):
    return "\x1B[1m" + text + "\x1B[0m"

def italic(text):
    return "\x1B[3m" + text + "\x1B[0m"

def underline(text):
    return "\x1B[4m" + text + "\x1B[0m"
    
def asopotro(subensis, mascapos):
  cupo = ''
  for ito in subensis:
    if ito in mascapos:
      cupo += ito
    else:
      cupo += 'X'
  return cupo

def tirar(veces):
    numeros = []
    for i in range(veces):
        numeross = randint(1,6)
        numeros.append(numeross)
    return numeros

def es_par(numero):
    return numero % 2 == 0

# if es_par(sum(tirar(2))):
#     print(bold("Es par"))


# print(underline(italic(asopotro('Holanda', ['h', 'a']))))
# print(underline(bold(italic(asopotro(___, ___)))))

s = 'sfbaskjbfksa'
print('hola: ' + s.upper())

if s.isalpha():
  print('Es alfanumerico :) ')
  
print(s.count('a') * '#')
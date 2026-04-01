num = int(input('Cantidad de elementos: '))

abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 3 -> ABC, ACB, BAC, BCA, CAB, CBA

def quitar(palabra, letras): 
  nueva = ''
  for l in palabra:
    if not (l in letras):
      nueva += str(l)
  return nueva

letras = abecedario[0:num]

for letra1 in letras:
  for letra2 in quitar(letras, letra1):
    for letra3 in quitar(letras, letra1 + letra2):
      print(letra1, letra2, letra3)
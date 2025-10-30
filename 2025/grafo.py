from random import choice

grafo = {
  'piedra': ['tijera', 'motosierra'],
  'papel': ['piedra', 'agua'],
  'tijera': ['papel', 'motosierra'],
  'agua': ['piedra', 'tijera'],
  'motosierra': ['papel', 'agua']
}

opciones = list(grafo.keys())

print('Tus opciones son: ')

for elemento in opciones:
  print(elemento)

usuario = input('Elegi una opcion > ')
while usuario not in grafo: 
  usuario = input('Elegi una opción de las disponibles > ')
  
print('Tu elección', usuario)
print('Tu elección le gana a: ', grafo[usuario])

computadora = choice(opciones)

print('La computadora eligió', computadora)
print('Lo que la computadora eligió le gana a', grafo[computadora])

# __________ "Ganaste" / "Perdiste"
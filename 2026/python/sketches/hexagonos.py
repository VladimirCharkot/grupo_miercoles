from random import randint
from py5 import *

# Buffer para almacenar las posiciones y colores de los hexágonos
posiciones = []

# Cantidad de hexagonos a dibujar
hexas = 128

# Amplitud del noise
dn = 10

# Radio de los hexágonos
r = 20

def settings():
  size(400, 400)
  global posiciones
  for _ in range(hexas):
    posiciones.append((randint(0, 400), randint(0, 400), (randint(100, 250), randint(100, 250), randint(100, 250))))
    
def hexa(r): 
  with begin_closed_shape():
    for i in range(6):
        vertex(cos(i * TAU / 6) * r, sin(i * TAU / 6) * r)

def draw():
  background(235)
  
  for i in range(hexas):
    x, y, c = posiciones[i]
    dx, dy = dn * os_noise(millis()/1000, 2.2 * i), dn * os_noise(millis()/1000, 32.2 * i)
    push_matrix()
    translate(x, y)
    rotate(millis()/500)
    translate(dx, dy)
    fill(*c)
    hexa(r)
    pop_matrix()

run_sketch()
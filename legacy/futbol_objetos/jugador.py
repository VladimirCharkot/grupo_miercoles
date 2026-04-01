
from jugadores import jugadores as jugadores_diccionarios

class Jugador:
  botines = None
  
  def __init__(self, nombre, talle, edad, rol):
    print(f'Creando nuevo jugador {nombre}')
    self.nombre = nombre
    self.talle = talle
    self.edad = edad
    self.rol = rol
  
  def saludar(self):
    print(f'Soy {self.nombre}, juego de {self.rol}, tengo {self.edad} años y calzo {self.talle}')

  def puntaje_jugador(self):
    
    if not(self.botines):
      return 0
    
    if self.botines.talle == self.talle:
      return 10

    return 4
  
jugadores_objetos = []

for jug in jugadores_diccionarios:
  jugador_objeto = Jugador(jug['nombre'], jug['talle'], jug['edad'], jug['rol'])
  jugadores_objetos.append(jugador_objeto)
  
  
vla = Jugador('Vla', 'L', 32, 'defensa')
ren = Jugador('Ren', 'M', 15, 'defensa')
luki = Jugador('Luki', 'S', 12, 'mediocampista')

jugadores_objetos.append(vla)
jugadores_objetos.append(ren)
jugadores_objetos.append(luki)
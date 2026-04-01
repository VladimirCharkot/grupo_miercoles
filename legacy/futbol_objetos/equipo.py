from jugador import jugadores_objetos

class Equipo:
  
  def __init__(self, nombre, jugadores):
    self.nombre = nombre

    if len(jugadores) < 5: 
      raise "Necesitamos al menos cinco jugadores"

    self.mediocampistas = []
    self.delanteros = []
    self.defensas = []
    self.arquero = []
    
    for jugador in jugadores:
      if jugador.rol == 'mediocampista':
        self.mediocampistas.append(jugador)
      elif jugador.rol == 'delantero':
        self.delanteros.append(jugador)
      elif jugador.rol == 'defensa':
        self.defensas.append(jugador)
      elif jugador.rol == 'arquero':
        self.arquero.append(jugador)
  
  def mostrar(self):
    print('Equipo', self.nombre, 'de', len(self.mediocampistas), 'mediocampistas')
    
  def puntaje_equipo(self):
    puntaje = 0
    for jug in self.delanteros:
      if jug.rol == "delantero":
        puntaje += 7
  
e = Equipo('Equipito', jugadores_objetos[:11])
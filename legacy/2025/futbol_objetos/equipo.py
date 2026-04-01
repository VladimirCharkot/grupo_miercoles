from jugadores import jugadores

def extraer(jugadores, rol):
  de_este_rol = []
  for jugador in jugadores:
    if jugador.rol == rol:
      de_este_rol.append(jugador)
  return de_este_rol


class Equipo:
  
  def __init__(self, jugadores, nombre):
    print(f'Creando equipo {nombre}')
    self.nombre = nombre
    self.delanteros = extraer(jugadores, 'delantero')
    self.delanteros = [jug for jug in jugadores if jug.rol == 'delantero']
    self.defensas = extraer(jugadores, 'defensa')
    self.mediocampistas = extraer(jugadores, 'mediocampista')
    self.arquero = extraer(jugadores, 'arquero')[0]
    
  def mostrar_plantel(self):
    print('Equipo:', self.nombre)
    print('Jugadores:')
    print('- Delanteros:')
    for jug in self.delanteros:
      print(jug)
    print('- Mediocampistas:')
    for jug in self.mediocampistas:
      print(jug)
    print('- Defensas:')
    for jug in self.defensas:
      print(jug)
    print('- Arquero:')
    print(self.arquero)
    
    
  # Hoy refactorizamos esta:
  def reportar_problemas(self):
    problemas = []
    
    # Nos fijamos si entre los delanteros, defensas y mediocampistas si hay alguno que no esté en su rol
    posiciones = ["delantero", "defensa", "mediocampista"]
    for posicion in posiciones:
      # for jug in getattr(self, posicion + 's'):
      for jug in _______:
        
        if jug.rol != posicion:
          problemas.append(f'{jug.nombre} tiene rol {jug.rol} pero está jugando de {posicion}')
          
        if not(jug.botines):
          problemas.append(f'{jug.nombre} no tiene botines!')
          
        elif jug.botines.talle != jug.talle:
          problemas.append(f'{jug.nombre} calza talle {jug.talle} pero sus botines son {jug.botines.talle}!')
    
    # Para el arquero:
    if self.arquero.rol != "arquero":
      problemas.append(f'{self.arquero.nombre} está de arquero pero es {self.arquero.rol}')
    if not(self.arquero.botines):
      problemas.append(f'{self.arquero.nombre} no tiene botines!')
    elif self.arquero.botines.talle != self.arquero.talle:
      problemas.append(f'{self.arquero.nombre} calza talle {self.arquero.talle} pero sus botines son {self.arquero.botines.talle}!')
    
    return problemas
  
  def puntaje(self):
    puntaje = 0
    
    # Nos fijamos que los roles coincidan con las posiciones
    for jug in self.delanteros:
      if jug.rol == "delantero":
        puntaje += 7
    
    for jug in self.defensas:
      if jug.rol == "defensa":
        puntaje += 7
    
    for jug in self.mediocampistas:
      if jug.rol == "mediocampista":
        puntaje += 7
      if jug.rol == "delantero":
        puntaje += 3
      if jug.rol == "defensa":
        puntaje += 3
        
    if self.arquero.rol == "arquero":
      puntaje += 7
    
    for jug in self.delanteros:
      puntaje += jug.puntaje()
    for jug in self.defensas:
      puntaje += jug.puntaje()
    for jug in self.mediocampistas:
      puntaje += jug.puntaje()
      
    puntaje += self.arquero.puntaje()
    
    return puntaje
    

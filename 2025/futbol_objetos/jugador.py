
class Jugador:
  botines = None
  
  def __init__(self, nombre, talle, edad, rol):
    print(f'Creando nuevo jugador {nombre}')
    self.nombre = nombre
    self.talle = talle
    self.edad = edad
    self.rol = rol
    
  def __repr__(self):
    return f'{self.nombre} ({self.rol})'
  
  def __str__(self):
    return self.nombre
  
  def saludar(self):
    print(f'Soy {self.nombre}, juego de {self.rol}, tengo {self.edad} años y calzo {self.talle}')

  def puntaje(self):
    
    if not(self.botines):
      return 0
    
    if self.botines["talle"] == self.talle:
      return 10

    return 4
  
  def equipar(self, botines):
    self.botines = botines
    print(f'{self.nombre} se calzó unos {botines['nombre']}')

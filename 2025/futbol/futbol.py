from random import sample
from jugadores import jugadores, riquelme, messi, cristiano, dibu_martinez
from botines import botines

# Función de puntaje
def puntaje_jugador(jugador):
  
  if not('botines' in jugador) or not(jugador["botines"]):
    return 0
  
  if jugador["botines"]["talle"] == jugador["talle"]:
    return 10

  return 4

# Definimos un equipo
los_campeones = {
    "nombre": "Los Campeones",
    "jugadores": {
      "mediocampistas": [riquelme],
      "delanteros": [messi],
      "defensas": [cristiano],
      "arquero": dibu_martinez
    }
}

def puntaje_equipo(equipo):
  puntaje = 0
  
  # Nos fijamos que los roles coincidan con las posiciones
  for jug in equipo["jugadores"]["delanteros"]:
    if jug["rol"] == "delantero":
      puntaje += 7
  
  for jug in equipo["jugadores"]["defensas"]:
    if jug["rol"] == "defensa":
      puntaje += 7
  
  for jug in equipo["jugadores"]["mediocampistas"]:
    if jug["rol"] == "mediocampista":
      puntaje += 7
    if jug["rol"] == "delantero":
      puntaje += 3
    if jug["rol"] == "defensa":
      puntaje += 3
      
  if equipo["jugadores"]["arquero"]["rol"] == "arquero":
    puntaje += 7
  
  for jug in equipo["jugadores"]["delanteros"]:
    puntaje += puntaje_jugador(jug)
  for jug in equipo["jugadores"]["defensas"]:
    puntaje += puntaje_jugador(jug)
  for jug in equipo["jugadores"]["mediocampistas"]:
    puntaje += puntaje_jugador(jug)
    
  puntaje += puntaje_jugador(equipo["jugadores"]["arquero"])
  
  return puntaje
  
def reportar_problemas(equipo):
  problemas = []
  
  # Nos fijamos si entre los delanteros, defensas y mediocampistas si hay alguno que no esté en su rol
  posiciones = ["delantero", "defensa", "mediocampista"]
  for posicion in posiciones:
    for jug in equipo["jugadores"][posicion + 's']:
      
      if jug["rol"] != posicion:
        problemas.append(f'{jug['nombre']} tiene rol {jug['rol']} pero está jugando de {posicion}')
        
      if not(jug["botines"]):
        problemas.append(f'{jug['nombre']} no tiene botines!')
        
      elif jug["botines"]["talle"] != jug["talle"]:
        problemas.append(f'{jug['nombre']} calza talle {jug["talle"]} pero sus botines son {jug["botines"]["talle"]}!')
  
  # Para el arquero:
  if equipo["jugadores"]["arquero"]["rol"] != "arquero":
    problemas.append(f'{jug['nombre']} está de arquero pero es {equipo["jugadores"]["arquero"]["rol"]}')
  if not(equipo["jugadores"]["arquero"]["botines"]):
    problemas.append(f'{jug['nombre']} no tiene botines!')
  elif equipo["jugadores"]["arquero"]["botines"]["talle"] != equipo["jugadores"]["arquero"]["talle"]:
    problemas.append(f'{jug['nombre']} calza talle {jug["talle"]} pero sus botines son {jug["botines"]["talle"]}!')
  
  return problemas

def generar_equipo():
  bots = sample(botines, 5)
  jugs = sample(jugadores, 5)
  
  jugs[0]['botines'] = bots[0]
  jugs[1]['botines'] = bots[1]
  jugs[2]['botines'] = bots[2]
  jugs[3]['botines'] = bots[3]
  jugs[4]['botines'] = bots[4]
  
  return {
    "nombre": "Generado",
    "jugadores": {
      "mediocampistas": [jugs[0], jugs[1]],
      "delanteros": [jugs[2]],
      "defensas": [jugs[3]],
      "arquero": jugs[4]
    }
  }

def mostrar_equipo(equipo):
  print('Equipo:', equipo['nombre'])
  print('Jugadores:')
  print('- Delanteros:')
  for jug in equipo["jugadores"]["delanteros"]:
    print(f'  - {jug["nombre"]} con botines {jug["botines"]["nombre"]}')
  print('- Mediocampistas:')
  for jug in equipo["jugadores"]["mediocampistas"]:
    print(f'  - {jug["nombre"]} con botines {jug["botines"]["nombre"]}')
  print('- Defensas:')
  for jug in equipo["jugadores"]["defensas"]:
    print(f'  - {jug["nombre"]} con botines {jug["botines"]["nombre"]}')
  print('- Arquero:')
  print(f'  - {equipo["jugadores"]["arquero"]["nombre"]} con botines {equipo["jugadores"]["arquero"]["botines"]["nombre"]}')
  
def evaluar_calidad(equipo):
  pje = puntaje_equipo(equipo)
  if pje < 20: 
    return 'malo'
  if pje >= 20 and pje < 30: 
    return 'medio'
  if pje >= 30: 
    return 'bueno'
  

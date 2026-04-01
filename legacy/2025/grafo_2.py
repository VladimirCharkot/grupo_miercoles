
from random import choice
from time import sleep

paises = {
  'argentina': ['brasil', 'uruguay'],
  'brasil': ['argentina', 'uruguay'],
  'uruguay': ['argentina', 'brasil'],
  'colombia': ['peru', 'venezuela'],
  'peru': ['colombia'],
  'venezuela': ['colombia'],
}

cosas = {
  'mercurio': ['venus', 'marte', 'júpiter'],
  'gamma': ['alfa', 'delta', 'theta'],
  'naranja': ['manzana', 'uva'],
  'zeta': ['beta', 'épsilon', 'theta'],
  'saturno': ['venus', 'marte', 'júpiter'],
  'alfa': ['beta', 'gamma', 'delta'],
  'plátano': ['manzana', 'uva'],
  'épsilon': ['beta', 'delta', 'zeta', 'eta'],
  'marte': ['mercurio', 'júpiter', 'saturno'],
  'theta': ['gamma', 'zeta', 'eta'],
  'manzana': ['naranja', 'plátano'],
  'beta': ['alfa', 'épsilon', 'zeta'],
  'venus': ['mercurio', 'saturno'],
  'eta': ['delta', 'épsilon', 'theta'],
  'uva': ['naranja', 'plátano'],
  'júpiter': ['mercurio', 'marte', 'saturno'],
  'delta': ['alfa', 'gamma', 'eta', 'épsilon'],
}

grafo = cosas

lugares = list(grafo.keys())

visitados = []

islas = []
isla = []

seguir = True

lugar = choice(lugares)
por_visitar = grafo[lugar].copy()

while seguir:
  visitados.append(lugar)
  isla.append(lugar)

  for destino in grafo[lugar]:
    print(f'Desde {lugar} se puede llegar a {destino}...')
    if destino in visitados:
      print(f'...pero por ahí ya pasamos')
    elif destino in por_visitar:
      print(f'...pero ya lo tenemos agendado')
    else:
      por_visitar.append(destino)
      print(f'...lo agregamos a los pendientes de visitar')

  # Si nos quedan lugares por visitar, vamos
  if por_visitar:
    lugar = choice(por_visitar)
    por_visitar.remove(lugar)
    
  else: 
    islas.append(isla.copy())
    isla = []
    
    # Si ya visitamos todos los lugares, listo
    if len(visitados) == len(lugares):
      seguir = False
      
    # Sino, elejimos uno que no hayamos visitado
    else: 
      posibles = lugares.copy()
      for visitado in visitados:
        posibles.remove(visitado)
      lugar = choice(posibles)
  
print('Las islas son: ')
print(islas)

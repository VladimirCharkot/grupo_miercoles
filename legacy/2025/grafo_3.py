
con_ciclo = {
  'a': ['d','b'],
  'b': ['c'],
  'c': ['a'],
  'd': [],
  'e': ['d']
}

sin_ciclo = {
  'a' : ['b'],
  'b': ['c'],
  'c': [],
}

sin_ciclo_2 = {
  'a': ['b', 'c'],
  'b': [],
  'c': ['b']
}

grafo = con_ciclo

nodos = list(grafo.keys())

# Arrancamos una vez por cada nodo
for primer_nodo in nodos:

  visitados = []
  nodo_actual = primer_nodo
  por_visitar = grafo[nodo_actual].copy()
  
  print(f'Arrancando desde {nodo_actual}')

  # Mientras queden nodos en la lista por visitar
  while por_visitar:
    visitados.append(nodo_actual)

    # Miramos los vecinos de este: 
    for destino in grafo[nodo_actual]:
      print(f'Desde {nodo_actual} se puede llegar a {destino}...')
      
      # Si ya lo visitamos es que hay un bucle!
      if destino in visitados:
        print('Hay bucle!')
        exit()

    # Si nos quedan lugares por visitar, vamos
    nodo_actual = por_visitar.pop()
    por_visitar.extend(grafo[nodo_actual].copy())
      
print("No hay bucle")
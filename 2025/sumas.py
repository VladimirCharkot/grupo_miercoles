def sumar(lista):
  
  linea_anterior = lista
  while len(linea_anterior) > 1:
    siguiente_linea = []
    for i in range(len(linea_anterior) - 1):
      siguiente_linea.append(linea_anterior[i] + linea_anterior[i + 1])

    linea_anterior = siguiente_linea
    
  return linea_anterior[0]
  
print(sumar([1, 2, 3, 4]))

print(sumar([21, 5, 7, 10]))

print(sumar([21, 6, 7, 10]))

print(sumar([22, 4, 7, 10]))

print(sumar([21, 5, 7, 11]))

print(sumar([22, 24, 26, 21]))
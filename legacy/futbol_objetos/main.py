
intentos = 0
seguir = True
equipo = None

while seguir:
  intentos += 1
  
  # Agarrar jugadores al azar
  
  # Crear un equipo y guardarlo en la variable `equipo`
  
  # Reportar problemas del equipo
  
  print(f'Encontramos {len(resultado)} problemas')
  if len(resultado) == 0:
    print(f'Equipo perfecto!')
    seguir = False

equipo.mostrar()

print('El puntaje del equipo es', puntaje_equipo(eqp))
print('Así que el equipo es', evaluar_calidad(eqp))
print('Encontrar un equipo sin problemas nos tomó', intentos, 'intentos')
from futbol import generar_equipo, reportar_problemas, mostrar_equipo, puntaje_equipo, evaluar_calidad

# Main:

intentos = 0
seguir = True

while seguir:
  intentos += 1
  eqp = generar_equipo()
  resultado = reportar_problemas(eqp)
  print(f'Encontramos {len(resultado)} problemas')
  if len(resultado) == 0:
    print(f'Equipo perfecto!')
    seguir = False

mostrar_equipo(eqp)

print('El puntaje del equipo es', puntaje_equipo(eqp))
print('Así que el equipo es', evaluar_calidad(eqp))
print('Encontrar un equipo sin problemas nos tomó', intentos, 'intentos')
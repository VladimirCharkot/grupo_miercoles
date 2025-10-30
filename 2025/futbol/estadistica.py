from futbol import generar_equipo, reportar_problemas

ensayos = 1000000
perfectos = 0

for i in range(ensayos):
  eqp = generar_equipo()
  resultado = reportar_problemas(eqp)
  if len(resultado) == 0:
    perfectos += 1

print('Hubo', perfectos, 'equipos perfectos')
print('La probabilidad de equipo perfecto es:', 100*(perfectos/ensayos), '%')
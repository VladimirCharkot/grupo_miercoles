import { generarEquipo, reportarProblemas, mostrarEquipo, puntajeEquipo, evaluarCalidad } from './futbol.js'

// Main:
let intentos = 0
let seguir = true
let eqp

while (seguir) {
  intentos += 1
  eqp = generarEquipo()
  const resultado = reportarProblemas(eqp)
  console.log(`Encontramos ${resultado.length} problemas`)
  if (resultado.length === 0) {
    console.log('Equipo perfecto!')
    seguir = false
  }
}

mostrarEquipo(eqp)
console.log('El puntaje del equipo es', puntajeEquipo(eqp))
console.log('Así que el equipo es', evaluarCalidad(eqp))
console.log('Encontrar un equipo sin problemas nos tomó', intentos, 'intentos')

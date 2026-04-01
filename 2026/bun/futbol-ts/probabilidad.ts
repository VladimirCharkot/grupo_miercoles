import { generarEquipo, reportarProblemas } from './futbol.js';

const ensayos: number = 1000000;
let perfectos: number = 0;

for (let i = 0; i < ensayos; i++) {
  const eqp = generarEquipo();
  const resultado = reportarProblemas(eqp);
  if (resultado.length === 0) {
    perfectos += 1;
  }
}

console.log('Hubo', perfectos, 'equipos perfectos');
console.log('La probabilidad de equipo perfecto es:', 100 * (perfectos / ensayos), '%');
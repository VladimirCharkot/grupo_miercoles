// Importar datos (asumiendo que existen estos archivos JS)
import { jugadores, riquelme, messi, cristiano, dibu_martinez } from './jugadores.js';
import { botines } from './botines.js';

// Función auxiliar para sample (equivalente a random.sample de Python)
function sample(array, n) {
  const shuffled = [...array].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, n);
}

// Función de puntaje
function puntajeJugador(jugador) {
  if (!jugador.botines) {
    return 0;
  }
  
  if (jugador.botines.talle === jugador.talle) {
    return 10;
  }
  return 4;
}

// Definimos un equipo
const losCampeones = {
  nombre: "Los Campeones",
  jugadores: {
    mediocampistas: [riquelme],
    delanteros: [messi],
    defensas: [cristiano],
    arquero: dibu_martinez
  }
};

function puntajeEquipo(equipo) {
  let puntaje = 0;
  
  // Nos fijamos que los roles coincidan con las posiciones
  for (const jug of equipo.jugadores.delanteros) {
    if (jug.rol === "delantero") {
      puntaje += 7;
    }
  }
  
  for (const jug of equipo.jugadores.defensas) {
    if (jug.rol === "defensa") {
      puntaje += 7;
    }
  }
  
  for (const jug of equipo.jugadores.mediocampistas) {
    if (jug.rol === "mediocampista") {
      puntaje += 7;
    }
    if (jug.rol === "delantero") {
      puntaje += 3;
    }
    if (jug.rol === "defensa") {
      puntaje += 3;
    }
  }
      
  if (equipo.jugadores.arquero.rol === "arquero") {
    puntaje += 7;
  }
  
  for (const jug of equipo.jugadores.delanteros) {
    puntaje += puntajeJugador(jug);
  }
  for (const jug of equipo.jugadores.defensas) {
    puntaje += puntajeJugador(jug);
  }
  for (const jug of equipo.jugadores.mediocampistas) {
    puntaje += puntajeJugador(jug);
  }
    
  puntaje += puntajeJugador(equipo.jugadores.arquero);
  
  return puntaje;
}

function reportarProblemas(equipo) {
  const problemas = [];
  
  // Nos fijamos si entre los delanteros, defensas y mediocampistas si hay alguno que no esté en su rol
  const posiciones = ["delantero", "defensa", "mediocampista"];
  
  for (const posicion of posiciones) {
    for (const jug of equipo.jugadores[posicion + 's']) {
      
      if (jug.rol !== posicion) {
        problemas.push(`${jug.nombre} tiene rol ${jug.rol} pero está jugando de ${posicion}`);
      }
        
      if (!jug.botines) {
        problemas.push(`${jug.nombre} no tiene botines!`);
      } else if (jug.botines.talle !== jug.talle) {
        problemas.push(`${jug.nombre} calza talle ${jug.talle} pero sus botines son ${jug.botines.talle}!`);
      }
    }
  }
  
  // Para el arquero:
  const arquero = equipo.jugadores.arquero;
  if (arquero.rol !== "arquero") {
    problemas.push(`${arquero.nombre} está de arquero pero es ${arquero.rol}`);
  }
  if (!arquero.botines) {
    problemas.push(`${arquero.nombre} no tiene botines!`);
  } else if (arquero.botines.talle !== arquero.talle) {
    problemas.push(`${arquero.nombre} calza talle ${arquero.talle} pero sus botines son ${arquero.botines.talle}!`);
  }
  
  return problemas;
}

function generarEquipo() {
  const bots = sample(botines, 5);
  const jugs = sample(jugadores, 5);
  
  jugs[0].botines = bots[0];
  jugs[1].botines = bots[1];
  jugs[2].botines = bots[2];
  jugs[3].botines = bots[3];
  jugs[4].botines = bots[4];
  
  return {
    nombre: "Generado",
    jugadores: {
      mediocampistas: [jugs[0], jugs[1]],
      delanteros: [jugs[2]],
      defensas: [jugs[3]],
      arquero: jugs[4]
    }
  };
}

function mostrarEquipo(equipo) {
  console.log('Equipo:', equipo.nombre);
  console.log('Jugadores:');
  console.log('- Delanteros:');
  for (const jug of equipo.jugadores.delanteros) {
    console.log(`  - ${jug.nombre} con botines ${jug.botines.nombre}`);
  }
  console.log('- Mediocampistas:');
  for (const jug of equipo.jugadores.mediocampistas) {
    console.log(`  - ${jug.nombre} con botines ${jug.botines.nombre}`);
  }
  console.log('- Defensas:');
  for (const jug of equipo.jugadores.defensas) {
    console.log(`  - ${jug.nombre} con botines ${jug.botines.nombre}`);
  }
  console.log('- Arquero:');
  console.log(`  - ${equipo.jugadores.arquero.nombre} con botines ${equipo.jugadores.arquero.botines.nombre}`);
}

function evaluarCalidad(equipo) {
  const pje = puntajeEquipo(equipo);
  if (pje < 20) {
    return 'malo';
  }
  if (pje >= 20 && pje < 30) {
    return 'medio';
  }
  if (pje >= 30) {
    return 'bueno';
  }
}

// Exportar funciones si es necesario
export {
  puntajeJugador,
  puntajeEquipo,
  reportarProblemas,
  generarEquipo,
  mostrarEquipo,
  evaluarCalidad,
  losCampeones
};
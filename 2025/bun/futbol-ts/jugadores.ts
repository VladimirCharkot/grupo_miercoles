import type { Jugador } from './types.js';

export const riquelme: Jugador = {
  nombre: "Juan Román Riquelme",
  talle: "M",
  edad: 45,
  rol: "mediocampista",
};

export const messi: Jugador = {
  nombre: "Lionel Messi",
  talle: "S",
  edad: 36,
  rol: "delantero",
};

export const cristiano: Jugador = {
  nombre: "Cristiano Ronaldo",
  talle: "L",
  edad: 38,
  rol: "delantero",
};

export const montiel: Jugador = {
  nombre: "Gonzalo Montiel",
  talle: "M",
  edad: 26,
  rol: "defensa",
};

export const mbappe: Jugador = {
  nombre: "Kylian Mbappé",
  talle: "M",
  edad: 24,
  rol: "delantero",
};

export const pedri: Jugador = {
  nombre: "Pedri González",
  talle: "S",
  edad: 20,
  rol: "mediocampista",
};

export const pezzella: Jugador = {
  nombre: "Germán Pezzella",
  talle: "L",
  edad: 32,
  rol: "defensa",
};

// Arqueros
export const dibuMartinez: Jugador = {
  nombre: "Emiliano Martínez",
  talle: "L",
  edad: 31,
  rol: "arquero",
};

export const courtois: Jugador = {
  nombre: "Thibaut Courtois",
  talle: "XL",
  edad: 31,
  rol: "arquero",
};

// Defensas adicionales
export const marquinhos: Jugador = {
  nombre: "Marquinhos",
  talle: "M",
  edad: 29,
  rol: "defensa",
};

export const vanDijk: Jugador = {
  nombre: "Virgil van Dijk",
  talle: "XL",
  edad: 32,
  rol: "defensa",
};

// Mediocampistas adicionales
export const deBruyne: Jugador = {
  nombre: "Kevin De Bruyne",
  talle: "L",
  edad: 32,
  rol: "mediocampista",
};

export const modric: Jugador = {
  nombre: "Luka Modrić",
  talle: "S",
  edad: 38,
  rol: "mediocampista",
};

// Delanteros adicionales
export const haaland: Jugador = {
  nombre: "Erling Haaland",
  talle: "XL",
  edad: 23,
  rol: "delantero",
};

export const benzema: Jugador = {
  nombre: "Karim Benzema",
  talle: 'L',
  edad: 36,
  rol: "delantero",
};

export const jugadores: Jugador[] = [
  riquelme, messi, cristiano, montiel, mbappe, pedri, pezzella,
  dibuMartinez, courtois, marquinhos, vanDijk, deBruyne, modric,
  haaland, benzema
];
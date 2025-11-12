import type { Botines, Talle } from './types.js';

export const talles: Talle[] = ['S', 'M', 'L', 'XL'];
// Small
// Medium
// Large
// Extra large

const botinesNike: Botines = {
  nombre: "Nike Mercurial Vapor",
  talle: "M",
  precio: 150,
};

const botinesNike2: Botines = {
  nombre: "Nike Phantom GT",
  talle: "S",
  precio: 140,
};

const botinesPuma: Botines = {
  nombre: "Puma Future Z",
  talle: "L",
  precio: 120,
};

const botinesPuma2: Botines = {
  nombre: "Puma Ultra",
  talle: "S",
  precio: 110,
};

const botinesAdidas: Botines = {
  nombre: "Adidas Copa Sense",
  talle: "M",
  precio: 130,
};

const botinesAdidas2: Botines = {
  nombre: "Adidas Predator Edge",
  talle: "S",
  precio: 140,
};

// Más botines Nike
const botinesNike3: Botines = {
  nombre: "Nike Tiempo Legend",
  talle: "XL",
  precio: 160,
};

const botinesNike4: Botines = {
  nombre: "Nike Mercurial Superfly",
  talle: "L",
  precio: 180,
};

// Más botines Adidas
const botinesAdidas3: Botines = {
  nombre: "Adidas X Ghosted",
  talle: "XL",
  precio: 135,
};

const botinesAdidas4: Botines = {
  nombre: "Adidas Nemeziz",
  talle: "L",
  precio: 125,
};

// Más botines Puma
const botinesPuma3: Botines = {
  nombre: "Puma King Platinum",
  talle: "M",
  precio: 115,
};

const botinesPuma4: Botines = {
  nombre: "Puma One",
  talle: "XL",
  precio: 105,
};

// Otras marcas
const botinesUmbro: Botines = {
  nombre: "Umbro Velocita",
  talle: "S",
  precio: 90,
};

const botinesMizuno: Botines = {
  nombre: "Mizuno Morelia Neo",
  talle: "M",
  precio: 170,
};

const botinesNewBalance: Botines = {
  nombre: "New Balance Furon",
  talle: "L",
  precio: 100,
};

export const botines: Botines[] = [
  botinesNike, botinesPuma, botinesAdidas,
  botinesNike2, botinesPuma2, botinesAdidas2,
  botinesNike3, botinesNike4, botinesAdidas3,
  botinesAdidas4, botinesPuma3, botinesPuma4,
  botinesUmbro, botinesMizuno, botinesNewBalance
];
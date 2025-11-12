export type Talle = "S" | "M" | "L" | "XL"

export interface Botines {
  nombre: string;
  talle: Talle;
  precio: number;
}

export interface Jugador {
  nombre: string;
  talle: Talle;
  edad: number;
  rol: "delantero" | "defensa" | "mediocampista" | "arquero";
  botines?: Botines;
}

export interface Equipo {
  nombre: string;
  jugadores: {
    mediocampistas: Jugador[];
    delanteros: Jugador[];
    defensas: Jugador[];
    arquero: Jugador;
  };
}
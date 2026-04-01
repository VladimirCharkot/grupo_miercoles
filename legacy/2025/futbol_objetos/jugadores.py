from jugador import Jugador


riquelme = {
    "nombre": "Juan Román Riquelme",
    "talle": "M",
    "edad": 45,
    "rol": "mediocampista",
}

messi = {
    "nombre": "Lionel Messi",
    "talle": "S",
    "edad": 36,
    "rol": "delantero",
}

cristiano = {
    "nombre": "Cristiano Ronaldo",
    "talle": "L",
    "edad": 38,
    "rol": "delantero",
}

montiel = {
    "nombre": "Gonzalo Montiel",
    "talle": "M",
    "edad": 26,
    "rol": "defensa",
}

mbappe = {
    "nombre": "Kylian Mbappé",
    "talle": "M",
    "edad": 24,
    "rol": "delantero",
}

pedri = {
    "nombre": "Pedri González",
    "talle": "S",
    "edad": 20,
    "rol": "mediocampista",
}

pezzella = {
    "nombre": "Germán Pezzella",
    "talle": "L",
    "edad": 32,
    "rol": "defensa",
}

# Arqueros
dibu_martinez = {
   "nombre": "Emiliano Martínez",
   "talle": "L",
   "edad": 31,
   "rol": "arquero",
}

courtois = {
   "nombre": "Thibaut Courtois",
   "talle": "XL",
   "edad": 31,
   "rol": "arquero",
}

# Defensas adicionales
marquinhos = {
   "nombre": "Marquinhos",
   "talle": "M",
   "edad": 29,
   "rol": "defensa",
}

van_dijk = {
   "nombre": "Virgil van Dijk",
   "talle": "XL",
   "edad": 32,
   "rol": "defensa",
}

# Mediocampistas adicionales
de_bruyne = {
   "nombre": "Kevin De Bruyne",
   "talle": "L",
   "edad": 32,
   "rol": "mediocampista",
}

modric = {
   "nombre": "Luka Modrić",
   "talle": "S",
   "edad": 38,
   "rol": "mediocampista",
}

# Delanteros adicionales
haaland = {
   "nombre": "Erling Haaland",
   "talle": "XL",
   "edad": 23,
   "rol": "delantero",
}

benzema = {
   "nombre": "Karim Benzema",
   "talle": "L",
   "edad": 36,
   "rol": "delantero",
}

jugadores_diccionarios = [
  riquelme, messi, cristiano, montiel, mbappe, pedri, pezzella,
  dibu_martinez, courtois, marquinhos, van_dijk, de_bruyne, modric,
]

jugadores = []
for jug in jugadores_diccionarios:
  jugador = Jugador(jug['nombre'], jug['talle'], jug['edad'], jug['rol'])
  jugadores.append(jugador)

# TODO: Agregar estos a jugadores:
vla = Jugador('Vla', 42, 32, 'delantero')
ren = Jugador('Ren', 40, 15, 'defensa')
luki = Jugador('Luki', 37, 12, 'mediocampista')
jere = Jugador('Jere', 41, 30, 'arquero')

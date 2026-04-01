from math import comb
from random import randint, choice, sample
from efectos import celeste, italic, bold, naranja, reverse

nombres = [ "Ale", "Berta", "Ben", "Cami", "Dalia", "Edwin", "Fran", "Gene", "Hele", "Ina", "Jaz", "Kiro", "Lau", "Mar", "Noe", "Omar", "Pepa", "Quimey", "Rae", "Sasha", "Tilo", "Uma", "Valen", "Walt", "Xavi", "Yesa", "Zoe" ]

habilidades = ["circo", "danza", "programación", "guitarra", "piano", "ilustración", "dibujo", "cocina", "gimnasia", "jardinería", "patín", "artes marciales", "ciclismo", "acrobacia", "pintura"]

slots = 3

def personaAlAzar():
  persona = {
    "nombre": choice(nombres),
    "edad": randint(16, 40),
    "habilidades": sample(habilidades, slots),
    # "disgutos": sample(habilidades, 2)
  }
  return persona

def saludar(p):
  print(f'Hola, mi nombre es {celeste(bold(p["nombre"]))}, tengo {p["edad"]} años y mis habilidades son:')
  for h in p["habilidades"]:
    print("-", italic(h))

def compatibilidad(pj1, pj2):
  n = 0
  for h in pj1['habilidades']:
    if h in pj2['habilidades']:
      n = n + 1
  # print(f"La compatibilidad entre {pj1['nombre']} y {pj2['nombre']} es: {naranja(str(n))}")
  return n

def simulacion(escenarios_de_interes): 
  compatibles = 0
  total = 1000000

  for i in range(total):
    p1 = personaAlAzar()
    p2 = personaAlAzar()
    c = compatibilidad(p1, p2)
    if c in escenarios_de_interes: 
      compatibles += 1

  print(f'En {total} simulaciones, hubo {compatibles} casos de compatibilidad {escenarios_de_interes}')


combinaciones_posibles = comb(len(habilidades), slots)

print(f'Corriendo simulación 2 personas con {slots} slots y lista de {len(habilidades)} habilidades')
print(f'Cada personaje tiene {combinaciones_posibles} posibles combinaciones de habilidades')
print(f'En total hay {combinaciones_posibles ** 2} escenarios posibles')
print(f'')

# Simulamos buscando los casos en que haya solo una habilidad en común
simulacion([1])
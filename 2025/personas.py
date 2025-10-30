from random import randint, choice

nombres = [ "Ale", "Berta", "Ben", "Cami", "Dalia", "Edwin", "Fran", "Gene", "Hele", "Ina", "Jaz", "Kiro", "Lau", "Mar", "Noe", "Omar", "Pepa", "Quimey", "Rae", "Sasha", "Tilo", "Uma", "Valen", "Walt", "Xavi", "Yesa", "Zoe" ]

habilidades = ["circo", "danza", "programación", "guitarra", "piano", "ilustración", "dibujo", "cocina", "gimnasia", "jardinería", "patín", "artes marciales", "ciclismo", "acrobacia", "pintura"]

def personaAlAzar():
  habilidades_persona = []
  cantidad_habilidades = randint(3,7)
  for i in range(cantidad_habilidades):
    habilidades_persona += [choice(habilidades)]
  persona = {
    "nombre": choice(nombres),
    "edad": randint(16, 40),
    "habilidades": habilidades_persona
  }
  return persona

def saludar(p):
  print(f'Hola, mi nombre es {p["nombre"]}, tengo {p["edad"]} años y mis habilidades son:')
  for h in p["habilidades"]:
    print("-", h)

def compatibilidad(pj1, pj2):
  pass
  nombre1 = pj1['nombre']
  nombre2 = pj2['nombre']
  n = 0
  for h in pj1['habilidades']:
    if h in pj2['habilidades']:
      n = n + 1
  print(f"La compatibilidad entre {nombre1} y {nombre2} es: {n}")

for i in range(5):
  print()
  saludar(personaAlAzar())

p1 = personaAlAzar()
p2 = personaAlAzar()

print()
print("Las personas creadas son:")
print(p1)
print(p2)
compatibilidad(p1, p2)
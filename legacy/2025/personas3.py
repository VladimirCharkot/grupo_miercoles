import ollama
import json
from random import randint, choice, sample

nombres = [ "Ale", "Berta", "Ben", "Cami", "Dalia", "Edwin", "Fran", "Gene", "Hele", "Ina", "Jaz", "Kiro", "Lau", "Mar", "Noe", "Omar", "Pepa", "Quimey", "Rae", "Sasha", "Tilo", "Uma", "Valen", "Walt", "Xavi", "Yesa", "Zoe" ]

habilidades = ["circo", "danza", "programación", "guitarra", "piano", "ilustración", "dibujo", "cocina", "gimnasia", "jardinería", "patín", "artes marciales", "ciclismo", "acrobacia", "pintura"]

signos = ["aries", "tauro", "géminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio", "acuario", "piscis"]

slots = [4, 2, 3]

def personaAlAzar():
  a, b, c = slots
  muestra = sample(habilidades, sum(slots))
  persona = {
    "nombre": choice(nombres),
    "edad": randint(16, 40),
    "habilidades": muestra[:a],
    "desea": muestra[a:a+b],
    "detesta": muestra[a+b:],
    "signo": choice(signos)
  }
  return persona

def generarPerfil():
  p = personaAlAzar()

  prompt = open('prompt.txt', 'r').read()
  prompt = prompt\
    .replace('NOMBRE', p['nombre'])\
    .replace('EDAD', str(p['edad']))\
    .replace('HABILIDADES', ', '.join(p['habilidades']))\
    .replace('DESEA', ', '.join(p['desea']))\
    .replace('DETESTA', ', '.join(p['detesta']))\
    .replace('SIGNO', p['signo'])

  print(prompt)

  respuesta = ollama.generate(
      model='llama3.1',
      prompt=prompt
  )

  try:
      parsed_json = json.loads(respuesta['response'])
      with open(f'personas/{p["nombre"]}.json', 'w', encoding='utf-8') as f:
          json.dump(parsed_json, f, indent=2, ensure_ascii=False)
  except json.JSONDecodeError:
      print("Error: Ollama output is not valid JSON")
      print("Raw output:", respuesta['response'])

generarPerfil()
import json
import os
import time
from flask import Flask, render_template, jsonify, request
from data.football_api import get_tabla_de_posiciones, get_competiciones, get_equipos, get_equipo

app = Flask(__name__)

def cargar_jugadores():
  with open('data/jugadores.json', encoding='utf-8') as f:
    return json.load(f)
  
def cargar_botines():
   with open('data/botines.json', encoding='utf-8') as x:
      return json.load(x)

jugadores = cargar_jugadores()
botines = cargar_botines()

# Versión 1: el servidor convierte los datos a JSON y el JS los usa directamente
@app.route('/')
def inicio():
  return render_template('inicio.html', jugadores=jugadores)

@app.route('/competiciones')
def competiciones_render():
  cache = leer_cache(CACHE_COMPETICIONES)
  if cache:
    print('✅ Cache HIT: competiciones')
  else:
    print('❌ Cache MISS: competiciones')
    cache = get_competiciones()
    escribir_cache(CACHE_COMPETICIONES, cache)
  return render_template('competiciones.html', competiciones=cache['competitions'])

# Versión 2: el servidor solo renderiza los nombres, 
# el JS pide la info de detalles del jugador al servidor
@app.route('/jugadores')
def lista_jugadores():
  print(request.user_agent)
  talle = request.args.get('talle')
  if not talle: 
     return render_template('jugadores.html', jugadores=jugadores)
  
  print('En el query llegó el talle:', talle)
  
  # To do: Renderizar solo los jugadores del talle/edad que me pidan!
  elegidos = []
  for j in jugadores:
     if j['talle'] == talle:
        elegidos.append(j)
        print(f'se sumó al equipo {j['nombre']} de talle {j['talle']}')
  return render_template('jugadores.html', jugadores=elegidos)

@app.route('/botineslista')
def lista_botines_biblio():
  return render_template('botines.html', botines=botines )

@app.route(f'/botines')
def lista_botines():
  print(request.user_agent)
  talle = request.args.get('talle')
  if not talle: 
     return render_template('botines.html', botines = botines)
  
  print('En el query llegó el talle:', talle)

  elegidos = []
  for b in botines:
     if b['talle'] == talle:
        elegidos.append(b)
        print(f'Los botines {b['nombre']} de talle {b['talle']} de {b['precio']} fueron comprados')
  return render_template('botines.html', botines=elegidos)

@app.route('/jugadores/<nombre>')
def jugador(nombre):
    for j in jugadores:
       if j['nombre'] == nombre:
          return jsonify(j)

@app.route('/botines/<nombre>')
def botiness(nombre)                                  :
    for b in botines:
       if b['nombre'] == nombre:
          return jsonify(b)

@app.route('/jugador', methods=['GET'])
def formulario_jugador():
    return render_template('nuevo_jugador.html')

@app.route('/jugador', methods=['POST'])
def crear_jugador():
    datos = {
        'nombre': request.form.get('nombre'),
        'rol':    request.form.get('rol'),
        'edad':   int(request.form.get('edad')),
        'talle':  request.form.get('talle'),
    }
    jugadores.append(datos) # Guardamos el jugador en MEMORIA

    with open('data/jugadores.json',mode="w",encoding='utf-8') as x:
      json.dump(jugadores, x)
    
    # To do: guardar el jugador en el archivo JSON para que persista aunque se reinicie el servidor
    with open('data/jugadores.json',mode="w",encoding='utf-8') as x:
        json.dump(jugadores, x)
    return render_template('nuevo_jugador.html', mensaje=f"✅ Jugador agregado: {datos['nombre']}")

##########################################################

# Cache en archivo para las competiciones (la API tiene rate limit muy bajo)
CACHE_COMPETICIONES = 'data/cache_competiciones.json'

# Para los equipos la cache depende de la competición, así que el id_codigo
# forma parte del nombre del archivo (una cache por competición).
def cache_equipos(id_codigo):
    return f'data/cache_equipos_{id_codigo}.json'

# Tiempo de vida de la cache en segundos (por defecto 24 horas)
TTL_CACHE = 60 * 60 * 24

def leer_cache(nombre_archivo, ttl=TTL_CACHE):
    try:
        # Si el archivo es más viejo que el TTL, lo tratamos como inexistente
        antiguedad = time.time() - os.path.getmtime(nombre_archivo)
        if antiguedad > ttl:
            print('⌛ Cache vencida')
            return None
        with open(nombre_archivo, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('El archivo de cache todavía no existe')
        return None

def escribir_cache(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', encoding='utf-8') as f:
        json.dump(datos, f)

##########################################################

@app.route('/api/competiciones')
def competiciones():
    cache = leer_cache(CACHE_COMPETICIONES)
    if cache:
        print('✅ Cache HIT: competiciones')
        return jsonify(cache)

    print('❌ Cache MISS: competiciones')
    cache = get_competiciones()
    escribir_cache(CACHE_COMPETICIONES, cache)
    return jsonify(cache)
  

@app.route('/api/competiciones/<id_codigo>/equipos')
def equipos(id_codigo):
  archivo = cache_equipos(id_codigo)
  cache = leer_cache(archivo)
  if cache:
    print(f'✅ Cache HIT: equipos {id_codigo}')
    return jsonify(cache)

  print(f'❌ Cache MISS: equipos {id_codigo}')
  cache = get_equipos(id_codigo)
  escribir_cache(archivo, cache)
  return jsonify(cache)

# Versión render: misma lógica de cache pero devuelve el template
@app.route('/competiciones/<id_codigo>/equipos')
def equipos_render(id_codigo):
  archivo = cache_equipos(id_codigo)
  cache = leer_cache(archivo)
  if cache:
    print(f'✅ Cache HIT: equipos {id_codigo}')
  else:
    print(f'❌ Cache MISS: equipos {id_codigo}')
    cache = get_equipos(id_codigo)
    escribir_cache(archivo, cache)
  return render_template('equipos.html', competicion=cache['competition'], equipos=cache['teams'])


@app.route('/api/equipos/<id_equipo>')
def equipo(id_equipo):
    codigo = id_equipo = request.args.get('codigo')
    data = get_competiciones()
    if codigo == 'WC':
        for i in data["competitions"]:
            if i["code"] == codigo:
                 return jsonify(get_equipo(id_equipo))
@app.route('/api/posiciones')
def posiciones():
    return jsonify(get_tabla_de_posiciones('CL'))

#-----------------------------------------------------------------
def cargar_botines():
  with open('data/botines.json', encoding='utf-8') as f:
    return json.load(f)

botiness = cargar_botines()

@app.route('/botines')
def botines():
  return render_template('botines.html', botines=botiness)

@app.route('/botines/<int:indice>')
def botin(indice):
    return jsonify(botiness[indice])
#-----------------------------------------------------------------


if __name__ == '__main__':
    print('🚀 Servidor en http://localhost:3005')
    app.run(host='0.0.0.0', port=3005, debug=True)

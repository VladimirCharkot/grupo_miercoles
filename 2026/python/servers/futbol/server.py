import json
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
  return render_template('competiciones.html', competiciones=get_competiciones()['competitions'])

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

@app.route('/api/competiciones')
def competiciones():
    return jsonify(get_competiciones())

# @app.route('/api/competiciones/equipos')
# def equipos():
#    codigo = request.args.get('code')
#    elegido = []
#    for c in codigos:
#       if c['code'] == codigo:
#          elegido.append(c('code'))
#          print(f'Codigo = equipo{c}')
#    return jsonify(get_equipos(f'{elegido}')) # CL = Champions League

@app.route('/api/competiciones/<int:id_codigo>/equipos')
def equipos(id_codigo):
  return jsonify(get_equipos(id_codigo))


@app.route('/api/equipos/<int:id_equipo>')
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








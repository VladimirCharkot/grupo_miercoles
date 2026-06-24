### Nuestra DB inicial

import json

from flask import jsonify, render_template, request

### DB: 

def cargar_jugadores():
  with open('data/jugadores.json', encoding='utf-8') as f:
    return json.load(f)
  
def cargar_botines():
  with open('data/botines.json', encoding='utf-8') as x:
      return json.load(x)

jugadores = cargar_jugadores()
botines = cargar_botines()

### Rutas: 

def registrar_rutas_db_inicial(app):

  # Versión 1: el servidor convierte los datos a JSON y el JS los usa directamente
  @app.route('/')
  def inicio():
    return render_template('inicio.html', jugadores=jugadores)

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

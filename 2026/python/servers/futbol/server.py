import json
from flask import Flask, render_template, jsonify, request
from data.football_api import get_tabla_de_posiciones, get_competiciones, get_equipos, get_equipo

app = Flask(__name__)

def cargar_jugadores():
  with open('data/jugadores.json', encoding='utf-8') as f:
    return json.load(f)
  
jugadores = cargar_jugadores()

# Versión 1: el servidor convierte los datos a JSON y el JS los usa directamente
@app.route('/')
def inicio():
  return render_template('inicio.html', jugadores=jugadores)

@app.route('/competiciones')
def competiciones_render():
  return render_template('competiciones.html', competiciones=get_competiciones())

# Versión 2: el servidor solo renderiza los nombres, 
# el JS pide la info de detalles del jugador al servidor
@app.route('/jugadores')
def lista_jugadores():
  print(request.user_agent)
  talle2 = request.args.get('talle')
  edad2 = request.args.get('edadmax')  
  lista = []

  for i in jugadores:
     if edad2 and int(edad2) >= i["edad"] and  talle2 == i["talle"]:
      
        lista.append(i)
    
    
  print('En el query llegó el nombre:', lista)
#  if talle 
  # To do: Renderizar solo los jugadores del talle/edad que me pidan!
  
  return render_template('jugadores.html', jugadores=lista)
# Versión 2: el servidor solo renderiza los nombres, el JS pide la info al servidor

@app.route('/jugadores/<int:indice>')
def jugador(indice):
    return jsonify(jugadores[indice])

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

    # To do: guardar el jugador en el archivo JSON para que persista aunque se reinicie el servidor
    with open('data/jugadores.json',mode="w",encoding='utf-8') as x:
        json.dump(jugadores, x)
    return render_template('nuevo_jugador.html', mensaje=f"✅ Jugador agregado: {datos['nombre']}")

@app.route('/api/competiciones')
def competiciones():
    return jsonify(get_competiciones())

@app.route('/api/competiciones/equipos')
def equipos():
    return jsonify(get_equipos('CL')) # CL = Champions League

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








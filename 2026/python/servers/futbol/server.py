import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def cargar_jugadores():
  with open('data/jugadores.json', encoding='utf-8') as f:
    return json.load(f)
  
jugadores = cargar_jugadores()

# Versión 1: el servidor convierte los datos a JSON y el JS los usa directamente
@app.route('/')
def inicio():
  return render_template('inicio.html', jugadores=jugadores)

# Versión 2: el servidor solo renderiza los nombres, 
# el JS pide la info de detalles del jugador al servidor
@app.route('/jugadores')
def lista_jugadores():
  print('🔍 Solicitando jugadores con args:', request.args.to_dict())
  
  # To do: Renderizar solo los jugadores del talle que me pidan!
  
  return render_template('jugadores.html', jugadores=jugadores)

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

    return render_template('nuevo_jugador.html', mensaje=f"✅ Jugador agregado: {datos['nombre']}")

if __name__ == '__main__':
    print('🚀 Servidor en http://localhost:3005')
    app.run(port=3005, debug=True)

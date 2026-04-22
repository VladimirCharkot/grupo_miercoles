from flask import Flask, render_template, jsonify
from data.jugadores import jugadores

app = Flask(__name__)

# Versión 1: el servidor convierte los datos a JSON y el JS los usa directamente
@app.route('/')
def inicio():
  return render_template('inicio.html', jugadores=jugadores)

# Versión 2: el servidor solo renderiza los nombres, el JS pide la info al servidor
@app.route('/jugadores')
def lista_jugadores():
  return render_template('jugadores.html', jugadores=jugadores)

@app.route('/jugadores/<int:indice>')
def jugador(indice):
  return jsonify(jugadores[indice])

if __name__ == '__main__':
    print('🚀 Servidor en http://localhost:3005')
    app.run(port=3005, debug=True)

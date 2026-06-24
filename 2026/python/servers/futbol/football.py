from flask import jsonify, render_template, request
from data.football_api import get_competiciones, get_equipo, get_equipos, get_tabla_de_posiciones

def registrar_rutas_football_api(app):

  ### Renderizan HTML ###

  @app.route('/competiciones')
  def competiciones_render():
    datos = get_competiciones()
    return render_template('competiciones.html', competiciones=datos['competitions'])

  @app.route('/competiciones/<id_competicion>/equipos')
  def equipos_render(id_competicion):
    datos = get_equipos(id_competicion)
    return render_template('equipos.html', competicion=datos['competition'], equipos=datos['teams'])

  ### Devuelven JSON ###

  @app.route('/api/competiciones/<id_competicion>/equipos')
  def equipos(id_competicion):
    return jsonify(get_equipos(id_competicion))

  @app.route('/api/equipos/<id_equipo>')
  def equipo(id_equipo):
      id_equipo = request.args.get('codigo')
      if not id_equipo:
          return jsonify({'error': 'Falta el código del equipo'}), 400
      return jsonify(get_equipo(id_equipo))
                
  @app.route('/api/posiciones/<id_competicion>')
  def posiciones(id_competicion):
      return jsonify(get_tabla_de_posiciones(id_competicion))
    
  @app.route('/api/competiciones')
  def competiciones():
      return jsonify(get_competiciones())
    

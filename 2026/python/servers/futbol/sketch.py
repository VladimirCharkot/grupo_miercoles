### Ruta para el sketch de p5.js

from flask import render_template, request
from data.football_api import get_equipos

def registrar_rutas_sketch(app):

    @app.route('/sketch')
    def sketch():
      compe = request.args.get('competicion', 'WC')
      respuesta = get_equipos(compe)
      return render_template('sketch.html', data=respuesta)

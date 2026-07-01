import json
import os
import time
from flask import Flask, render_template, jsonify, request
from data.football_api import get_tabla_de_posiciones, get_competiciones, get_equipos, get_equipo
from minidb import registrar_rutas_db_inicial
from football import registrar_rutas_football_api
from sketch import registrar_rutas_sketch

app = Flask(__name__)

registrar_rutas_db_inicial(app)
registrar_rutas_football_api(app)
registrar_rutas_sketch(app)

if __name__ == '__main__':
    print('🚀 Servidor en http://localhost:3005')
    app.run(host='0.0.0.0', port=3005, debug=True)

from flask import Flask, request, redirect, render_template, jsonify
from datetime import datetime
from random import randint

app = Flask(__name__)

# Storage
visitas = []

# Template crudo
@app.route('/') 
def inicio():
    list_items = []
    for v in visitas:
      list_items.append(f'<li>#{v["numero"]}: {v["nombre"]} a las {v["hora"]}</li>')
  
    items = ''.join(list_items)
    
    return f'''
        <html>
          <head>
            <title>Servidor de Visitas</title>
            <style>
              body {{ font-family: Arial; max-width: 600px; margin: 50px auto; }}
              input, button {{ padding: 10px; margin: 5px; }}
            </style>
          </head>
          <body>
            <h1>Registro de Visitas</h1>
            <form action="/registrar" method="GET">
              <input type="text" name="nombre" placeholder="Tu nombre" required>
              <button type="submit">Registrarme</button>
            </form>
            <h2>Visitas recientes:</h2>
            <ul>{items}</ul>
          </body>
        </html>
    '''

# Template jinja2
@app.route('/inicio')
def inicio_template():
    return render_template('inicio.html', visitas=visitas)

# Routing
@app.route('/usuario/<nombre>')
def perfil(nombre):
    return f'Hola {nombre}'

@app.route('/registrar')
def registrar():
    # Request args
    nombre = request.args.get('nombre', 'Anónimo')
    visita = {
        'numero': len(visitas) + 1,
        'nombre': nombre,
        'hora': datetime.now().strftime('%H:%M:%S')
    }
    visitas.append(visita)
    print(f'✅ Nueva visita: {nombre}')
    return redirect('/')

@app.route('/interactivo')
def interactivo():
    return render_template('interactivo.html')

# POST
@app.route('/random', methods=['POST'])
def random():
    # JSON
    return jsonify({ 'dado': randint(1, 6) })

if __name__ == '__main__':
    print('🚀 Servidor en http://localhost:3003')
    print('Abre el navegador y registra visitas!')
    app.run(port=3003, debug=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import os
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])    # Indicamos la ruta y los métodos
def webhook():                              # que aceptamos

    # Lee el json de la entrada y lo convierte en dic
    post = request.get_json(silent=True, force=True)

    respuesta = ""

    # Extraemos el nombre de la acción que será el nombre que pongamos a la función que le dará respuesta
    f = post["result"]["action"]

    # Para dar respuesta solo nos importa la información contenida en 'result'
    q = post["result"]["parameter"]
    
    return f,q

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000)
    
    

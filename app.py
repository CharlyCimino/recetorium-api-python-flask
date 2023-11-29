from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Habilitar CORS para todos los dominios en todas las rutas
CORS(app) # https://developer.mozilla.org/es/docs/Web/HTTP/CORS



from routes import ingredientes_routes
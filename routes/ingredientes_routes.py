from app import app
from flask import send_from_directory
from controllers.ingredientes_controller_hardcode import *

# Configurar la carpeta estática para imágenes
app.config['FOLDER_IMG_INGREDIENTES'] = 'public/img/ingredientes'

@app.route('/api/ingredientes/img/<filename>')
def enviar_imagen(filename):
    return send_from_directory(app.config['FOLDER_IMG_INGREDIENTES'], filename)

# Obtener todos los ingredientes
app.get('/api/ingredientes')(obtener_ingredientes)

# Obtener un ingrediente por ID
app.get('/api/ingredientes/<int:id>')(obtener_ingrediente)

# Crear un nuevo ingrediente
app.post('/api/ingredientes')(crear_ingrediente)

# Actualizar un ingrediente por ID
app.put('/api/ingredientes/<int:id>')(actualizar_ingrediente)

# Eliminar un ingrediente por ID
app.delete('/api/ingredientes/<int:id>')(eliminar_ingrediente)
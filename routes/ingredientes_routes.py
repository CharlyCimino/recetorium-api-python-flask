from app import app
from controllers.ingredientes_controller import *

# Obtener todos los ingredientes
app.route('/api/ingredientes', methods=['GET'])(obtener_ingredientes)

# Obtener un ingrediente por ID
app.route('/api/ingredientes/<int:id>', methods=['GET'])(obtener_ingrediente)

# Crear un nuevo ingrediente
app.route('/api/ingredientes', methods=['POST'])(crear_ingrediente)

# Actualizar un ingrediente por ID
app.route('/api/ingredientes/<int:id>', methods=['PUT'])(actualizar_ingrediente)

# Eliminar un ingrediente por ID
app.route('/api/ingredientes/<int:id>', methods=['DELETE'])(eliminar_ingrediente)
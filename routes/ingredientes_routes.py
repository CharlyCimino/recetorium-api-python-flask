from app import app
from controllers.ingredientes_controller_hardcode import *

# Establecer la ruta lógica del servidor que aloja las imágenes de los ingredientes
app.config['PATH_IMG_INGREDIENTES'] = 'api/ingredientes/img'

# Obtener todos los ingredientes
app.get("/api/ingredientes")(obtener_ingredientes)

# Obtener un ingrediente por ID
app.get("/api/ingredientes/<int:id>")(obtener_ingrediente)

# Obtener imagen de ingrediente por ID
app.get(f"/{app.config['PATH_IMG_INGREDIENTES']}/<filename>")(obtener_img_ingrediente_por_id)

# Crear un nuevo ingrediente
app.post("/api/ingredientes")(crear_ingrediente)

# Actualizar un ingrediente por ID
app.put("/api/ingredientes/<int:id>")(actualizar_ingrediente)

# Eliminar un ingrediente por ID
app.delete("/api/ingredientes/<int:id>")(eliminar_ingrediente)
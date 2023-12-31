from models.ingredientes_hard_code import lista_de_ingredientes, next_id
from flask import jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app
import os

# Establecer la carpeta pública del servidor que aloja las imágenes de los ingredientes
app.config['FOLDER_IMG_INGREDIENTES'] = 'public/img/ingredientes'

def obtener_ingredientes():
    return jsonify({'ingredientes': lista_de_ingredientes})

def obtener_ingrediente(id):
    ingrediente = get_ingrediente_by_id(id)
    if ingrediente:
        return jsonify({'ingrediente': ingrediente})
    else:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404

def obtener_img_ingrediente_por_id(filename):
    return send_from_directory(app.config['FOLDER_IMG_INGREDIENTES'], filename)

def crear_ingrediente():
    id = next_id()
    nombre = request.form['nombre']
    foto = request.files['foto']
    color = request.form['color']
    print(request.url)

    # Toma el nombre del archivo original como entrada y devuelve un nombre de archivo seguro para su almacenamiento.
    nombre_imagen = secure_filename(foto.filename)
    # Separa el nombre del archivo de su extensión, considerando el punto como separador.
    nombre_base, extension = os.path.splitext(nombre_imagen)
    # Guarda la imagen con el nombre asociado a su ID.
    nombre_imagen = f"ing_{id}{extension}"
    foto.save(os.path.join(app.config['FOLDER_IMG_INGREDIENTES'], nombre_imagen))
    nuevo_ingrediente = {
        "id": id,
        "nombre": nombre,
        "foto": f"/{app.config['PATH_IMG_INGREDIENTES']}/{nombre_imagen}",
        "color": color
    }
    lista_de_ingredientes.append(nuevo_ingrediente)
    return jsonify({'ingrediente': nuevo_ingrediente}), 201

def actualizar_ingrediente(id):
    ingrediente = get_ingrediente_by_id(id)
    if ingrediente:
        data = request.get_json()
        ingrediente.update(data)
        return jsonify({'ingrediente': ingrediente})
    else:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    
def eliminar_ingrediente(id):
    global lista_de_ingredientes
    ingrediente_eliminado = get_ingrediente_by_id(id)    
    if ingrediente_eliminado:
        lista_de_ingredientes = [i for i in lista_de_ingredientes if i['id'] != id]
        return jsonify({'mensaje': 'Ingrediente eliminado exitosamente', 'ingrediente_eliminado': ingrediente_eliminado})
    else:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    

def get_ingrediente_by_id(id):
    return next((ing for ing in lista_de_ingredientes if ing['id'] == id), None)
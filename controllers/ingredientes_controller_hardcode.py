from models.ingredientes_hard_code import lista_de_ingredientes
from flask import jsonify, request
from werkzeug.utils import secure_filename
from app import app
import os

def obtener_ingredientes():
    return jsonify({'ingredientes': lista_de_ingredientes})

def obtener_ingrediente(id):
    ingrediente = get_ingrediente_by_id(id)
    if ingrediente:
        return jsonify({'ingrediente': ingrediente})
    else:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404

def crear_ingrediente():
    id = len(lista_de_ingredientes) + 1
    nombre = request.form['nombre']
    foto = request.files['foto']
    color = request.form['color']

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
        "foto": nombre_imagen,
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
    global ingredientes
    ingrediente_eliminado = get_ingrediente_by_id(id)    
    if ingrediente_eliminado:
        ingredientes = [i for i in lista_de_ingredientes if i['id'] != id]
        return jsonify({'mensaje': 'Ingrediente eliminado exitosamente', 'ingrediente_eliminado': ingrediente_eliminado})
    else:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    

def get_ingrediente_by_id(id):
    return next((ing for ing in lista_de_ingredientes if ing['id'] == id), None)
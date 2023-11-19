from models.ingredientes_hard_code import lista_de_ingredientes
from flask import jsonify, request

def obtener_ingredientes():
    return jsonify({'ingredientes': lista_de_ingredientes})

def obtener_ingrediente(id):
    ingrediente = next((i for i in lista_de_ingredientes if i['id'] == id), None)
    if ingrediente:
        return jsonify({'ingrediente': ingrediente})
    else:
        return jsonify({'mensaje': 'Ingrediente no encontrado'}), 404
    
def crear_ingrediente():
    data = request.get_json()
    nuevo_ingrediente = {
        'id': len(lista_de_ingredientes) + 1,
        'nombre': data['nombre'],
        'rutaDeLaFoto': data['rutaDeLaFoto'],
        'colorHEX': data['colorHEX']
    }
    lista_de_ingredientes.append(nuevo_ingrediente)
    return jsonify({'ingrediente': nuevo_ingrediente}), 201

def actualizar_ingrediente(id):
    ingrediente = next((i for i in lista_de_ingredientes if i['id'] == id), None)
    if ingrediente:
        data = request.get_json()
        ingrediente.update(data)
        return jsonify({'ingrediente': ingrediente})
    else:
        return jsonify({'mensaje': 'Ingrediente no encontrado'}), 404
    
def eliminar_ingrediente(id):
    global ingredientes
    ingredientes = [i for i in lista_de_ingredientes if i['id'] != id]
    return jsonify({'mensaje': 'Ingrediente eliminado exitosamente'})
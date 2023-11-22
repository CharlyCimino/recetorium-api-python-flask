from models.ingredientes_hard_code import lista_de_ingredientes
from flask import jsonify, request

def obtener_ingredientes():
    return jsonify({'ingredientes': lista_de_ingredientes})

def obtener_ingrediente(id):
    ingrediente = get_ingrediente_by_id(id)
    if ingrediente:
        return jsonify({'ingrediente': ingrediente})
    else:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404

def crear_ingrediente():
    data = request.get_json()
    print(data)
    nuevo_ingrediente = {
        'id': len(lista_de_ingredientes) + 1,
        'nombre': data["nombre"],
        'foto': data["foto"],
        'color': data["color"]
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
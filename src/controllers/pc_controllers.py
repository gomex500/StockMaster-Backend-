from turtle import st
from flask import request, jsonify
from bson import ObjectId

###controlador insertar pc
def insertar_pc(collections):
    try:
        data = request.json
        id = collections.insert_one(data)
        return jsonify({'id':str(id)})
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status = 400
        return response

###controlador mostrar pc
def obtener_pc(collections):
    try:
        users = []
        for doc in collections.find():
            user = doc
            user['_id'] = str(doc['_id'])
            users.append(user)

        return jsonify(users)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

###actualizar pc
def actualizar_pc(collections, id):
    try:
        data = request.json
        result = collections.update_one({'_id': ObjectId(id)}, {'$set': data})
        return jsonify({'message':'Pc Actualizada'})
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status = 400
        return response

#controlador eliminar usuario
def eliminar_pc(collections, id):
    try:
        collections.delete_one({'_id': ObjectId(id)})
        return jsonify({'mensaje': 'PC eliminada'})
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

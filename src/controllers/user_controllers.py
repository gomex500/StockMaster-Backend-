from flask import request, jsonify
from src.models.user_models import UserModel
from bson import ObjectId
import json
import bcrypt

#funcion para vilidar si el correo existe
def validacion_email(coll, email):
    doc = coll.find_one({'email': email})
    if doc:
        return True
    return False

#controlador insertar usuario
def insertar_usuario(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)

        # Verificar si el correo electrónico ya existe
        if validacion_email(collections, user_instance.email):
            response = jsonify({"message": "El correo electrónico ya está en uso"})
            response.status_code = 400
            return response

        #encriptando password
        password = user_instance.password.encode('utf-8')
        salt = bcrypt.gensalt()
        passEncriptado = bcrypt.hashpw(password, salt)
        user_instance.password = passEncriptado.decode('utf-8')

        #insertando password y usuario a la db
        id = collections.insert_one(user_instance.__dict__).inserted_id
        user_data = {
            "nombre": user_instance.nombre,
            "email": user_instance.email,
            "password": user_instance.password
        }
        return jsonify({'id':str(id)})
    except:
        response = jsonify({"menssage":"error de registro"})
        response.status = 400
        return response


#controlador mostrar usuarios
def obtener_usuarios(collections):
    try:
        users = []
        for doc in collections.find():
            user = UserModel(doc).__dict__
            user['_id'] = str(doc['_id'])
            # Evitar agregar la contraseña a la lista de usuarios
            user.pop('password', None)
            users.append(user)

        return jsonify(users)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar usuario
def obtener_usuario(collections, id):
    try:
        doc = collections.find_one({'_id': ObjectId(id)})
        user_data = UserModel(doc).__dict__
        user_data['_id'] = str(doc['_id'])
        return jsonify(user_data)
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

#controlador eliminar usuario
def eliminar_usuario(collections, id):
    try:
        collections.delete_one({'_id': ObjectId(id)})
        return jsonify({'mensaje': 'Usuario eliminado'})
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response
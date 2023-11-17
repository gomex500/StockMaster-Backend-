from flask import request, jsonify
from src.models.user_models import UserModel
from bson import ObjectId
import json
import bcrypt

#funcion para vilidar si el correo existe
def validacion_username(coll, username):
    doc = coll.find_one({'username': username})
    if doc:
        return True
    return False

#validar si el password existe
def validar_password(coll, password):
    passEncriptado = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    doc = coll.find_one({'password': passEncriptado})
    if doc:
        return True
    return False

#controlador insertar usuario
def insertar_usuario(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)

        # Verificar si el correo electrónico ya existe
        if validacion_username(collections, user_instance.username):
            response = jsonify({"message": "El user name ya está en uso"})
            response.status_code = 400
            return response

        #encriptando password
        password = user_instance.password.encode('utf-8')
        salt = bcrypt.gensalt()
        passEncriptado = bcrypt.hashpw(password, salt)
        user_instance.password = passEncriptado.decode('utf-8')

        #insertando password y usuario a la db
        id = collections.insert_one(user_instance.__dict__).inserted_id
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

#controllador de logeo de usuarios
def login(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)

        # Validar si el correo electrónico existe
        if not validacion_username(collections, user_instance.username):
            response = jsonify({"message": "El user name no existe"})
            response.status_code = 401
            return response

        # Obtener el documento del usuario
        user_doc = collections.find_one({'username': user_instance.username})

        # Validar la contraseña
        if not bcrypt.checkpw(user_instance.password.encode('utf-8'), user_doc['password'].encode('utf-8')):
            response = jsonify({"message": "La contraseña no es válida"})
            response.status_code = 401
            return response

        return jsonify({'id': str(user_doc['_id'])})
    except Exception as e:
        print(str(e))
        response = jsonify({"message": "Error de inicio de sesión"})
        response.status_code = 400
        return response
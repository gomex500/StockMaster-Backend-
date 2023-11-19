from flask import Blueprint
from src.config.conexion import collections
from src.controllers.user_controllers import (
    insertar_usuario,
    obtener_usuarios,
    obtener_usuario,
    eliminar_usuario,
    login,
    obtener_username,
    actualizar_usuario
)

#inicializando rutas de usuario
user_routes = Blueprint('user_routes', __name__)

#ruta crear usuario
@user_routes.route('/users', methods=['POST'])
def insertar_usuario_ruta():
    return insertar_usuario(collections('usuarios'))

#ruta de logeo de usuario
@user_routes.route('/login', methods=['POST'])
def login_route():
    return login(collections('usuarios'))

#ruta mostrar usuarios
@user_routes.route('/users', methods=['GET'])
def obtener_usuarios_ruta():
    return obtener_usuarios(collections('usuarios'))

#ruta mostrar usuario
@user_routes.route('/user/<id>', methods=['GET'])
def obtener_usuario_ruta(id):
    return obtener_usuario(collections('usuarios'), id)

#ruta eliminar usuario
@user_routes.route('/user/<id>', methods=['DELETE'])
def eliminar_usuario_ruta(id):
    return eliminar_usuario(collections('usuarios'), id)

#ruta mostrar usuario por el correo
@user_routes.route('/username/<username>', methods=['GET'])
def obtener_username_ruta(username):
    return obtener_username(collections('usuarios'), username)

#ruta actualizar usuario
@user_routes.route('/user/<id>', methods=['PUT'])
def actualizar_usuario_ruta(id):
    return actualizar_usuario(collections('usuarios'), id)
from crypt import methods
from flask import Blueprint
from src.config.conexion import collections
from src.controllers.pc_controllers import (
    insertar_pc,
    obtener_pc,
    actualizar_pc,
    eliminar_pc
)

##inicializando rutas de las pc
pc_routes = Blueprint('pc_routes', __name__)

@pc_routes.route('/pc', methods=['POST'])
def insertar_pc_ruta():
    return insertar_pc(collections('pc'))

##
@pc_routes.route('/pc', methods=["GET"])
def obtener_pc_ruta():
    return obtener_pc(collections('pc'))

#ruta actualizar pc
@pc_routes.route('/pc/<id>', methods=['PUT'])
def actualizar_pc_ruta(id):
    return actualizar_pc(collections('pc'), id)

#ruta eliminar pc
@pc_routes.route('/pc/<id>', methods=['DELETE'])
def eliminar_pc_ruta(id):
    return eliminar_pc(collections('pc'), id)
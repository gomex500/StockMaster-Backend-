from flask import Blueprint

#inicializando ruta
home = Blueprint('home', __name__)

#ruta inicial
@home.route('/')
def index():
    return '<h1>welcome to api StockMaster</h1>'
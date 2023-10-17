from http import client
from pymongo import MongoClient
from src.config.config import MONGO_URI

#inicializando conexion con mongo
client = MongoClient(MONGO_URI)
db = client['stockmaster']

#funcio apar obtener una collection
def collections(collection):
    collection = db[collection]
    return collection
from datetime import datetime

#modelo de objeto usuario
class UserModel:
    def __init__(self, data):
        self.nombre = data.get('nombre', '')
        self.username = data.get('username', '')
        self.rol = data.get('rol', 0)
        self.password = data.get('password', '')
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())
from flask import Flask
from flask_cors import CORS
from src.routes.home import home
from src.routes.user_routes import user_routes
from src.routes.pc_routes import pc_routes
from src.config.config import DEBUG, PORT

app = Flask(__name__)

CORS(app)

app.register_blueprint(home)
app.register_blueprint(user_routes)
app.register_blueprint(pc_routes)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)


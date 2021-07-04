from flask import Blueprint
# controlador
from controllers.UserController import index

# el controlador de ruta
user_bp = Blueprint('user_bp', __name__)

# ruta get de index.
user_bp.route('/', methods=['GET'])(index)
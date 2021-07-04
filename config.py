import os

SECRET_KEY = os.urandom(32)

# Tomar la carpeta donde se ejecuta el script
basedir = os.path.abspath(os.path.dirname(__file__))

# Debug mode
DEBUG = True

# Conectar a base de datos
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir+'/db.sqlite3')

# Apagar los eventos de error de SQL-Alchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
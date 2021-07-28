from flask import Flask, render_template
# Migramos la base
from flask_migrate import Migrate 

# Modelo de user
from flask_sqlalchemy import SQLAlchemy
# la ruta de blue print
from routes.user_bp import user_bp

db = SQLAlchemy()
# app y configuración
app = Flask(__name__)
app.config.from_object('config')

# Iniciamos app
db.init_app(app)
# Migramos datos
# migrate = Migrate(app, db)
db.create_all(app=app)

# Registramos la ruta
app.register_blueprint(user_bp, url_prefix='/usuarios')

# Principal
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run()
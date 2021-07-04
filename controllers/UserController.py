from flask import jsonify
# models
from models.User import User
# db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Ruta de get
def index():
    # q = User.query.all()
    # print(q)
    # q = User(name='pedro',age='25',address='mexico')
    # db.session.add(q)
    # db.session.commit()
    return jsonify({'msg':'Hola user'})
from flask_sqlalchemy import SQLAlchemy
from ..app import db

class User(db.Model):
    __tablename__ = 'users'    
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String(120))
    address = db.Column(db.String(120))
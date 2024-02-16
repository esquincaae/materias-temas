# app/models/tema.py
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Tema(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    estatus = db.Column(db.String(10), default="activo")
    identificador_mayoria = db.Column(db.String(255))
    materia_id = db.Column(db.String(36), db.ForeignKey('materia.uuid'), nullable=False)

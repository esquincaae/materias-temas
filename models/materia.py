# app/models/materia.py
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Materia(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    carrera = db.Column(db.String(255), nullable=False)
    estatus = db.Column(db.String(10), default="activo")
    temas = db.relationship('Tema', backref='materia', lazy=True)

    def __init__(self, nombre, carrera):
        self.uuid = str(uuid.uuid4())
        self.nombre = nombre
        self.carrera = carrera

    def desactivar(self):
        self.estatus = "inactivo"

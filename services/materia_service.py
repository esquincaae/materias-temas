# app/services/materia_service.py
from models.materia import Materia, db
from models.tema import Tema

class MateriaService:
    def crear_materia(self, nombre, carrera):
        # Validaciones (puedes agregar más según tus necesidades)
        if not nombre or not carrera:
            raise ValueError("Nombre y carrera son obligatorios para crear una materia.")

        # Verificar si ya existe una materia con el mismo nombre en la misma carrera
        materia_existente = Materia.query.filter_by(nombre=nombre, carrera=carrera).first()
        if materia_existente:
            raise ValueError("Ya existe una materia con el mismo nombre en la misma carrera.")

        # Crear la materia y agregarla a la base de datos
        nueva_materia = Materia(nombre=nombre, carrera=carrera)
        db.session.add(nueva_materia)
        db.session.commit()

        return nueva_materia

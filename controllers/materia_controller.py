#controllers/materia_controller.py
from flask import Blueprint, jsonify, request
from services.materia_service import MateriaService

materia_controller = Blueprint('materia_controller', __name__)
materia_service = MateriaService()

@materia_controller.route('/materia', methods=['POST'])
def crear_materia():
    data = request.get_json()
    nombre = data.get('nombre')
    carrera = data.get('carrera')

    try:
        nueva_materia = materia_service.crear_materia(nombre, carrera)
        return jsonify({"uuid": str(nueva_materia.uuid), "nombre": nueva_materia.nombre, "carrera": nueva_materia.carrera, "estatus": nueva_materia.estatus})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

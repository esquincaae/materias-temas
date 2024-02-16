# run.py
from flask import Flask
from infrastructure.db import db
from models.materia import Materia
from models.tema import Tema
from controllers.materia_controller import materia_controller

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:contraseña@localhost/nombredelabasededatos'  # Reemplaza con tus credenciales
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Registrar blueprints
app.register_blueprint(materia_controller)

# Configuración de modelos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

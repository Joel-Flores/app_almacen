#importando dependencias
from flask import Flask
import os

#importacion de blueprint
from .authentication import auth
from .store import store

#creacion de la app
def create_app():
    app = Flask(__name__)
    #configuracion de la app con ingreso de datos desde consola
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('FLASK_SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE') 
    )
    
    #importacion de la base de datos
    from app import db
    db.init_app(app)
    
    #agregar el blueprint a la aplicacion
    app.register_blueprint(auth)
    app.register_blueprint(store)
    
    return app
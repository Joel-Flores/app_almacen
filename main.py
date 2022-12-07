#importando dependencias de la app
from app import create_app
from app.funtion_views import view_materials_in_store
#importando herramientas de flask
from flask import render_template, jsonify

app = create_app()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/')
def index():
    json = view_materials_in_store()
    return render_template('index.html')
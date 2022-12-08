#importar la el blueprint de store
from . import tech

#importacion de frameworks
from flask import render_template, redirect, url_for, request, session, flash, g
from werkzeug.exceptions import abort

#importacion de decorado para protejer rutas
from app.authentication.views import login_required
 
#importacion de la conexion a la base de datos
from app.db import get_db

@tech.route('/')
@login_required
def index():
    return render_template('store/index.html')

#importar la el blueprint de store
from . import tech
#importar logica para los routes
from ..authentication.data_technical import data_technical
from .data_view import data_type_works, code_list
from .code_entry import code_entry
from .works_form import works_form
from .materials_form import materials_form
from .retired_claim_team import retired_claim_team
from .updt_serial_tech import updt_serial_tech

#importacion de frameworks
from flask import render_template, redirect, url_for, flash, g, session
from werkzeug.exceptions import abort

#importacion de decorado para protejer rutas
from app.authentication.routes import login_required

@tech.before_request
@login_required
def before_request():
    g.username = session.get('username')
    g.materials =  session.get('materials')
    g.serials =  session.get('serials')
    g.equipments =  session.get('equipment')
    g.equipments_all = session.get('equipments_all')
    g.code_for_retired = session.get('code_for_retired')
@tech.route('/')
def index():
    json = dict()
    json = data_type_works(json)
    json = code_list(json)
    return render_template('tech/index.html', **json)

@tech.route('/new_code', methods = ['POST'])
def new_code():
    json = dict()
    json = code_entry(json)
    return render_template('tech/form_work_order.html', **json)

@tech.route('/new_order', methods = ['POST'])
def new_order():
    works_form()
    return render_template('tech/complete_materials_the_code.html')

@tech.route('/material_code', methods = ['POST'])
def material_code():
    message = materials_form()
    if message == 'datos incorrectos.' :
        flash(message)
        return abort(404)
    flash(message)
    data_technical()
    return redirect(url_for('tech.index'))

@tech.route('/new_serial', methods = ['POST'])
def new_serial():
    json = retired_claim_team()
    return render_template('tech/form_new_serial.html', **json)

@tech.route('/update_serial_tech', methods = ['POST'])
def update_serial_tech():
    message = updt_serial_tech()
    flash(message)
    return redirect(url_for('tech.index'))
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
from .removal_order import removal_order
from .details_code import details_code

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

#vista general para el tecnico
@tech.route('/')
def index():
    json = data_type_works()
    return render_template('tech/index.html', **json)

#rutas para instalacion, reclamos, retiros; registro de codigos
@tech.route('/new_code', methods = ['POST'])
def new_code():
    json, message, error = code_entry()
    flash(message)
    if error is True:
        return render_template('tech/withdrawal_record/withdrawal_form.html', **json)
    return render_template('tech/registration_of_installations_and_claims/form_work_order.html', **json)
#agregar orden de trabajo instalacion y reclamos
@tech.route('/new_order', methods = ['POST'])
def new_order():
    message = works_form()
    flash(message)
    return render_template('tech/registration_of_installations_and_claims/complete_materials_the_code.html')

#actualizar materiales de la ot y del tecnico
@tech.route('/material_code', methods = ['POST'])
def material_code():
    message = materials_form()
    if message == 'datos incorrectos.' :
        flash(message)
        return abort(404)
    flash(message)
    data_technical()
    return redirect(url_for('tech.index'))

#registro de equipo retirado de reclamos
@tech.route('/new_serial', methods = ['POST'])
def new_serial():
    json = retired_claim_team()
    if json == 'codigo ya registrado':
        flash(json)
        return redirect(url_for('tech.index'))
    return render_template('tech/withdrawal_record/form_new_serial.html', **json)

#agregando datos al equipo subido y (cortejando a la ot)pendiente
@tech.route('/update_serial_tech', methods = ['POST'])
def update_serial_tech():
    message = updt_serial_tech()
    flash(message)
    return redirect(url_for('tech.index'))

#agregar orden de trabajo para retiros
@tech.route('/removal_orders', methods = ['POST'])
def removal_orders():
    message = removal_order()
    flash(message)
    return render_template('tech/withdrawal_record/complete_materials_the_code.html')

#detalles de los codigos ejecutados
@tech.route('/details/<int:id>')
def details(id):
    
    json = details_code(id)
    return render_template('tech/details_codes/details_code.html', json = json)
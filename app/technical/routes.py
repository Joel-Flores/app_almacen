#importar la el blueprint de store
from . import tech
from .materials_form import materials_form
from .data_technical import data_technical, data_json, data_type_works, code_list
from .code_entry import code_entry
from .works_form import works_form

#importacion de frameworks
from flask import render_template, redirect, url_for, request, session, flash, g
from werkzeug.exceptions import abort

#importacion de decorado para protejer rutas
from app.authentication.views import login_required


@tech.route('/')
@login_required
def index():
    data_technical()
    return redirect(url_for('tech.view'))

@tech.route('/view')
@login_required
def view():
    json = data_json()
    json = data_type_works(json)
    json = code_list(json)
    return render_template('tech/index.html', **json)

@tech.route('/new_code', methods = ['POST'])
@login_required
def new_code():
    json = data_json()
    json = code_entry(json)
    return render_template('tech/form_work_order.html', **json)

@tech.route('/new_order', methods = ['POST'])
@login_required
def new_order():
    works_form()
    json = data_json()
    return render_template('tech/complete_materials_the_code.html', **json)

@tech.route('/material_code', methods = ['POST'])
@login_required
def material_code():
    message = materials_form()
    if message == 'datos incorrectos.' :
        flash(message)
        return abort(404)
    flash(message)
    return redirect(url_for('tech.index'))
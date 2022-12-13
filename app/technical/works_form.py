from flask import request, flash, redirect, url_for, g, session
from app.db import get_db

#extraer informacion del formulario de ordenes
def form_works():
    db, c = get_db()
    query = 'SELECT id FROM codes WHERE code = %s'
    c.execute(query,[session.get('code')])
    session['code'] = c.fetchone()
    try:
        form = dict()
        order = list()
        serial = list()
        
        order_one = request.form['order_one']
        serial_one = request.form['serial_one']
        if order_one != '' and serial_one != '':
            order.append(int(order_one))
            serial.append(int(serial_one))
        
        order_two = request.form['order_two']
        serial_two = request.form['serial_two']
        if order_two != '' and serial_two != '':
            order.append(int(order_two))
            serial.append(int(serial_two))
        
        order_three = request.form['order_three']
        serial_three = request.form['serial_three']
        if order_three != '' and serial_three != '':
            order.append(int(order_three))
            serial.append(int(serial_three))
            
        order_four = request.form['order_four']
        serial_four = request.form['serial_four']
        if order_four != '' and serial_four != '':
            order.append(int(order_four))
            serial.append(int(serial_four))
            
        order_five = request.form['order_five']
        serial_five = request.form['serial_five']
        if order_five != '' and serial_five != '':
            order.append(int(order_five))
            serial.append(int(serial_five))
            
        order_six = request.form['order_six']
        serial_six = request.form['serial_six']
        if order_six != '' and serial_six != '':
            order.append(int(order_six))
            serial.append(int(serial_six))

        if order == [] and serial == []:
            error = 'no se lleno todos los datos necesarios!'
            return error
        
        if session.get('type_works_id') == 12 and serial == [1]:
            form['orders'] = order
            form['serials'] = None
        
        else:
            form['orders'] = order
            form['serials'] = serial
        return form
    except:
        error = 'error al llenar el formulario'
        return error
    
    
def confirm_order_(orders):
    db, c = get_db()

    error = None
    query = 'SELECT work_order FROM work_orders WHERE work_order = %s AND technical_id = %s'
    
    for order in orders:
        c.execute(query, [order, g.user['id']])
        if c.fetchone() is not None:
            error = f'la orden {order} se encuentra registrado'
            return error
        
    query = 'INSERT INTO materials (user_id) VALUES (%s)'
    c.execute(query,[g.user['id']])
    db.commit()
    
    query = 'SELECT id FROM materials WHERE user_id = %s ORDER BY id DESC LIMIT 1'
    c.execute(query, [g.user['id']])
    materials_id = c.fetchone()
    session['materials_id'] = materials_id['id']

#verificado y update de la orden_series
def update_work(form):
    db, c = get_db()

    code_id = session.get('code')
    orders_id = form['orders']
    serials_id = form['serials']
    materials_id = session.get('materials_id')
    
    query = 'INSERT INTO  work_orders(work_order, serials_id, materials_id, code_id, technical_id) VALUES (%s, %s, %s, %s,%s)'
    for i in range(len(orders_id)):
        c.execute(query, [orders_id[i], serials_id[i], materials_id, code_id['id'], g.user['id']])
        db.commit()
    message = 'ordenes subidas exitosamente'

    update_tech_equip(serials_id)
    return message

#eliminar los equipos usados en la tabla de technical_serial
def update_tech_equip(serials_id):
    db, c = get_db()
    query = 'DELETE FROM technical_serial WHERE serials_id = %s AND technical_id = %s'
    for id in serials_id:
        c.execute(query,[id, g.user['id']])
    db.commit()


def update_work_order(orders):
    db, c = get_db()

    code_id = session.get("code")
    materials_id = session.get('materials_id')
    
    query = 'INSERT INTO  work_orders(work_order, serials_id, materials_id, code_id, technical_id) VALUES (%s, %s, %s, %s,%s)'
    for i in range(len(orders)):
        c.execute(query, [orders[i], 1, materials_id, code_id['id'], g.user['id']])
        db.commit()
    message = 'ordenes subidas exitosamente'

    return message

#manejador de las funciones
def works_form():
    form = form_works()
    if type(form) == str:
        flash(form)
        return redirect(url_for('tech.index'))
    
    confirm_order_(form['orders'])
    
    if form['serials'] is not None:
        message = update_work(form)
        
    else:
        message = update_work_order(form['orders'])
    
    flash(message)
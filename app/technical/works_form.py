from flask import request, session, flash, redirect, url_for, g
from app.db import get_db
#extraer informacion del formulario de ordenes
def form_works():
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
        
        if order == [] or serial == []:
            error = 'no se lleno todos las datos necesarios!'
            return error
        
        form['orders'] = order
        form['serials'] = serial
        return form
    except:
        error = 'error al llenar el formulario'
        return error
    
#verificado y update de la orden_series
def update_work(form):
    db, c = get_db()
    
    user_id = session.get('user_id')
    code = session.get('code')
    
    query = 'SELECT id FROM codes WHERE code = %s'
    c.execute(query,[code])
    code_id = c.fetchone()
    code_id = code_id ['id']
    
    error = None
    
    query = 'SELECT work_order FROM work_orders WHERE work_order = %s'
    orders_id = form['orders']
    serials_id = form['serials']
    
    for order in orders_id:
        c.execute(query, [order])
        if c.fetchone() is not None:
            error = f'la orden {order} se encuentra registrado'
            return error
    
    if error is None:
        query = 'INSERT INTO  work_orders(work_order, serials_id, materials_id, code_id, technical_id) VALUES (%s, %s, %s, %s,%s)'
        for i in range(len(orders_id)):
            c.execute(query, [orders_id[i], serials_id[i], 1, code_id, user_id])
            db.commit()
        message = 'ordenes subidas exitosamente'
        
    query = 'SELECT MAX(id) FROM work_orders WHERE technical_id = %s'
    c.execute(query,[user_id])
    work_order_id = c.fetchone()
    work_order_id = work_order_id['MAX(id)']
    session['work_order_id'] = work_order_id
    
    update_tech_equip(serials_id)
    return message

#eliminar los equipos usados en la tabla de technical_serial
def update_tech_equip(serials_id):
    db, c = get_db()
    query = 'DELETE FROM technical_serial WHERE serials_id = %s'
    for id in serials_id:
        c.execute(query,[id])
    db.commit()
    
def works_form():
    form = form_works()
    if type(form) == str:
        flash(form)
        return redirect(url_for('tech.index'))
    message = update_work(form)
    flash(message)
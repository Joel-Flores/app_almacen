from flask import request, flash, redirect, url_for, g, session
from app.db import get_db

# controlar el formulario
def form_works():
    try:
        form = dict()
        order = list()
        serial = list()
        equipment_id = list()
        
        order_one = request.form['order_one']
        serial_one = request.form['serial_one']
        equipment_id_one = request.form['equipment_id_one']
        if order_one != '' and serial_one != '':
            order.append(int(order_one))
            serial.append(serial_one.upper())
            equipment_id.append(int(equipment_id_one))
        
        order_two = request.form['order_two']
        serial_two = request.form['serial_two']
        equipment_id_two = request.form['equipment_id_two']
        if order_two != '' and serial_two != '':
            order.append(int(order_two))
            serial.append(serial_two.upper())
            equipment_id.append(int(equipment_id_two))
        
        order_three = request.form['order_three']
        serial_three = request.form['serial_three']
        equipment_id_three = request.form['equipment_id_three']
        if order_three != '' and serial_three != '':
            order.append(int(order_three))
            serial.append(serial_three.upper())
            equipment_id.append(int(equipment_id_three))
        
        order_four = request.form['order_four']
        serial_four = request.form['serial_four']
        equipment_id_four = request.form['equipment_id_four']
        if order_four != '' and serial_four != '':
            order.append(int(order_four))
            serial.append(serial_four.upper())
            equipment_id.append(int(equipment_id_four))
        
        order_five = request.form['order_five']
        serial_five = request.form['serial_five']
        equipment_id_five = request.form['equipment_id_five']
        if order_five != '' and serial_five != '':
            order.append(int(order_five))
            serial.append(serial_five.upper())
            equipment_id.append(int(equipment_id_five))
        
        order_six = request.form['order_six']
        serial_six = request.form['serial_six']
        equipment_id_six = request.form['equipment_id_six']
        if order_six != '' and serial_six != '':
            order.append(int(order_six))
            serial.append(serial_six.upper()) 
            equipment_id.append(int(equipment_id_six))
        
        if order == [] and serial == []:
            error = 'no se lleno todos los datos necesarios!'
            return error
        
        else:
            form['orders'] = order
            form['serials'] = serial
            form['equipment_id'] = equipment_id
            return form
    except:        
        error = 'error al llenar el formulario'
        return error


def confirm_order_(orders):
    error = None
    
    db, c = get_db()
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
    return error

def update_work(form):
    db, c = get_db()

    code_id = session.get('code')
    orders_id = form['orders']
    cm_macs = form['serials']
    equipments_id = form['equipment_id']
    materials_id = session.get('materials_id')
    
    #ingresar las ordenes de retiros
    query = 'INSERT INTO  work_orders(work_order, serials_id, materials_id, code_id, technical_id) VALUES (%s, %s, %s, %s,%s)'
    for i in range(len(orders_id)):
        c.execute(query, [orders_id[i], 1, materials_id, code_id['id'], g.user['id']])
        db.commit()
    
    #extraer ids de las ordenes subidas
    orders_id = len(orders_id)
    query = 'SELECT id FROM work_orders WHERE technical_id = %s AND code_id = %s ORDER BY id DESC LIMIT %s;'
    c.execute(query, [g.user['id'], code_id['id'], orders_id])
    work_orders_id = c.fetchall()
    
    
    #subir los series retiradas
    reverse = len(work_orders_id) -1 
    query = 'INSERT INTO serials_tech (cm_mac, equipment_id, code_id, work_orders_id, user_id) VALUES (%s, %s, %s, %s, %s)'
    for i in range(len(cm_macs)):
        c.execute(query, [cm_macs[i], equipments_id[i], code_id['id'], work_orders_id[reverse]['id'], g.user['id']])
        reverse -= 1
        db.commit()
    
    message = 'ordenes subidas exitosamente'

    return message

def removal_order():
    form = form_works()
    if type(form) == 'str':
        flash(form)
        return redirect(url_for('tech.index'))
    
    error = confirm_order_(form['orders'])
    if error is None:
        message = update_work(form)
        return message    
    
    flash(error)
    return redirect(url_for('tech.index'))
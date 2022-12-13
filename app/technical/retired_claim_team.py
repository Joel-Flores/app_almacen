from flask import request, g, session
from app.db import get_db

def retired_claim_team():
    new_serial = request.form['new_serial']
    new_serial = new_serial.upper()
    
    #controlar que la serie ya este retirada
    db, c =  get_db()
    c.execute('SELECT cm_mac, cm_mac_two, card_number FROM serials_tech;')
    codes_all = c.fetchall()
    
    error = None
    for code in codes_all:
        if new_serial == code['cm_mac']:
            error = 'codigo ya registrado'
        elif new_serial == code['cm_mac_two']:
            error = 'codigo ya registrado'
        elif new_serial == code['card_number']:
            error = 'codigo ya registrado'
            
    #ingresar datos en caso de no tener un error en el control
    if error is None:
        code_id = int(request.form['code_id'])
        
        query = 'SELECT id FROM work_orders WHERE technical_id = %s AND code_id = %s ORDER BY id DESC;'
        c.execute(query, [g.user['id'], code_id])
        work_order_id = c.fetchone()
        equipment_id = int(request.form['equipment_id'])
        
        json = dict()
        session['code_id_for_retired'] = code_id 
        json['new_serial'] = new_serial
        
        query = 'INSERT INTO serials_tech (cm_mac, equipment_id, code_id, work_orders_id, user_id) VALUES (%s, %s, %s, %s, %s)'
        c.execute(query, [new_serial, equipment_id, code_id, work_order_id['id'], g.user['id']])
        db.commit()
        return json
    return error
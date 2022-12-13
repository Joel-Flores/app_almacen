from flask import request, g, session
from app.db import get_db
def retired_claim_team():
    new_serial = int(request.form['new_serial'])
    equipment_id = int(request.form['equipment_id'])
    code_id = int(request.form['code_id'])
    
    db, c =  get_db()
    c.execute('SELECT cm_mac, cm_mac_two, card_number FROM serials_tech;')
    codes_all = c.fetchall()
    
    error = None
    for code in codes_all:
        if new_serial == int(code['cm_mac']):
            error = 'codigo ya registrado'
        elif new_serial == int(code['cm_mac_two']):
            error = 'codigo ya registrado'
        elif new_serial == int(code['card_number']):
            error = 'codigo ya registrado'
            
    if error is None:
        json = dict()
        session['code_id_for_retired'] = code_id 
        session['serial'] = new_serial
        
        json['new_serial'] = new_serial
        
        query = 'INSERT INTO serials_tech(cm_mac, equipment_id, code_id, user_id) VALUES (%s, %s, %s, %s)'
        c.execute(query, [new_serial, equipment_id, code_id, g.user['id']])
        db.commit()
        return json
    return error
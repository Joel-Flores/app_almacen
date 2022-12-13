from flask import request, g, session
from app.db import get_db
def retired_claim_team():
    json = dict()
    new_serial = int(request.form['new_serial'])
    equipment_id = int(request.form['equipment_id'])
    code_id = int(request.form['code_id'])
    session['code_id_for_retired'] = code_id 
    
    json['new_serial'] = new_serial
    session['serial'] = new_serial
    
    db, c =  get_db()
    query = 'INSERT INTO serials_tech(cm_mac, equipment_id, code_id, user_id) VALUES (%s, %s, %s, %s)'
    c.execute(query, [new_serial, equipment_id, code_id, g.user['id']])
    db.commit()
    
    return json
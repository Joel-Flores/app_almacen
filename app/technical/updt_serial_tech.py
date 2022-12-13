from flask import request,g, session
from app.db import get_db

def updt_serial_tech():
    cm_mac_two = request.form['cm_mac_two']
    card_number = request.form['card_number']
    
    db, c = get_db()
    
    if cm_mac_two == '' and card_number == '':
        return 'Equipo subido.'
    
    else:
        query = '''UPDATE serials_tech 
        SET cm_mac_two = %s,
        card_number = %s 
        WHERE code_id = %s and user_id = %s'''
        code_id = session.get('code_id_for_retired')
        c.execute(query, [cm_mac_two, card_number, code_id, g.user['id']])
        db.commit()
        
        return 'Equipo completo subido'
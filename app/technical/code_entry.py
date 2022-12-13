from flask import request, flash, g, session
from app.db import get_db


# crear nuevo registro de codigo ejecutado
def _code_entry(code, type_works_id):
    db, c = get_db()
    query = 'SELECT code FROM codes WHERE code = %s'
    c.execute(query, [code])
    
    if c.fetchone() is not None:
        return 'Codigo ya registrado, ingrese nuevas orden(es) de trabajo.'
    
    query = 'INSERT INTO codes(code, type_works_id, technical_id) VALUES (%s, %s, %s)'
    c.execute(query,[code, type_works_id, g.user['id']])
    db.commit()
    return 'Nuevo codigo registrado, ingrese nueva(s) orden(es) de trabajo'


def code_entry(json):
    code = int(request.form['new_code'])
    type_works_id = int(request.form['type_works_id'])
    
    session['code'] = code
    session['type_works_id'] = type_works_id
    
    json['code'] = code
    json['ots'] = [
        {'order' : 'order_one','serial' : 'serial_one'},
        {'order' : 'order_two','serial' : 'serial_two'},
        {'order' : 'order_three','serial' : 'serial_three'},
        {'order' : 'order_four','serial' : 'serial_four'},
        {'order' : 'order_five','serial' : 'serial_five'},
        {'order' : 'order_six','serial' : 'serial_six'}
    ]
    
    message = _code_entry(code,type_works_id)
    flash(message)
    return json
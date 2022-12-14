from flask import request, flash, g, session
from app.db import get_db


# crear nuevo registro de codigo ejecutado
def _code_entry(code, type_works_id):
    db, c = get_db()
    query = 'SELECT code FROM codes WHERE code = %s'
    c.execute(query, [code])
    error = False
    message = c.fetchone()
    #si no tiene codigo lo registramos y comprobamos si es un retiro, ingresamos el codigo a la base de datos
    if message is None:
        query = 'INSERT INTO codes(code,technical_id) VALUES (%s, %s)'
        c.execute(query,[code, g.user['id']])
        db.commit()
        if int(type_works_id) == 13:
            error = True
            message = 'Nuevo codigo registrado, ingrese nueva(s) orden(es) y equipos retirados'
        else:
            message = 'Nuevo codigo registrado, ingrese nueva(s) orden(es) de trabajo'
    else:
        message = 'Codigo registrado'
    
    #traemos el codigo registrado por el usuario
    query = 'SELECT id FROM codes WHERE code = %s AND technical_id = %s ORDER BY id DESC LIMIT 1;'
    c.execute(query, [code, g.user['id']])
    session['code'] = c.fetchone()
    code_id =session.get("code")
    
    #ingresamos el tipo de trabajo a la base de datos
    query = 'INSERT INTO code_type_works(code_id, type_works_id) VALUES (%s, %s)'
    c.execute(query, [code_id['id'], type_works_id])
    db.commit()
    
    
    
    return message, error
    
#manejador de las funciones
def code_entry():
    json = dict()
    code = int(request.form['new_code'])
    type_works_id = int(request.form['type_works_id'])
    
    session['type_works_id'] = type_works_id
    
    json['code'] = code
    json['ots'] = [
        {'order' : 'order_one','serial' : 'serial_one', 'equipment_id':'equipment_id_one'},
        {'order' : 'order_two','serial' : 'serial_two', 'equipment_id':'equipment_id_two'},
        {'order' : 'order_three','serial' : 'serial_three', 'equipment_id':'equipment_id_three'},
        {'order' : 'order_four','serial' : 'serial_four', 'equipment_id':'equipment_id_four'},
        {'order' : 'order_five','serial' : 'serial_five', 'equipment_id':'equipment_id_five'},
        {'order' : 'order_six','serial' : 'serial_six', 'equipment_id':'equipment_id_six'}
    ]
    
    message, error = _code_entry(code,type_works_id)
    return json, message, error
#importacion de frameworks
from flask import g
#importacion de la base de datos
from app.db import get_db

# lista de los trabajos a realizar por el tecnico
def data_type_works(json):
    db, c = get_db()
    c.execute('SELECT id, type_work FROM type_works')
    json['type_works'] = c.fetchall()
    return json

#lista de codigos ejecutados por el tecnico
def code_list(json):
    user = g.user['id']
    db, c = get_db()
    query = 'SELECT id FROM codes WHERE technical_id = %s;'
    c.execute(query, [user])
    codes_id = c.fetchall()
    
    query = '''SELECT c.code, t.type_work, w.created_in, count(*) as ots
        FROM type_works AS t
        INNER JOIN codes as c
        ON t.id = c.type_works_id
        INNER JOIN work_orders AS w
        ON c.id = w.code_id
        WHERE w.technical_id = %s AND c.id = %s;
    '''
    codes_list = list()
    for code_id in codes_id:
        c.execute(query,[user, code_id['id']])
        codes_list.append(c.fetchone())
        
    json['code_list'] = codes_list
    return json

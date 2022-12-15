#importacion de frameworks
from flask import g
#importacion de la base de datos
from app.db import get_db

#lista de codigos ejecutados por el tecnico
def code_list(json):
    user = g.user['id']
    db, c = get_db()
    query = '''SELECT ct.code_id, ct.type_works_id 
		FROM code_type_works AS ct
		INNER JOIN codes AS c
		ON c.id = ct.code_id
		WHERE c.technical_id = %s ORDER BY ct.id DESC LIMIT 10;
    '''
    c.execute(query, [user])
    ids = c.fetchall()
    
    query = '''SELECT ct.id, c.code, t.type_work, ct.created_in, COUNT(*) AS ots
		FROM work_orders AS w
        LEFT JOIN codes AS c
        ON c.id = w.code_id
        INNER JOIN code_type_works AS ct
		ON c.id = ct.code_id
        INNER JOIN type_works AS t
        ON t.id = ct.type_works_id
        WHERE c.technical_id = %s AND w.code_id = %s  AND ct.type_works_id = %s;
    '''
    codes_list = list()
    for id in ids:
        c.execute(query,[user, id['code_id'], id['type_works_id']])
        codes_list.append(c.fetchone())
        
    json['code_list'] = codes_list
    return json

# lista de los trabajos a realizar por el tecnico
def data_type_works():
    json = dict()
    db, c = get_db()
    c.execute('SELECT id, type_work FROM type_works')
    json['type_works'] = c.fetchall()
    json = code_list(json)
    return json

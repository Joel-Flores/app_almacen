from flask import g, session
from app.db import get_db

# traer el nombre, cargo del usuario
def data_user(user_id):
    db, c = get_db()
    query = 'SELECT staff_id FROM user_staff WHERE user_id = %s'
    c.execute(query,[user_id])
    staff_id = c.fetchone()
    query = '''SELECT s.user_name, s.user_lastname, p.position
    FROM staff AS s
    JOIN positions AS p
    ON s.positions_id = p.id
    WHERE s.id = %s
    '''
    c.execute(query,[staff_id['staff_id']])
    return c.fetchone()

# traer materiales asignados al usuario
def data_materials(user_id):
    db, c = get_db()
    query = '''SELECT m.cable_hdmi, m.cable_rca, m.spliter_two, m.spliter_three, m.remote_control, m.connector_int, m.connector_ext, m.power_supply, m.q_span, m.cp_black, m.sp_black, m.sp_withe, m.satellite_dish, m.lnb
    FROM technical_material AS tm
    JOIN materials AS m
    ON tm.materials_id = m.id
    WHERE tm.technical_id = %s
    '''
    c.execute(query,[user_id])
    return c.fetchone()

#traer equipos asignados al tecnico
def data_equipments(user_id):
    db, c = get_db()
    c.execute('SELECT id FROM equipment;')
    equipments_id = c.fetchall()
    equipments = list()
    for  data in equipments_id:
        query = '''SELECT e.name, COUNT(*) AS caunt
        FROM equipment AS e
        INNER JOIN serials as s
        ON e.id = s.equipment_id
        INNER JOIN technical_serial AS ts
        ON ts.serials_id = s.id
        WHERE technical_id = %s and e.id = %s;
    '''
        c.execute(query,[user_id, data['id']])
        equipments.append(c.fetchone())
    return equipments

#traer equipos asignados al tecnico
def data_serials(user_id):
    db, c = get_db()
    query = 'SELECT serials_id FROM technical_serial WHERE technical_id = %s'
    c.execute(query,[user_id])
    serials_id = c.fetchall()
    serials = list()
    query = '''SELECT s.id, s.cm_mac, e.name
        FROM serials as s
        JOIN equipment as e
        ON s.equipment_id = e.id
        WHERE s.id = %s
        '''
    for id in serials_id:
        c.execute(query,[id['serials_id']])
        serials.append(c.fetchone())
    return serials

def data_type_works(json):
    db, c = get_db()
    c.execute('SELECT id, type_work FROM type_works')
    json['type_works'] = c.fetchall()
    return json

def code_list(json):
    user_id = session.get('user_id')
    db, c = get_db()
    query = '''SELECT c.code, t.type_work, w.create_at
        FROM type_works AS t
        INNER JOIN codes as c
        ON t.id = c.type_works_id
        INNER JOIN work_orders AS w
        ON c.id = w.code_id
        WHERE technical_id = %s;
    '''
    c.execute(query,[user_id])
    json['code_list'] = c.fetchall()
    return json


# enviar el json de datos 
def data_json():
    json = dict()
    json['username'] = session.get('username')
    json['materials'] = session.get('materials')
    json['equipments'] = session.get('equipments')
    json['serials'] = session.get('serials')
    return json

def data_technical():
    user_id = session.get('user_id')
    usermane = data_user(user_id)
    materials = data_materials(user_id)
    serials = data_serials(user_id)
    equipment = data_equipments(user_id)
    #code = data_codes(user_id)
    
    session['username'] = usermane
    session['materials'] = materials
    session['serials'] = serials
    session['equipments'] = equipment


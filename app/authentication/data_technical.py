from flask import g, session
from app.db import get_db

# traer el nombre, cargo del usuario
def data_user(user_id):
    db, c = get_db()
    
    query = '''SELECT s.user_name, s.user_lastname, p.position
    FROM staff AS s
    INNER JOIN positions AS p
    ON s.positions_id = p.id
    INNER JOIN user_staff AS us
    ON s.id = us.staff_id
    WHERE us.user_id = %s
    '''
    c.execute(query,[user_id])
    return c.fetchone()

# traer materiales asignados al usuario
def data_materials(user_id):
    db, c = get_db()
    query = '''SELECT m.cable_hdmi, m.cable_rca, m.spliter_two, m.spliter_three, m.remote_control, m.connector_int, m.connector_ext, m.power_supply, m.q_span, m.cp_black, m.sp_black, m.sp_withe, m.satellite_dish, m.lnb
    FROM technical_material AS tm
    INNER JOIN materials AS m
    ON tm.materials_id = m.id
    WHERE tm.technical_id = %s AND m.user_id = %s
    '''
    c.execute(query,[user_id,user_id])
    return c.fetchone()

#traer equipos asignados al tecnico
def data_equipments(user_id):
    db, c = get_db()
    c.execute('SELECT id, name FROM equipment;')
    equipments_id = c.fetchall()
    session['equipments_all'] = equipments_id
    
    equipments = list()
    
    query = '''SELECT e.name, COUNT(*) AS caunt
        FROM equipment AS e
        INNER JOIN serials as s
        ON e.id = s.equipment_id
        INNER JOIN technical_serial AS ts
        ON ts.serials_id = s.id
        WHERE ts.technical_id = %s AND e.id = %s AND s.user_id = %s;
    '''
    for  id in equipments_id:
        c.execute(query,[user_id, id['id'], user_id])
        equipments.append(c.fetchone())
    return equipments

#traer equipos asignados al tecnico
def data_serials(user_id):
    db, c = get_db()
    
    query = 'SELECT id , code FROM codes WHERE technical_id = %s AND type_works_id = 12 ORDER BY id desc LIMIT 5;'
    c.execute(query, [user_id])
    session['code_for_retired'] = c.fetchall()
    
    query = 'SELECT serials_id FROM technical_serial WHERE technical_id = %s'
    c.execute(query,[user_id])
    serials_id = c.fetchall()
    
    serials = list()
    query = '''SELECT s.id, s.cm_mac, e.name
        FROM serials as s
        INNER JOIN equipment as e
        ON s.equipment_id = e.id
        WHERE s.id = %s AND s.user_id = %s;
        '''
    for id in serials_id:
        c.execute(query,[id['serials_id'],user_id])
        serials.append(c.fetchone())
        
    return serials

def data_technical():
    user_id = session.get('user_id')
    username = data_user(user_id)
    materials = data_materials(user_id)
    equipment = data_equipments(user_id)
    serials = data_serials(user_id)
    
    session['username'] = username
    session['materials'] = materials
    session['serials'] = serials
    session['equipment'] = equipment
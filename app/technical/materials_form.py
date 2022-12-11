# importacion de los frmanworks nacasarios 
from flask import g, session,request
from app.db import get_db
from datetime import datetime



#update de la orden_material
def _update_material_work(data_form):
    db, c = get_db()
    work_order_id = session.get('work_order_id')
    
    query = 'INSERT INTO materials(cable_hdmi, cable_rca, spliter_two, spliter_three, remote_control, connector_int, connector_ext, power_supply, q_span, cp_black, sp_black, sp_withe, satellite_dish, lnb) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    c.execute(query, data_form)
    db.commit()
    
    query = 'SELECT MAX(id) FROM materials'
    c.execute(query)
    materials_id = c.fetchone()
    materials_id = materials_id['MAX(id)']
    
    query = 'UPDATE work_orders SET materials_id = %s, create_at = %s WHERE id = %s;'
    c.execute(query, [materials_id, datetime.now(), work_order_id])
    db.commit()


#eliminar los materiales usados en el registro del tecnico
def _update_tech_material(data_form):
    db, c = get_db()
    user_id = session.get('user_id')
    materials = session.get('materials')
    new_data = list()
    
    for key in data_form:
        new_data.append(materials[key] - data_form[key])
    
    query = 'SELECT materials_id FROM technical_material WHERE technical_id = %s'
    c.execute(query,[user_id])
    materials_id = c.fetchone()
    
    new_data.append(materials_id['materials_id'])
    
    query = '''UPDATE materials
            SET cable_hdmi = %s,
            cable_rca = %s,
            spliter_two = %s,
            spliter_three = %s,
            remote_control = %s,
            connector_int = %s,
            connector_ext = %s,
            power_supply = %s,
            q_span = %s,
            cp_black = %s,
            sp_black = %s,
            sp_withe = %s,
            satellite_dish = %s,
            lnb = %s
            WHERE id = %s;'''
    c.execute(query, new_data)
    db.commit()



#limpiar datos y extraer los nombres de las campos de la tabla y guardarlos en una lista
def _name_materials(datas):
    name_materials = list()
    for data in datas:
        if data['Field'] != 'id':
            name_materials.append(data['Field'])
    return name_materials

#extraer datos del request y guardarlos en una lista
def _resquiest_form(datas):
    _list = list()
    _dict = dict()
    for name in datas:
        _dict[name] = request.form[name]
        _list.append(request.form[name])
    return _list, _dict

#convertir los datos de la lista a int 
def _values_int(_list, _dict):
    for i in range(len(_list)):
        if _list[i] == '':
            _list[i] = 0
        else:
            try:
                _list[i] = int(_list[i])
            except:
                 return 'datos incorrectos.' 
        
    for key in _dict:
        if _dict[key] == '':
             _dict[key] = 0
        else:
            try:
                _dict[key] = int(_dict[key])
            except:
                return 'datos incorrectos.' 
    return _list, _dict

# manejador del las funciones para la extraccion y namejo de datos
def materials_form():
    db, c = get_db()
    c.execute('SHOW COLUMNS FROM materials;')
    name_materials = _name_materials(c.fetchall())
    data_form_list, data_form_dict = _resquiest_form(name_materials)
    data_form_list, data_form_dict = _values_int(data_form_list, data_form_dict)
    _update_material_work(data_form_list)
    _update_tech_material(data_form_dict)
    return 'Codigo agregado exitosamente.'
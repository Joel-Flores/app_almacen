# importacion de los frmanworks nacasarios 
from flask import g, request,session, flash, redirect, url_for
from app.db import get_db
from datetime import datetime



#update de la orden_material
def _update_material_work(data_form):
    db, c = get_db()
    #agregamos a la lista el id_material de codigo y el tecnico que hizo la orden
    data_form.append(session.get('materials_id'))
    data_form.append(g.user['id'])
    
    query = '''UPDATE materials SET cable_hdmi = %s,
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
        WHERE id = %s AND user_id = %s;
    '''
    c.execute(query, data_form)
    db.commit()
    return 'Codigo agregado exitosamente.'

#eliminar los materiales usados en el registro del tecnico
def _update_tech_material(data_form):
    db, c = get_db()
    user_id = g.user['id']
    materials = session.get('materials')
    error = None
    new_data = list()
    
    #iterar entre los materiales y controlar que tengamos el material nesesario
    
    if session.get('type_works_id') != 13:
        for key in data_form:
            if materials[key] >= 0 and materials[key] - data_form[key] >= 0:
                new_data.append(materials[key] - data_form[key])
            else:
                error = 'No tienes los materiles suficientes, contactate con almacen'
                return error
    else:
        for key in data_form:
            new_data.append(materials[key] + data_form[key])
            
    #obtener el id de los materiales de tecnico y actualizar
    query = 'SELECT materials_id FROM technical_material WHERE technical_id = %s'
    c.execute(query,[user_id])
    materials_id = c.fetchone()
    
    new_data.append(materials_id['materials_id'])
    new_data.append(g.user['id'])
    
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
            WHERE id = %s AND user_id = %s;'''
    c.execute(query, new_data)
    db.commit()
    return error

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

#extraer datos del request y guardarlos en una lista y diccionario
def _resquiest_form(data):
    _list = list()
    _dict = dict()
    for name in data:
        _dict[name] = request.form[name]
        _list.append(request.form[name])
    return _list, _dict

#limpiar datos y extraer los nombres de las campos de la tabla y guardarlos en una lista
def _name_materials(datas):
    name_materials = list()
    for data in datas:
        if data['Field'] != 'id' and data['Field'] != 'user_id' and data['Field'] != 'created_in':
            name_materials.append(data['Field'])
    return name_materials

# manejador del las funciones para la extraccion y manejo de datos
def materials_form():
    db, c = get_db()
    c.execute('SHOW COLUMNS FROM materials;')
    name_materials = _name_materials(c.fetchall())
    data_form_list, data_form_dict = _resquiest_form(name_materials)
    data_form_list, data_form_dict = _values_int(data_form_list, data_form_dict)
    

    message = _update_tech_material(data_form_dict)
    #controlamos que la funcion nos diga si tiene o no material para asignarlo al codigo
    if message is None:
        message = _update_material_work(data_form_list)
        return message
    else:
        return message
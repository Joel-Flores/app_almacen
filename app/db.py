#importando frameworks
import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

#importando instruciones para la base de datos
from app.schema import instrutions
from app import insert
#funcion para llamar a la base de datos y al cursor
def get_db():
    if 'db' not in  g:
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary = True)
    return g.db, g.c

#funcion para cerrar la base de datos administrada por la app
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()



#cargar tablas a la base de datos
def init_db():
    db, c = get_db()
    
    for instruction in instrutions:
        c.execute(instruction)
    db.commit()

#cargar datos basicos a las tablas
def init_load():
    db, c = get_db()
     
    for instruction in insert.equipment:
        query = 'INSERT INTO equipment (name) VALUES(%s)'
        c.execute(query,[instruction])
    db.commit()
    
    query = 'INSERT INTO user(nickname, password, active) VALUES (%s, %s, %s)'
    password = 'joe'
    c.execute(query,['joe',generate_password_hash(password),1])
    db.commit()
   
    for instruction in insert.vm:
        query = 'INSERT INTO serials (cm_mac,equipment_id, user_id) VALUES(%s, %s, %s)'
        c.execute(query,[instruction,1,1])
    db.commit()
    
    for instruction in insert.arris:
        query = 'INSERT INTO serials (cm_mac,equipment_id, user_id) VALUES(%s, %s, %s)'
        c.execute(query,[instruction, 2, 1])
    db.commit()
    
    for instruction in insert.hitron:
        query = 'INSERT INTO serials (cm_mac,equipment_id, user_id) VALUES(%s, %s, %s)'
        c.execute(query,[instruction, 3, 1])
    db.commit()
    
    for instruction in insert.positions:
        query = 'INSERT INTO positions (position) VALUES(%s)'
        c.execute(query,[instruction])
    db.commit()
    
    for instruction in insert.staff:
        query = 'INSERT INTO staff (user_name, user_name_two, user_lastname, user_lastname_two, positions_id) VALUES(%s, %s, %s, %s, %s)'
        c.execute(query,instruction)
    db.commit()
    
    query = 'INSERT INTO user_staff(user_id, staff_id) VALUES (%s, %s)'
    c.execute(query,[1,1])
    db.commit()
    
    for instruction in insert.material:
        instruction.append(1)
        query = 'INSERT INTO materials (cable_hdmi, cable_rca, spliter_two, spliter_three, remote_control, connector_int, connector_ext, power_supply, q_span, cp_black, sp_black, sp_withe, user_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        c.execute(query,instruction)
    db.commit()
    
    query = 'INSERT INTO technical_material(technical_id, materials_id) VALUES (%s, %s)'
    c.execute(query,[1,2])
    db.commit()
    
    c.execute('SELECT id FROM serials')
    data = c.fetchall()
    for instruction in data:
        query = 'INSERT INTO technical_serial (technical_id, serials_id) VALUES(%s, %s)'
        c.execute(query,[1 ,instruction['id']])
    db.commit()
    
    for instruction in insert.type_works:
        query = 'INSERT INTO type_works(type_work) VALUES(%s)'
        c.execute(query, [instruction])
    db.commit()
    
#declarando nuevo comando para flask
@click.command(name = 'init-db')
@with_appcontext    
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')
    init_load()
    click.echo('base de datos actualizada')

#funcion para que la app se encargue de las ejecuciones
def init_app(app):
        app.teardown_appcontext(close_db)
        app.cli.add_command(init_db_command)
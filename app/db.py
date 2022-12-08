#importando frameworks
import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext

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
    for instruction in insert.vm:
        query = 'INSERT INTO serials (cm_mac,equipment_id) VALUES(%s,%s)'
        c.execute(query,[instruction,1])
    db.commit()
    for instruction in insert.arris:
        query = 'INSERT INTO serials (cm_mac,equipment_id) VALUES(%s,%s)'
        c.execute(query,[instruction,2])
    db.commit()
    for instruction in insert.hitron:
        query = 'INSERT INTO serials (cm_mac,equipment_id) VALUES(%s,%s)'
        c.execute(query,[instruction,3])
    db.commit()
    for instruction in insert.positions:
        query = 'INSERT INTO positions (position) VALUES(%s)'
        c.execute(query,[instruction])
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
from flask import request, session, g
from werkzeug.security import check_password_hash

from app.db import get_db


def init_session():
    db, c = get_db()
        
    username = request.form['username']
    password = request.form['password']
    error = None
        
    query = 'SELECT * FROM user WHERE nickname = %s'
    c.execute(query,[username])
    user = c.fetchone()
        
    if user is None:
        error = 'Usuario y/o Contraseña invalida'
    elif not check_password_hash(user['password'],password):
        error = 'Usuario y/o Contraseña invalida' 
    elif user['active'] == 0:
        error = 'Permiso Denegado'
        
    if error is None:
        session.clear()
        session['user_id'] = user['id']
        print('dentro')
        
        return 'Bienvenido'
    
    return error
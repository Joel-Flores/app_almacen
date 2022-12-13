from flask import request
from werkzeug.security import generate_password_hash

from app.db import get_db


def new_user():
    db, c = get_db()
        
    username = request.form['username']
    password = request.form['password']
    
    error = None
    query = 'SELECT id FROM user WHERE nickname = %s'
    c.execute(query,[username])
    
    if not username:
        error = 'usuario es requerido'
    elif not password:
        error = 'password es requerido'
    elif c.fetchone() is not None:
        error = f'usuario {username} se encuentra registrado'

    if error is None:
        query = 'INSERT INTO user (nickname, password, active) VALUES (%s,%s, %s)'
        password = generate_password_hash(password)
        c.execute(query,[username,password,1])
        db.commit()
            
        return 'Registrado Exitosamente'
    
    return error
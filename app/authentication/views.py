#importar la wel bp de auth
from . import auth

#importacion de frameworks
from flask import render_template, redirect, url_for, request, session, flash, g
import functools
from werkzeug.security import check_password_hash, generate_password_hash

#importacion de la conexion a la base de datos
from app.db import get_db

@auth.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        db, c = get_db()
        username = request.form['username']
        password = request.form['password']
        error = None
        query = 'SELECT id FROM user WHERE username = %s'
        c.execute(query,[username])
        if not username:
            error = 'usuario es requerido'
        elif not password:
            error = 'password es requerido'
        elif c.fetchone() is not None:
            error = f'usuario {username} se encuentra registrado'

        if error is None:
            query = 'INSERT INTO user (username, password) VALUES (%s,%s)'
            password = generate_password_hash(password)
            print(password)
            c.execute(query,[username,password])
            db.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    
    user_ip = session.get('user_ip')
    return render_template('auth/register.html', user_ip = user_ip)
    
@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        db, c = get_db()
        username = request.form['username']
        password = request.form['password']
        error = None
        query = 'SELECT * FROM user WHERE username = %s'
        c.execute(query,[username])
        user = c.fetchone()
        if user is None:
            error = 'Usuario y/o Contraseña invalida'
        elif not check_password_hash(user['password'],password):
            error = 'Usuario y/o Contraseña invalida'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('store.index'))
        flash(error)
        
    return render_template('auth/login.html')

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user= None
    else:
        db, c = get_db()
        query = 'SELECT * FROM user WHERE id = %s'
        c.execute(query,[user_id])
        g.user = c.fetchone
    
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Inicia sesion')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
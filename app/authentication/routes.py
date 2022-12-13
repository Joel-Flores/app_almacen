#importar la del bp de auth
from . import auth


#importacion de frameworks
from flask import render_template, redirect, url_for, request, session, flash, g
import functools

#importacion de la conexion a la base de datos
from app.db import get_db

from .new_user import new_user
from .init_session import init_session
from .data_technical import data_technical


@auth.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        flash(new_user())
        
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')
    
@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        flash(init_session())
        data_technical()
        return redirect(url_for('tech.index'))
        
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user= None
    else:
        db, c = get_db()
        query = 'SELECT * FROM user WHERE id = %s'
        c.execute(query,[user_id])
        g.user = c.fetchone()
    
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Inicia sesion')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
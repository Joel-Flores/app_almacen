#importar la del bp de auth
from . import auth

#importacion de frameworks
from flask import render_template, redirect, url_for, request, session, flash, g
import functools

from .new_user import new_user
from.init_session import init_session
from .check_user import user_in_g


@auth.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        flash(new_user())
    
    return render_template('auth/register.html')
    
@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        flash(init_session())
        
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@auth.before_app_request
def load_logged_in_user():
    user_in_g()
    
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Inicia sesion')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
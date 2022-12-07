#importando dependencias de la app
from app import create_app
from app.funtion_views import view_materials_in_store
#importando herramientas
from flask import render_template, request, make_response, redirect, session
import unittest

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)

@app.errorhandler(404)
def server_error(error):
    return render_template('500.html', error = error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/auth/register'))
    session['user_ip'] = user_ip
    return response
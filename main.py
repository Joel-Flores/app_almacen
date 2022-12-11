#importando dependencias de la app
from app import create_app
#importando herramientas
from flask import render_template, redirect, url_for
import unittest

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error = error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error = error)


@app.route('/')
def index():
    return redirect(url_for('auth.login'))
#importar la wel bp de store
from . import store

#importacion de frameworks
from flask import render_template, redirect, url_for, request, session, flash, g

#importacion de la conexion a la base de datos
from app.db import get_db

@store.route('/')
def index():
    return 'store'

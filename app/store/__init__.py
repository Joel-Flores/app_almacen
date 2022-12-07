from flask import Blueprint

store = Blueprint('store', __name__, url_prefix ='/store')

from . import views
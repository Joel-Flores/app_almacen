from flask import Blueprint

tech = Blueprint('tech', __name__, url_prefix ='/tech')

from . import routes
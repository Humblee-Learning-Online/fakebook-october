from flask import Blueprint

bp = Blueprint('shop', __name__, url_prefix='/shop')

from .import models, routes
from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix="/blog")

from . import routes, models
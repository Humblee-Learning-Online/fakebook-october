from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.blueprints.auth.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(email, password):
    u = User.query.filter_by(email=email).first()
    if u and u.check_password(password):
        return u

@token_auth.verify_token
def verify_token(token):
    return User.check_token(token) if token else None
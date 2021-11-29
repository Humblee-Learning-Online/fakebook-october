from .import bp as api
from flask import json, jsonify
from app.blueprints.auth.models import User
from .auth import token_auth

@api.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    """
    [GET] /api/users
    """
    # jsonify ONLY takes a list of dictionaries/a single dictionary
    return jsonify([u.to_dict() for u in User.query.all()])
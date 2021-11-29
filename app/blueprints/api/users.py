from flask import request, url_for, jsonify, abort
from .errors import bad_request
from .import bp as api
from .auth import token_auth
from app.blueprints.auth.models import User
from app import db

@api.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    return jsonify([i.to_dict() for i in User.query.all()])

@api.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@api.route('/users', methods=['POST'])
@token_auth.login_required
def create_user():
    data = request.get_json() or {}
    if 'email' not in data or 'password' not in data:
        return bad_request('must include email and password fields')
    if User.query.filter_by(email=data['email'].first()):
        return bad_request('please use a different email address')
    u = User()
    u.from_dict(data, new_user=True)
    db.session.add(u)
    db.session.commit()
    response = jsonify(u.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=u.id)
    return response


@api.route('/users', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    if token_auth.current_user().id != id:
        abort(403)
    u = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'email' in data and data['email'] != u.email and User.query.filter_by(email=data['email'].first()):
        return bad_request('please use a different email address')
    u.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(User.query.get_or_404(id).to_dict())

@api.route('/users/<int:id>/followers', methods=['GET'])
@token_auth.login_required
def get_followers():
    pass

@api.route('/users/<int:id>/followed', methods=['GET'])
@token_auth.login_required
def get_followed(id):
    pass



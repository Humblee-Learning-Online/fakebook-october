from app.blueprints.main.models import Post
from .import bp as posts
from flask import json, jsonify, request
from .auth import token_auth
from app import db

@posts.route('/posts/<int:id>', methods=['GET'])
@token_auth.login_required
def get_post(id):
    return jsonify(Post.query.get(id).to_dict())

@posts.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    p = Post.query.get_or_404(id)
    data = request.get_json()
    
    p.body = data.get('body')
    db.session.commit()
    return jsonify(p.to_dict())
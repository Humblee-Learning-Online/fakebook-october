from app import db, login_manager
from datetime import datetime as dt
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    posts = db.relationship('Post', backref='user')

    def generate_password(self, real_password):
        self.password = generate_password_hash(real_password)

    def check_password(self, real_password):
        # return True or False
        return check_password_hash(self.password, real_password)

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))
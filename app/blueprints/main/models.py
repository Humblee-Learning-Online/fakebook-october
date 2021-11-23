from app import db
from datetime import datetime as dt
# from app import login_manager
# from flask_login import UserMixin

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
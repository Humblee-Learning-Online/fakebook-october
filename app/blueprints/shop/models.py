from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    description = db.Column(db.Text)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_key = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quantity = db.Column(db.Integer)
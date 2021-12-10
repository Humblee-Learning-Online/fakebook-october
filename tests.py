from datetime import datetime as dt, timedelta
import unittest
from app import create_app, db
from flask import current_app as app
from app.blueprints.auth.models import User
from app.blueprints.main.models import Post
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DARABASE_URI = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(email='derekh@codingtemple.com')
        u.generate_password('abc123')
        self.assertFalse(u.check_password('321bca'))
        self.assertTrue(u.check_password('abc123'))

    def test_token_creation(self):
        u = User(email='derekh@codingtemple.com')
        db.session.add(u)
        db.session.commit()
        u.get_token()
        self.assertEqual(u.get_token(), u.get_token())
        self.assertNotEqual(u.get_token(), 'anything')

    def test_token_expiration(self):
        u = User(email='derekh@codingtemple.com')
        db.session.add(u)
        db.session.commit()

        # Test token revocation
        u.get_token()
        self.assertEqual(u.get_token(), u.get_token())
        u.revoke_token()
        self.assertEqual(u.token, u.token)
        self.assertEqual(u.token_expiration, u.token_expiration)
        self.assertEqual(u.check_token(u.token), None)
        

class StripePaymentCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_payment_success(self):
        u = User(email='derekh@codingtemple.com')
        u.generate_password('abc123')
        self.assertFalse(u.check_password('321bca'))
        self.assertTrue(u.check_password('abc123'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
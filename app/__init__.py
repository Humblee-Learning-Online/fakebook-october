from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
moment = Moment(app)

from app.blueprints.main import bp as main
app.register_blueprint(main)

from app.blueprints.auth import bp as auth
app.register_blueprint(auth)

from app.blueprints.blog import bp as blog
app.register_blueprint(blog)
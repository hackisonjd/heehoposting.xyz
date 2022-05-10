from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():

    from website.views import bp
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = os.urandom(24)
    db.init_app(app)

    app.register_blueprint(bp, url_prefix="/")

    from .models import User, Post

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'bp.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
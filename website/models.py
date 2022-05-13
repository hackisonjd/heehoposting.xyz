'''
Schemas for each of the models that we're using here.
'''

from sqlalchemy.sql import func
from flask_login import UserMixin
from . import db

# Pylint is stupid, there's no other way to declare schemas like this, so Pylint can fuck itself.

# pylint: disable=R0903
class Post(db.Model):
    '''
    Schema for a Post data entry, each user has several posts.
    '''
    # pylint: disable=E1101
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# pylint: disable=R0903
class User(db.Model, UserMixin):
    '''
    Schema for a User data entry, each of them have an id, username, and password.
    They also have several posts.
    '''

    # pylint: disable=E1101
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    posts = db.relationship('Post')

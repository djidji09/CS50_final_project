from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70), unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    logged_in = db.Column(db.Boolean, default=False)
    gym_check_in = db.Column(db.Boolean, default=False)
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.id'))


class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    logged_in_users = db.Column(db.Integer)
    users = db.relationship('User', backref='gym', lazy=True)

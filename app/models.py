from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    groups = db.relationship('Group', backref='members', lazy='dynamic')
    kbas = db.relationship('KBA', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'''<{self.username} >'''

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(32), index=True, unique=True)
    geckos = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'''<Group Name: {self.group}
        Geckos: {self.geckos}>'''


class KBA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(126), index=True, unique=True)
    body = db.Column(db.String(1000), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'''Title: {self.title} - Date: {self.timestamp} - Author: {self.author}'''

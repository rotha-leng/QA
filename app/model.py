import datetime
from app import app, db #login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user


class MKT_USER(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Fullname = db.Column(db.String(50))
    Email_Address = db.Column(db.String(75))
    Password = db.Column(db.String(75))
    Avatar = db.Column(db.String(100))
    Created = db.Column(db.String(50), default=datetime.datetime.utcnow)


def __init__(self, FullName, Email_Address, Password, Avatar, Created):
    self.FullName = FullName
    self.Email_Address = Email_Address
    self.Password = Password
    self.Avatar = Avatar
    self.Created = Created

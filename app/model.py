import datetime
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user


class MKT_USER(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Fullname = db.Column(db.String(50))
    Email = db.Column(db.String(75))
    Password = db.Column(db.String(75))
    Avatar = db.Column(db.String(100))
    Created = db.Column(db.String(50), default=datetime.datetime.utcnow)

    def __init__(self, FullName, Email_Address, Password, Avatar, Created):
        self.FullName = FullName
        self.Email = Email
        self.Password = Password
        self.Avatar = Avatar
        self.Created = Created


class MKT_QUESTION(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Title = db.Column(db.String(75))
    Body = db.Column(db.Text)
    Tag = db.Column(db.String(150))
    Vote = db.Column(db.Integer)
    User = db.Column(db.Integer)
    BestAnswer = db.Column((db.Integer))
    Created = db.Column(db.String(20), default=datetime.datetime.utcnow)

    def __init__(self,Title, Body, Tag, Vote, User, BestAnswer,Created):
        self.Title = Title
        self.Body = Body
        self.Tag = Tag
        self.Vote = Vote
        self.User = User
        self.BestAnswer = BestAnswer
        self.Created = Created 

class  MKT_ANSWER(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    QuestionID = db.Column(db.Integer)
    Answer = db.Column(db.Text)
    User = db.Column(db.Integer)
    CreatedOn = db.Column(db.String(10))

    def __init__(self, QuestionID, Answer, User, CreatedOn):
        self.QuestionID = QuestionID
        self.Answer = Answer
        self.User = User
        self.CreateOn = CreateOn

class  MKT_VOTE(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    QuestionID = db.Column(db.Integer)
    UserID = db.Column(db.Integer)
    CreateOn = db.Column(db.String(10))

    def __init__(self,QuestionID, UserID, CreateOn):
        self.QuestionID =QuestionID
        self.UserID = UserID
        self.CreatedOn = CreatedOn
class MKT_COMMENT(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    QuestionID = db.Column(db.Integer)
    Comment = db.Column(db.Text)
    UserID = db.Column(db.Integer)
    CreatedOn = db.Column(db.String(10))
    def __init__(self, QuestionID, Comment, UserID, CreateOn):
        self.QuestionID = QuestionID
        self.Comment = Comment
        self.UserID = UserID
        self.CreateOn = CreateOn

      







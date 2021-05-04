import datetime
from app import app, db
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


class MKT_QUESTION(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Question_Tittle = db.Column(db.String(75))
    Question_body = db.Column(db.Text)
    Tag_Topic = db.Column(db.String(150))
    Vote = db.Column(db.Integer)
    User = db.Column(db.Integer)
    Best_Answer = db.Column((db.Integer))
    Created = db.Column(db.String(20), default=datetime.datetime.utcnow)

    def __init__(self,Question_Tittle, Question_body, Tag_Topic, Vote, User, Best_Answer,Created):
        self.Question_Tittle = Tittle
        self.Question_body = Body
        self.Tag_Topic = Tag 
        self.Vote = Vote
        self.User = User
        self.Created = Created 

class  MKT_ANSWER(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    QuestionID = db.Column(db.Integer)
    Answer = db.Column(db.Text)
    User = db.Column(db.Integer)
    Created_On = db.Column(db.String(10))

    def __init__(self, QuestionID, Answer, User, Created_On):
        self.QuestionID = QuestionID
        self.Answer = Answer
        self.User = User
        self.Created_On = CreatedOn

class  MKT_VOTE(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Question_ID = db.Column(db.Integer)
    User_ID = db.Column(db.Integer)
    Created_On = db.Column(db.String(10))

    def __init__(self,Question_ID, User_ID, Created_On):
        self.Question_ID = Question
        self.User_ID = User_ID
        self.Created_On = CreatedOn
class MKT_COMMENT(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Question_ID = db.Column(db.Integer)
    Comment = db.Column(db.Text)
    User_ID = db.Column(db.Integer)
    Created_On = db.Column(db.String(10))
    def __init__(self, Question_ID, Comment, User_ID, Created_On):
        self.Question_ID = Question
        self.Comment = Comment
        self.User_ID = User_ID
        self.Created_On = CreatedOn

      







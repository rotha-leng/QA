
from app import*
from .model import *
from flask import Flask,flash, render_template, request,redirect,url_for,jsonify
from werkzeug.exceptions import abort
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms import validators,ValidationError
import sqlalchemy
from sqlalchemy.sql.expression import cast



class searchQA(Form):
    searchbox = TextField("Search",[validators.Required("Please Enter your Title!")])
@app.route('/', methods=['POST', 'GET'])
def getPost():



    search = request.args.get('Search')
    """Fetch all post records by author ID, or all
    
    Args:
        postid (str, optional): if passed, ID of post to be displayed
    
    Returns:
        post object: Post Object Record
    """

    if search== None:
        totalQA = MKT_QUESTION.query.count()
        questions = db.session.query(MKT_QUESTION.Title,MKT_QUESTION.Body,MKT_QUESTION.BestAnswer,MKT_QUESTION.Created).all()
        question = db.session.\
                query(MKT_QUESTION.ID, MKT_QUESTION.Title, MKT_QUESTION.Body, 
                MKT_QUESTION.Tag, MKT_QUESTION.Vote, MKT_QUESTION.User, MKT_QUESTION.BestAnswer, MKT_QUESTION.Created,MKT_USER.Fullname).\
                join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric)==MKT_QUESTION.User).\
                order_by(MKT_QUESTION.Created.desc()).\
                all()
        
    else:
        search = "%{}%.format"(search)
        questions = db.session.query(MKT_QUESTION.Title,MKT_QUESTION.Body,MKT_QUESTION.BestAnswer,MKT_QUESTION.Created).all()
        
        question = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Title, MTK_QUESTION.Body, 
                MKT_QUESTION.Tag, MKT_QUESTION.Vote, MKT_QUESTION.User, MKT_QUESTION.BestAnswer, MKT_QUESTION.Created,MKT_User.Fullname).\
        join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric)==MKT_QUESTION.User).\
        filter(or_
                (MKT_QUESTION.Title.like("%"f"{search}""%"),
                MKT_QUESTION.Body.like("%"f"{search}""%"),
                MKT_QUESTION.Tag.like("%"f"{search}""%")))
        totalQA = question.count()
    return render_template('home/index.html',question=question,totalQA=totalQA )
        
                    
def btnFilter(condition):
    if condition == None:
        return redirect(url_for('getPost'))		
    else:
        questions = db.session.query(MKT_QUESTION.Title,MKT_QUESTION.Body,MKT_QUESTION.BestAnswer,MKT_QUESTION.Created).all()

        question = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Title, MTK_QUESTION.Body, 
                MKT_QUESTION.Tag, MKT_QUESTION.Vote, MKT_QUESTION.User, MKT_QUESTION.BestAnswer, MKT_QUESTION.Created,MKT_User.Fullname).\
                join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric)==MKT_QUESTION.User).\
                filter(MKT_qQUESTION.Title.like("%Test1%"))
        totalQA = question.count()
        return render_template('home/index.html',question=question,totalQA=totalQA )
    

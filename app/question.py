
from app import*
from .model import *
from flask import Flask,flash, render_template, request,redirect,url_for,jsonify
from werkzeug.exceptions import abort
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms import validators,ValidationError
import sqlalchemy
from sqlalchemy.sql.expression import cast


#@app.route('/Post/<int:postid>')
#@app.route('/Post/')
@app.route('/')
def getPost(postid=''):
	"""Fetch all post records by author ID, or all
	
	Args:
		postid (str, optional): if passed, ID of post to be displayed
	
	Returns:
		post object: Post Object Record
	"""
	if postid=='':
		questions = db.session.query(MKT_QUESTION.Title,MKT_QUESTION.Body,MKT_QUESTION.BestAnswer,MKT_QUESTION.Created).all()
		question = db.session.\
				query(MKT_QUESTION.ID, MKT_QUESTION.Title, MKT_QUESTION.Body, 
				MKT_QUESTION.Tag, MKT_QUESTION.Vote, MKT_QUESTION.User, MKT_QUESTION.BestAnswer, MKT_QUESTION.Created,MKT_USER.Fullname).\
				join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric())==MKT_QUESTION.User).\
				order_by(MKT_QUESTION.Created.desc()).\
				all()
		print(question)
		print(questions)
	else:

		question = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Title, MTK_QUESTION.Body, 
				MKT_QUESTION.Tag, MKT_QUESTION.Vote, MKT_QUESTION.User, MKT_QUESTION.BestAnswer, MKT_QUESTION.Created,MKT_User.Fullname).\
				join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric())==MKT_QUESTION.User).filter(MKT_QUESTION.ID == postid)
		print(question)
		if question.first() is None:
			abort(404) # trigger 404 post not found
 

	return render_template('home/index.html',posts=questions)



from .model import *
from app import db, app
import sqlalchemy
from sqlalchemy.sql.expression import cast

import datetime

from flask import render_template, request, url_for, flash, redirect, jsonify

from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash

from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField
from wtforms import validators, ValidationError
from sqlalchemy import or_
#from flask_moment import Moment



class searchQA(Form):
	searchbox = TextField("Search", [validators.Required("Please Enter your Title!")])


@app.route('/', methods=['POST', 'GET'])
def getPost():
	search = request.args.get('Search')
	if search == None:
		totalQA = MKT_QUESTION.query.count()
		question = db.session.\
			query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body, MKT_QUESTION.Tag_Topic,MKT_QUESTION.Created, MKT_USER.FullName). \
			join(MKT_USER, MKT_USER.ID == MKT_QUESTION.User). \
			all()


	else:
		search = "%{}%".format(search)
		"""questions = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body, MKT_QUESTION.Tag_Topic, MKT_QUESTION.Best_Answer,
									 MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Question_ID, MKT_ANSWER.QuestionID). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.User). \
			all()"""


		question = db.session.\
			query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body, MKT_QUESTION.Tag_Topic,MKT_QUESTION.Created, MKT_USER.FullName). \
			join(MKT_USER, MKT_USER.ID == MKT_QUESTION.User). \
			filter(or_
				(MKT_QUESTION.Question_Tittle.like("%"f"{search}""%"),
				MKT_QUESTION.Question_body.like("%"f"{search}""%"),
		        MKT_QUESTION.Tag_Topic.like("%"f"{search}""%")))
		totalQA = question.count()
	return render_template('home/index.html', posts=question, totalQA=totalQA)


"""def btnFilter(condition):
	if condition == None:
		return redirect(url_for('getPost'))
	else:

		questions = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body,
									 MKT_QUESTION.Tag_Topic, MKT_QUESTION.Best_Answer,
									 MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Question_ID,
									 MKT_ANSWER.QuestionID). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.User). \
			all()


		question = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body,
									MKT_QUESTION.Tag_Topic, MKT_QUESTION.Vote, MKT_QUESTION.User, MKT_QUESTION.Best_Answer,
									MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Question_ID). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.User). \
			filter(MKT_QUESTION.Question_Tittle.like("%Test1"))
		totalQA = question.count()
		return render_template('home/index.html', posts=question, totalQA=totalQA)"""

@app.route('/All')
def all():
	totalQA = MKT_QUESTION.query.count()
	question = db.session.\
			query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body, MKT_QUESTION.Tag_Topic,MKT_QUESTION.Created, MKT_USER.FullName). \
			join(MKT_USER, MKT_USER.ID == MKT_QUESTION.User). \
		all()
	return render_template('home/index.html', posts=question, totalQA=totalQA)

@app.route('/MostRecent')
def mostrecent():
	totalQA = MKT_QUESTION.query.count()
	question = db.session.\
			query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body, MKT_QUESTION.Tag_Topic,MKT_QUESTION.Created, MKT_USER.FullName). \
			join(MKT_USER, MKT_USER.ID == MKT_QUESTION.User). \
		order_by(MKT_QUESTION.Created.desc()). \
		all()
	return render_template('home/index.html', posts=question, totalQA=totalQA)



class PostForm(Form):
	username = TextField(" Full Name :", [validators.Required("Enter a name"), validators.Length(min=5, max=15, message="Full Name Cannot less than 5 or more then 30")])
	EmailAddress = TextField(" Email Address :", [validators.Required("Enter your email address")])
	password = PasswordField(" Password :", [validators.Required("Create a password"), validators.Length(min=1, max=15, message="Password Cannot less than 1 or more then 15")])


	def validate_EmailAddress(form, field):
		title = field.data
		postObj = MKT_USER.query.filter_by(Email_Address=title)
		if postObj.first():
			raise ValidationError(f'Post title {title} already exist!')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = PostForm()
	if request.method == 'POST':

		if form.validate() == True:

			fullname = request.form['username']
			emailaddress = request.form['EmailAddress']
			password = request.form['password']
			passwords = generate_password_hash(password)
			register = MKT_USER(FullName=fullname, Email_Address=emailaddress, Password=passwords, Avatar='', Created=datetime.datetime.now())
			db.session.add(register)
			db.session.commit()
			flash("Your Sign up have been successfully, Please click Sign in at bottom!")
			return redirect(url_for('register'))

	return render_template("auth/register.html", form=form)



@app.route('/Login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		emailaddress = request.form['email']
		password = request.form['password']

		authObj = MKT_USER.query.filter_by(Email_Address=emailaddress).first()
		if check_password_hash(authObj.Password, password) == True:
			login_user(authObj)
			return redirect(url_for('getPost'))
		else:
			flash("Incorrect Email Address or Password!")

	return render_template('auth/login.html')


class AskForm(Form):
	Title = TextField("Question Title", [validators.Required("Please enter post title."), validators.Length(min=10, max=100,message="Post Title Cannot less than 10 or more then 100")])
	Body = TextAreaField("Question Body", [validators.Required("Please enter post content.")])
	Tag = TextField("Tag and Topic", [validators.Required("Select Tags for the Question")])

	def validate_Title(form, field):
		title = field.data
		postObj = MKT_QUESTION.query.filter_by(Question_Tittle=title)

		if postObj.first():
			raise ValidationError(f'Post title {title} already exist!')


@app.route('/ask', methods=['GET', 'POST'])
# @login_required
def askQuestion():
	form = AskForm()

	if request.method == 'POST':

		if form.validate() == True:
			Title = request.form['Title']
			Body = request.form['Body']
			Tag = request.form['Tag']
			AuthorID = current_user.get_id()

			Posts = MKT_QUESTION(Question_Tittle=Title, Question_body=Body, Tag_Topic=Tag, Vote=0, Best_Answer=0, User=AuthorID, Created=datetime.datetime.now().strftime("%x-%X"))

			db.session.add(Posts)
			db.session.commit()

			flash('Your Post has been added successfully.')

			return redirect(url_for('getPost'))
	return render_template('question/create.html', form=form)


@app.route('/Logout')
@login_required
def logout():
	logout_user()
	flash('You are now logout! Please Sign in again.')
	return redirect(url_for('index'))


@app.route('/ManagePost')
@login_required
def managePost():
	ID = current_user.get_id()

	authorObj = MKT_USER.query.get(ID)
	postByAuthObj = MKT_QUESTION.query.filter_by(Question_Tittle=str(ID)).all()
	if postByAuthObj:

		return render_template('question/index.html', posts=postByAuthObj, user=authorObj)
	else:
		return render_template('question/index.html')


#@app.route('/getRetatedPost')
#@login_required
def getRelatedPost(search):
	#search = request.args.get('Search')
	#postList = []
	print('search:',search)
	if search:
		postObj = MKT_QUESTION.query.limit(2).all()
			#.filter(MKT_QUESTION.Question_Tittle.contains(search))\
		 
			

		return postObj
	return ''

@app.route('/comment', methods=['POST', 'GET'])
def comment():
	comment = db.session.query(MKT_COMMENT.Comment).all()
	print(comment)
	return render_template('question/index.html', comments=comment)


class CommentForm(Form):
	Comment = TextField("Leave a comment", [validators.Required("Please enter post content.")])
	Answer = TextField("Submit an answer", [validators.Required("Please enter post content.")])
	Submit = SubmitField("Send")

@app.route('/View/Question/<int:QuestionID>', methods=['POST', 'GET'])
def view(QuestionID=''):
	form = CommentForm()
	if QuestionID == '':
		Question =  db.session.\
			query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body, MKT_QUESTION.Tag_Topic,MKT_QUESTION.Created, MKT_USER.FullName). \
			join(MKT_USER, MKT_USER.ID == MKT_QUESTION.User). \
			all()

		"""comment = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body,
								   MKT_QUESTION.Tag_Topic, MKT_QUESTION.Vote, MKT_QUESTION.User,
								   MKT_QUESTION.Best_Answer,
								   MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Comment). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.ID). \
			all()

		answer = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body,
								   MKT_QUESTION.Tag_Topic, MKT_QUESTION.Vote, MKT_QUESTION.User,
								   MKT_QUESTION.Best_Answer,
								   MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Comment, MKT_ANSWER.Answer). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.ID). \
			all()"""

	else:
        
		Question =  db.session.\
			query(MKT_QUESTION.Question_Tittle,MKT_QUESTION.Question_body,MKT_QUESTION.Tag_Topic,MKT_QUESTION.Vote,MKT_QUESTION.User,MKT_QUESTION.Created,MKT_USER). \
			join(MKT_USER, MKT_USER.ID == MKT_QUESTION.User). \
            filter(MKT_QUESTION.ID == QuestionID).first()
		print(Question.User)

		"""comment = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body,
								   MKT_QUESTION.Tag_Topic, MKT_QUESTION.Vote, MKT_QUESTION.User,
								   MKT_QUESTION.Best_Answer,
								   MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Comment). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.ID). \
			filter(MKT_QUESTION.ID == QuestionID)


		answer = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body,
								   MKT_QUESTION.Tag_Topic, MKT_QUESTION.Vote, MKT_QUESTION.User,
								   MKT_QUESTION.Best_Answer,
								   MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Comment, MKT_ANSWER.Answer). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.ID). \
			filter(MKT_QUESTION.ID == QuestionID)
		print(answer)"""
		questionrelated=getRelatedPost(Question.Question_Tittle)


		


		if Question is None:
			abort(404)

	"""if request.method == 'POST':
		if form.validate() == True:
			comment = request.form['Comment']
			postcomment = MKT_COMMENT(Comment=comment)
			db.session.add(postcomment)
			db.session.commit()

			answer = request.form['Answer']
			answer = MKT_ANSWER(Answer=answer)
			db.session.add(answer)
			db.session.commit()"""

		#return redirect(url_for('view'))
	#Answer = MKT_ANSWER.query.all()
	return render_template('question/index.html', form=form, posts=Question,questionrelated=questionrelated)


"""questions = db.session.query(MKT_QUESTION.ID, MKT_QUESTION.Question_Tittle, MKT_QUESTION.Question_body, MKT_QUESTION.Tag_Topic, MKT_QUESTION.Best_Answer,
									 MKT_QUESTION.Created, MKT_USER.FullName, MKT_COMMENT.Question_ID, MKT_ANSWER.QuestionID). \
			join(MKT_USER, cast(MKT_USER.ID, sqlalchemy.Numeric) == MKT_QUESTION.User). \
			order_by(MKT_QUESTION.Created.desc()). \
			all()"""



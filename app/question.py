from app import *
from .model import *
from flask_blog import db, app
from flask import render_template

@app.route('/question')
def getQuestion(questionid=''):
	question = Question().query.all()

	return render_template('question/queation_view.html', posts=question)
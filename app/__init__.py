from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

from flask import Flask, render_template, request, session, url_for, redirect, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '!loveyou@ll'

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

DB_USER = 'postgres'  # database user
DB_PWD = 'biiiriiiniii13'  # database password
DB_NAME = 'qadb'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://%s:%s@localhost:5432/%s" % (DB_USER, DB_PWD, DB_NAME)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"


db = SQLAlchemy(app)

from .question import *  # register post view, so that its url is routable

@app.route('/')
def index():
    return render_template('home/index.html')


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/profile')
@login_required
def profilepage():
    return render_template('profile_page.html')

@app.route('/aboutpage', methods=['POST', 'GET'])
@login_required
def aboutpage():
    if "username" in session:
        username = session["username"]
        phone = session["phone"]
        email = session["email"]
        filename = session["image"]
        address = session["address"]
        return render_template('question/update.html', Name=username, Phone=phone, Email=email, filename=filename, Address=address)
    else:
        return render_template('question/update.html')


@app.route('/show', methods=['POST', 'GET'])
@login_required
def result():
    if request.method == 'POST':
        session.permanent = True
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session["image"] = filename
            myname = request.form['username']
            session["username"] = myname
            phone = request.form['phone']
            session["phone"] = phone
            email = request.form['email']
            session["email"] = email
            address = request.form['address']
            session["address"] = address
            return render_template('question/update.html', Name=myname, Phone=phone, filename=filename, Email=email, Address=address)
    else:
        if "username" in session:
            myname = request.form['username']
            phone = request.form['phone']
            email = request.form['email']
            address = request.form['address']
            return redirect(url_for('profile_page.htl', Name=myname, Phone=phone, Email=email, Address=address))
        else:
            return redirect(url_for('profilepage'))

@app.route('/display/<filename>')
@login_required
def display_image(filename):
    return redirect(url_for('static', filename='images/' + filename), code=301)
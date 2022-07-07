from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
# import time


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alex:123QWE@localhost/flask_db'
app.config['SECRET_KEY'] = 'djnhfjk3jh221jjj4h56vj7&89'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.route('/update/<int:id>', methods=['GET', "POST"])
def update(id):
	form=UserForm()
	name_to_update = Users.query.get_or_404(id)
	if request.method == "POST":
		name_to_update.name = request.form['name']
		name_to_update.email = request.form['email']
		name_to_update.favorite_color = request.form['favorite_color']
		try:
			db.session.commit()
			flash("User Updated!!!")
			return render_template("update.html",
				form=form,
				name_to_update=name_to_update)
		except Exception as e:
			flash("Error Updated")
			return render_template("update.html",
				form=form,
				name_to_update=name_to_update)
	else:
		return render_template("update.html",
				form=form,
				name_to_update=name_to_update)


class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	favorite_color = StringField("Favorite color")
	submit = SubmitField("Submit")


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(200), nullable=False, unique=True)
	favorite_color = db.Column(db.String(200))
	date_added = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Name %r>' % self.name


class NamerForm(FlaskForm):
	name = StringField("What's Your Name", validators=[DataRequired()])
	submit = SubmitField("Submit")


@app.route('/')
def index():
	flash("Welcome to our website!")
	return render_template("index.html")


@app.route('/user/<name>')
def user(name):
	return render_template("user.html", user_name=name)


@app.errorhandler(404)
def page404(e):
	return render_template("404.html"), 404


@app.errorhandler(500)
def page500(e):
	return render_template("500.html"), 500


@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("It's ok!")
	return render_template(
		'name.html',
		name = name,
		form = form)


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
	name = None
	form = UserForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user is None:
			user = Users(
				name=form.name.data,
				email=form.email.data,
				favorite_color=form.favorite_color.data)
			db.session.add(user)
			db.session.commit()
		name = form.name.data
		form.name.data = ''
		form.email.data = ''
		form.favorite_color.data = ''
		flash("User add Successfully!!!")
	our_users = Users.query.order_by(Users.date_added)
	return render_template(
		'add_user.html',
		form=form,
		name=name,
		our_users=our_users
		)








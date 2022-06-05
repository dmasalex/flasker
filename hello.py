from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'djnhfjk3jh221jjj4h56vj7&89'


class NamerForm(FlaskForm):
	name = StringField("What's Your Name", validators=[DataRequired()])
	submit = SubmitField("Submit")


@app.route('/')
def index():
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
	return render_template('name.html',
		name = name,
		form = form)








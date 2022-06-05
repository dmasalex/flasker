from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
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
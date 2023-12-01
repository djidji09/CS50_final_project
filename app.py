from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configure application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        return render_template("index.html")
    else:
        redirect("login")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """Show portfolio of stocks"""
    if request.method == "GET":
        return render_template("sign_up.html")
    else:
        redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Show portfolio of stocks"""
    if request.method == "GET":
        return render_template("login.html")
    else:
        redirect("/")


# running the debuger
if __name__ == '__main__':
    app.run(debug=True)

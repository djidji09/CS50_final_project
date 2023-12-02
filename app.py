from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return redirect(url_for("login"))


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("sign_up.html")
    else:
        return redirect(url_for("login"))  # Added return statement


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return redirect("/")  # Added return statement


# running the debugger
if __name__ == '__main__':
    app.run(debug=True)

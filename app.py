from flask import Flask, url_for, render_template, request
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


# running the debuger
if __name__ == '__main__':
    app.run(debug=True)

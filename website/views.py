from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        return render_template("index.html")
    else:
        return render_template("index.html")


@views.route('/exercices', methods=['GET', 'POST'])
@login_required
def exercices():
    if request.method == 'POST':
        return render_template("exerciecs.html")
    else:
        return render_template("exercices.html")

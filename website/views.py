from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Gym
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/gym_login', methods=['GET', 'POST'])
@login_required
def gym_login():
    if request.method == 'POST':
        gym_name = request.form.get("gym_name")
        gym = Gym.query.filter_by(name=gym_name).first()

        if not gym:
            flash('Gym does not exist. Creating a new one.')
            new_gym = Gym(name=gym_name)
            db.session.add(new_gym)
            db.session.commit()
            gym = new_gym

        # Update the user's gym_id and set online status to True
        current_user.gym_id = gym.id
        current_user.online = True
        db.session.commit()

        flash(f'Checked into {gym.name} successfully!')
        return redirect(url_for('views.home'))
    else:
        return render_template('gym_login.html')


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        # Retrieve the list of users currently online in a specific gym
        # online_users = User.query.filter_by(gym_id=gym_id, online=True).all()
        # return render_template("index.html", online_users=online_users)
        return render_template("index.html")


@views.route('/exercices', methods=['GET', 'POST'])
@login_required
def exercices():
    if request.method == 'POST':
        return render_template("exerciecs.html")
    else:
        return render_template("exercices.html")

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
        db.session.commit()

        flash(f'signed into {gym.name} successfully!')
        return redirect(url_for('views.home'))
    else:
        return render_template('gym_login.html')


@views.route('/check_in', methods=['GET', 'POST'])
@login_required
def check_in():
    if request.method == 'GET':
        if not current_user.gym_check_in:
            current_user.online = True
            current_user.gym_check_in = True  # Mark the user as checked in
            current_user.gym.logged_in_users = (
                current_user.gym.logged_in_users or 0) + 1
            db.session.commit()
            flash('Checked in successfully!')
        else:
            flash('Already checked in.')

        return redirect(url_for('views.home'))


@views.route('/check_out', methods=['GET', 'POST'])
@login_required
def check_out():
    if request.method == 'GET':
        if current_user.gym_check_in:
            current_user.online = False
            current_user.gym_check_in = False  # Mark the user as checked out
            current_user.gym.logged_in_users = max(
                0, current_user.gym.logged_in_users - 1)
            db.session.commit()
            flash('Checked out successfully!')
        else:
            flash('You need to check in first.')

        return redirect(url_for('views.home'))


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        # get the gym_id
        gym_id = current_user.gym_id
        # Retrieve the list of users currently online in a specific gym
        gym_name = db.session.query(Gym.name).filter_by(id=gym_id)
        logged_in_users = db.session.query(
            Gym.logged_in_users).filter_by(id=gym_id).scalar()
        return render_template("index.html", online_users=logged_in_users, gym_name=gym_name)


@views.route('/exercices', methods=['GET', 'POST'])
@login_required
def exercices():
    if request.method == 'POST':
        return render_template("exerciecs.html")
    else:
        return render_template("exercices.html")

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import user as user_db
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print("done taking user data")
        user = user_db.query.filter_by(username=username).first()
        print("done geting the data into a variable")
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                print("done cheking if the user is true")
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user) 
    


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        print('getting the users info')
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print("done")

        print("checking if the user is in the databe")
        user = user_db.query.filter_by(email=email).first()
        print("done")
        print("some conditions")
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            print("done")
            print("hashing the password and puting the ")
            new_user = user_db(email=email, username=username, password=generate_password_hash(
                password1, method='pbkdf2:sha256', salt_length=8))

            print("puting everything in the database")
            db.session.add(new_user)
            db.session.commit()
            print("done")
            print("login")
            login_user(new_user, remember=True)
            print("done")
            flash('Account created!', category='success')
            print("redirecting")

            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

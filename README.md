# Flask Gym Management Web App

#### Video Demo: https://youtu.be/13nCEXbKTSI

## Overview

This Flask web application is designed to serve as a gym management system, allowing users to create accounts, log in, and access information about their selected gym. The main features include user authentication, gym registration, and the ability to view the current gym occupancy at any time .

## Project Structure

### 1. `app.py`

It serves as an Entry point of the application. It creates and runs the Flask app.

### 1. `__init__.py`

This file initializes the Flask application and sets up the database using SQLAlchemy. It also configures the login manager for user authentication. The application is structured using blueprints for better modularity.

### 2. `auth.py`

Handles user authentication, including login, logout, and account creation. Passwords are securely hashed using the Werkzeug library. The file defines routes for these actions and includes error handling for various scenarios.

### 3. `models.py`

Defines the data models for the application using SQLAlchemy. Two main models are implemented: `User` for user accounts and `Gym` for gym information. The `User` model includes fields such as email, username, and a reference to the associated gym.

### 4. `views.py`

Contains routes for the main functionality of the app, such as gym login, check-in/out, and gym occupancy.

### 5. `templates` folder

Contains HTML templates for rendering web pages. Common templates include
`layout.html`
Base HTML template that defines the overall structure of the web pages.
`login.html`
for the login page and
`sign_up.html`
for user registration.
`index.html`
Template for the home page displaying the gym occupancy.
`gym_login.html`
Template for the gym login page.
`css`
Stylesheet for styling the HTML pages.
`java script`
JavaScript file for handling theme switching.

## Getting Started

1. **Install Dependencies:**

   bashCopy code

   `pip install Flask Flask-SQLAlchemy Flask-Login`

2. **Run the Application:**

   bashCopy code

   `python run.py`

   The application will be accessible at `you're local host`

3. **Usage:**

   - Visit `/sign_up` to create a new account.
   - Log in using the credentials at `/login`.
   - Visit the gym login to choose a gym
   - see how many people are there
   - when you go to the gym and check in it shows up to other people

## Database

The application uses SQLite as its database. The database file (`gym.db`) is created automatically upon running the application.

- User authentication (login, logout, sign-up).
- Gym management (login, check-in/out).
- Dynamic theme switching (light/dark).

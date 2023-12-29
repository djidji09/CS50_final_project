# Flask Gym Management Web App

#### Video Demo: <URL HERE>

#### Description:

## Overview

This Flask web application is designed to serve as a gym management system, allowing users to create accounts, log in, and access information about their selected gym. The main features include user authentication, gym registration, and the ability to view the current occupancy of the gym and the presence of a coach.

## Project Structure

### 1. `__init__.py`

This file initializes the Flask application and sets up the database using SQLAlchemy. It also configures the login manager for user authentication. The application is structured using blueprints for better modularity.

### 2. `auth.py`

Handles user authentication, including login, logout, and account creation. Passwords are securely hashed using the Werkzeug library. The file defines routes for these actions and includes error handling for various scenarios.

### 3. `models.py`

Defines the data models for the application using SQLAlchemy. Two main models are implemented: `User` for user accounts and `Gym` for gym information. The `User` model includes fields such as email, username, and a reference to the associated gym.

### 4. `views.py`

Incomplete, but intended to contain the main functionality for the application. This file is expected to handle the routes related to gym management, such as displaying gym occupancy and coach presence.

### 5. `templates` folder

Contains HTML templates for rendering web pages. Common templates include `login.html` for the login page and `sign_up.html` for user registration.

## Getting Started

1. **Install Dependencies:**

   bashCopy code

   `pip install Flask Flask-SQLAlchemy Flask-Login`

2. **Run the Application:**

   bashCopy code

   `python run.py`

   The application will be accessible at `http://127.0.0.1:5000/`.

3. **Usage:**

   - Visit `/sign_up` to create a new account.
   - Log in using the credentials at `/login`.
   - Explore the incomplete features in the `/main` route.

## Database

The application uses SQLite as its database. The database file (`gym.db`) is created automatically upon running the application.

## Notes

- The project structure and implementation provide a foundation for a gym management system, but additional features and views need to be developed in `views.py`.
- Ensure that all dependencies are installed before running the application.

Feel free to expand on this foundation by implementing additional features and completing the views. Happy coding!

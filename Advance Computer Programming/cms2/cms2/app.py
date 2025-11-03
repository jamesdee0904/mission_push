# Import all the tools we need from Flask
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

# Import tools from Flask-WTF (this helps us create and validate forms easily)
from flask_wtf import FlaskForm

# Import form fields (these are the input boxes, radio buttons, etc.)
from wtforms import StringField, PasswordField, SubmitField, RadioField, TextAreaField, DateField, SelectMultipleField, widgets

# Import validators (these make sure the user fills out the form correctly)
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

# Import json library to work with JSON data (used later for API)
import json

# Create our Flask app
app = Flask(__name__)

# Every Flask app that uses forms or sessions needs a secret key
# Think of this like a "lock" that keeps your session and CSRF data safe.
app.secret_key = "supersecret"  

# REGISTER FORM CLASS
# This class creates a registration form for new users
# It uses WTForms, which helps us create forms with validation rules easily.
class RegisterForm(FlaskForm):
    
    # Username text field — user must type something (min 3 chars, max 20)
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    
    # Password text field — must be filled and have at least 5 chars
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5)])
    
    # Confirm password field — must match the password field
    confirm = PasswordField("Confirm Password", validators=[EqualTo('password', "Passwords must match!")])
    
    # Gender radio buttons — choose one: Male or Female
    gender = RadioField("Gender", choices=[("Male", "Male"), ("Female", "Female")], validators=[DataRequired()])
    
    # Birthday field — uses a date picker (must be filled)
    birthday = DateField("Birthday", format="%Y-%m-%d", validators=[DataRequired()])
    
    # Address text field — must be at least 5 characters long
    address = StringField("Address", validators=[DataRequired(), Length(min=5)])
    
    # Description box — a big text area for anything the user wants to add
    description = TextAreaField("Description")

    # Custom validator for hobbies — user must pick at least one
    def at_least_one(form, field):
        if not field.data:
            raise ValidationError("Please select at least one hobby.")
        
    # Hobbies checkboxes — user can select multiple items
    # We use a special widget to make each hobby appear as a checkbox
    hobbies = SelectMultipleField(
        "Hobbies",
        choices=[
            ("reading", "Reading"),
            ("sports", "Sports"),
            ("music", "Music"),
            ("coding", "Coding"),
            ("travel", "Travel"),
        ],
        option_widget=widgets.CheckboxInput(),    # Makes them checkboxes
        widget=widgets.ListWidget(prefix_label=False),  # Layout style
        validators=[at_least_one]                 # Make sure at least one is picked
    )

    # Submit button to send the form
    submit = SubmitField("Register")

# LOGIN FORM CLASS
class LoginForm(FlaskForm):
    # User must type username and password
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# TEMPORARY STORAGE (like a mini database)
# For now, we store user data in a dictionary instead of a real database
# Example: users["jexus"] = {"password": "123", "gender": "Male", ...}
users = {}

# HOME PAGE
@app.route('/')
def home():
    # When someone visits "/", we show index.html
    return render_template('index.html')

# REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()  # Create an empty form

    # If the user clicks the "Register" button and the form is valid...
    if form.validate_on_submit():
        username = form.username.data  # Get username input

        # Check if username already exists in "users"
        if username in users:
            return render_template('register.html', form=form, error="Username already exists!")

        # Save the new user in our in-memory dictionary
        users[username] = {
            "password": form.password.data,
            "gender": form.gender.data,
            "birthday": form.birthday.data.strftime("%Y-%m-%d"),
            "address": form.address.data,
            "description": form.description.data,
            "hobbies": form.hobbies.data  # list of selected hobbies
        }

        # After successful registration, go to the login page
        return redirect(url_for('login'))

    # If user just opened the page (GET), show the blank form
    return render_template('register.html', form=form)

# LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Create a login form

    if form.validate_on_submit():  # When user clicks submit
        username = form.username.data
        password = form.password.data

        # Find the user in our "database"
        user = users.get(username)

        # If user exists and password matches
        if user and user["password"] == password:
            session['user'] = username  # Save username in session (like a login token)
            return redirect(url_for('profile'))  # Go to profile page

        # If wrong username or password, show error
        else:
            return render_template('login.html', form=form, error="Invalid credentials!")

    # If just visiting the page, show login form
    return render_template('login.html', form=form)

# ROFILE PAGE
@app.route('/profile')
def profile():
    # If not logged in, redirect to login page
    if 'user' not in session:
        return redirect(url_for('login'))

    # Get username and data of logged-in user
    username = session['user']
    user_data = users[username]

    # Show profile.html with user's data
    return render_template('profile.html', username=username, user=user_data)

# LOGOUT PAGE
@app.route('/logout')
def logout():
    # Remove the user from session (log out)
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/api/users', methods=['GET'])
def get_users():
    data = {}  # Start with an empty dictionary

    # Loop through all users
    for username, info in users.items():
        # Create a temporary dictionary for this user
        user_data = {}

        # Loop through all key-value pairs in the user's info
        for key, value in info.items():
            # Skip the password
            if key != "password":
                user_data[key] = value

        # Add the filtered user data to the main dictionary
        data[username] = user_data

    # Convert to JSON and return
    return jsonify(data)

# RUN THE APP
if __name__ == '__main__':
    app.run(debug=True)

# app.py
# ======
# Minimal Flask application that demonstrates:
#  - app creation
#  - route definitions
#  - rendering templates with data
#  - handling GET and POST with WTForms
#  - CSRF protection via Flask-WTF

from flask import Flask, render_template, request
# Flask: the main class to create the web application object.
# render_template: helper to load and render Jinja2 HTML templates.
# request: the global request object representing the current HTTP request.

from flask_wtf import FlaskForm
# FlaskForm: base class for building web forms integrated with Flask/CSRF.

from wtforms import StringField, SubmitField
# StringField: a field that renders an <input type="text">.
# SubmitField: a field that renders a submit <button>.

from wtforms.validators import DataRequired
# DataRequired: validator that ensures the field is not empty when submitted.

# ---------------------------
# 1) Create the Flask app
# ---------------------------
app = Flask(__name__)
# Flask(__name__) creates the WSGI application object.
# __name__ helps Flask locate templates/static files relative to this module.

# ---------------------------
# 2) Configuration
# ---------------------------
# SECRET_KEY is used by Flask extensions (like Flask-WTF) to sign cookies and
# generate CSRF tokens. In production use a securely generated secret (not a
# hardcoded literal).
app.config['SECRET_KEY'] = 'mysecretkey'

# ---------------------------
# 3) Define a WTForms form
# ---------------------------
class ContactForm(FlaskForm):
    """
    ContactForm defines the fields and validation rules for the contact page.
    When instantiated in a view, Flask-WTF will:
     - populate fields from form data (POST)
     - provide helper methods like validate_on_submit()
     - supply a CSRF token automatically (hidden field)
    """
    name = StringField("Your Name", validators=[DataRequired()])
    submit = SubmitField("Send")

# ---------------------------
# 4) Routes (URL -> function)
# ---------------------------
@app.route('/')
def home():
    """
    Route for the home page.
    render_template('index.html'):
      - Flask finds 'templates/index.html'
      - Renders the template using Jinja2 and returns an HTTP response.
    """
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Route for the contact page. Accepts GET (show form) and POST (process form).
    The pattern:
      1. Instantiate the form object.
      2. If a POST occurred and the form validates, read the data and respond.
      3. Otherwise render the form template (showing validation errors if any).
    """
    form = ContactForm()  # instantiate; Flask-WTF binds request.form automatically
    message = None        # feedback message to show back on the page

    # validate_on_submit() returns True when:
    #  - the incoming request method is POST AND
    #  - the form passes all validators (e.g., DataRequired)
    if form.validate_on_submit():
        # Access form data via form.fieldname.data
        name = form.name.data
        # Create a friendly message to pass into the template
        message = f"Hello, {name}! Your form was submitted successfully."

        # NOTE: In a real app you might:
        #  - save the data to a DB
        #  - send an email
        #  - redirect to a 'success' page (use redirect(url_for(...))) to avoid re-submission

    # Render the contact template and provide form + message variables to Jinja2
    # The template can access `form` (for rendering fields) and `message`.
    return render_template('contact.html', form=form, message=message)


# ---------------------------
# 5) Run the app (development)
# ---------------------------
if __name__ == '__main__':
    # app.run(debug=True) starts the Werkzeug development server.
    # debug=True enables auto-reload and a helpful interactive debugger on exceptions.
    # IMPORTANT: Never set debug=True in production (exposes internals).
    app.run(debug=True)

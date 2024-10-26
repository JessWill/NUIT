from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, DateTimeField, IntegerField, FileField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange

# creates the login information
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

 # the registration form 
class RegistrationForm (FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    contact_number = IntegerField("Contact Number", validators=[InputRequired()])
    street_address = StringField("Street Address", validators=[InputRequired()])
    submit = SubmitField("Register")

# Event creation form
class EventForm(FlaskForm):
    event_name = StringField("Event Name", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    date_time = DateTimeField("Date and Time", format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])
    available_tickets = IntegerField("Available Tickets", validators=[InputRequired(), NumberRange(min=1, message="Must be a positive number")])
    image = FileField("Image", validators=[InputRequired()])
    category = SelectField("Category", choices=[
        ('House', 'House'), 
        ('Techno', 'Techno'), 
        ('Trance', 'Trance'), 
        ('Dubstep', 'Dubstep'), 
        ('Drum and Bass', 'Drum and Bass'), 
        ('Electro', 'Electro'), 
        ('Future Bass', 'Future Bass'), 
        ('Trap', 'Trap'), 
        ('Glitch Hop', 'Glitch Hop'), 
        ('Chillwave', 'Chillwave')
    ], validators=[InputRequired()])

    submit = SubmitField("Create Event")
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectMultipleField, DateTimeField, IntegerField, FileField, HiddenField
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
    contact_number = StringField("Contact Number", validators=[
        InputRequired(), 
        Length(min=10, max=15)
    ])
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
    categories= SelectMultipleField("categories", choices=[
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

    submit = SubmitField("Confirm")

# Comments form
class CommentForm(FlaskForm):
    text = TextAreaField("Comment", validators=[InputRequired(), Length(max=500)])
    submit = SubmitField("Post")

# Booking Form
class BookingForm(FlaskForm):
    quantity = IntegerField("Ticket Quantity", validators=[InputRequired(), NumberRange(min=1)])
    user_id = HiddenField("UserID", validators=[InputRequired()])
    event_id = HiddenField("EventID", validators=[InputRequired()])

    submit = SubmitField("Book Now")
from flask import Blueprint, render_template
from .forms import LoginForm, RegistrationForm, EventForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    register_form = RegistrationForm () 
    login_form = LoginForm()
    return render_template('index.html', register_form=register_form, login_form=login_form)

@main_bp.route('/create-event')
def create_event():
    event_form = EventForm()
    return render_template('create_event.html', event_form=event_form)

@main_bp.route('/event-details')
def event_details():
    return render_template('event_details.html')

@main_bp.route('/booking_history')
def booking_history():
    return render_template('booking_history.html')

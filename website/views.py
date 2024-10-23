from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/create-event')
def create_event():
    return render_template('create_event.html')

@main_bp.route('/event-details')
def event_details():
    return render_template('event_details.html')

@main_bp.route('/booking_history')
def booking_history():
    return render_template('booking_history.html')

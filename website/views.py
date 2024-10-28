from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from .forms import LoginForm, RegistrationForm, EventForm, BookingForm, CommentForm
from .models import Event, Booking, Comment

main_bp = Blueprint('main', __name__)

#Index page
@main_bp.route('/')
def index():
    register_form = RegistrationForm () 
    login_form = LoginForm()
    selected_categories = request.args.getlist('categories')

    if selected_categories:
        events = Event.query.filter(Event.categories.in_(selected_categories)).all()
    else:
        events = Event.query.all()

    return render_template('index.html', register_form=register_form, login_form=login_form, events=events)

#Create an event page
@main_bp.route('/create-event')
@login_required
def create_event():
    event_form = EventForm()
    return render_template('create_event.html', event_form=event_form)


#View event detail page
@main_bp.route('/event-details/<int:event_id>', methods=['GET', 'POST'])
def event_details(event_id):
    event = Event.query.get_or_404(event_id)
    comments = Comment.query.filter_by(event_id=event_id).all()
    comment_form = CommentForm()
    booking_form = BookingForm()  
    return render_template('event_details.html', event=event, comments=comments, comment_form=comment_form, booking_form=booking_form)

#view users booking history
@main_bp.route('/booking_history')
@login_required
def booking_history():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    print("Retrieved bookings:", bookings)
    return render_template('booking_history.html', bookings=bookings)

#view users created events
@main_bp.route('/user-events')
@login_required
def user_events():
    user_created_events = Event.query.filter_by(creator_id=current_user.id).all()
    return render_template('user_events.html', events=user_created_events)

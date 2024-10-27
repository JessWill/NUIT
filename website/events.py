from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import EventForm
from . import db
from .models import Event
from flask_login import login_required

event_bp = Blueprint('event_bp', __name__)

# Creating an event
@event_bp.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    event_form = EventForm()
    if event_form.validate_on_submit():
        selected_categories = ', '.join(event_form.category.data)

        new_event = Event(
            name=event_form.event_name.data,
            location=event_form.location.data,
            date=event_form.date_time.data,
            description=event_form.description.data,
            available_tickets=event_form.available_tickets.data,
            image=event_form.image.data,
            categories=selected_categories 
        )

        db.session.add(new_event)
        db.session.commit()
        print("Event created and added to database")
        flash('Event created successfully!', 'success')

        #redirect to the event details page of the newly created event
        return redirect(url_for('event_bp.event_details', event_id=new_event.id))
    else:
            print("Form is invalid:", event_form.errors)
    return render_template('create_event.html', event_form=event_form) 

#View an event
@event_bp.route('/event-details/<int:event_id>', methods=['GET', 'POST'])
def event_details(event_id):
    event = Event.query.get_or_404(event_id)
    comments = Comment.query.filter_by(event_id=event_id).all()
    return render_template('event_details.html', event=event, comments=comments)

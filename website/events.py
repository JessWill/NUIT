from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from .forms import EventForm, CommentForm, BookingForm
from . import db
from .models import Event, Comment, Booking
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

# This file is dedicated to actions performed on events, such as creating an event, viewing specific events, posting comments and booking. 

event_bp = Blueprint('event_bp', __name__)

# create an event
@event_bp.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    event_form = EventForm()
    if event_form.validate_on_submit():
        selected_categories = ', '.join(event_form.categories.data)

        #save file to img folder
        file = event_form.image.data
        file_name = secure_filename(file.filename)
        file_path= os.path.join(current_app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)

        new_event = Event(
            name=event_form.event_name.data,
            location=event_form.location.data,
            date=event_form.date_time.data,
            description=event_form.description.data,
            available_tickets=event_form.available_tickets.data,
            image=file_path,
            creator_id=current_user.id,
            categories=selected_categories 
        )

        db.session.add(new_event)
        db.session.commit()
        print("Event created and added to database")
        flash('Event created successfully!', 'success')

        #redirect to the event details page of the newly created event
        return redirect(url_for('main.event_details', event_id=new_event.id))
    else:
            print("Form is invalid:", event_form.errors)
    return render_template('create_event.html', event_form=event_form) 


# Comment on an event
@event_bp.route('/event-details/<int:event_id>/add-comment', methods=['POST'])
@login_required
def post_comment(event_id):
    event = Event.query.get_or_404(event_id)
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(
            text=form.text.data,
            event_id=event_id,
            user_id=current_user.id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash("Comment Posted 👍", "success")
        return redirect(url_for('main.event_details', event_id=event_id))
    comments = Comment.query.filter_by(event_id=event_id).all()
    return render_template('event_details.html', event=event, comments=comments, comment_form=form)

# book  an event
@event_bp.route('/event-details/<int:event_id>/book-event', methods=['POST'])
@login_required
def book_event(event_id):
    form = BookingForm()
    if form.validate_on_submit():
        new_booking = Booking(
             event_id =event_id,
             user_id=current_user.id,
             quantity=form.quantity.data,
        )
        db.session.add(new_booking)
        db.session.commit()

        flash("You're booked in 👍", "Success")
        return redirect(url_for('main.event_details', event_id=event_id))
    else:
         flash("Booking Failed 😭", "danger")
         print("Form errors:", form.errors)
         return redirect(url_for('main.event_details', event_id=event_id))

from flask import Blueprint, flash, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from .forms import LoginForm, RegistrationForm
from . import db

# Create a blueprint 
auth_bp = Blueprint('auth', __name__)

# Registration route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Registration successful! :)', 'success')
        return redirect(url_for('main.index'))

    print(form.errors)
    flash('Registration was not Successful ):', 'danger')
    return redirect(url_for('main.index'))

# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None 
    
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = db.session.scalar(db.select(User).where(User.email == email))

        if user is None:
            error = 'Incorrect user name'
        elif not check_password_hash(user.password_hash, password):
            error = 'Incorrect password'

        if error is None:
            login_user(user)
            nextp = request.args.get('next')
            if not nextp or not nextp.startswith('/'):
                return redirect(url_for('main.index'))
            return redirect(nextp)
        else:
            flash(error, 'error')

    return redirect(url_for('main.index'))

## Logout Route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bye! You have been logged out.', 'info')
    return redirect(url_for('main.index'))
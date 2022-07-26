# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
to create all routes for webpage login module

'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

from flask import Blueprint, render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth=Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                flash('Logged in', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash(f'UserName:{form.username.data} does not exist, please register first!', category='error')
    return render_template("login.html", form=form) #"<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    #flash(form.errors)
    # to make sure user doesn't already exist!
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        flash(f'{user.username} already exist!', category='error')
    else:
        if form.validate_on_submit():
            new_user=User(username=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('views.home'))
    return render_template("register.html", title='Register', form=form) #"<p>Sign Up</p>"
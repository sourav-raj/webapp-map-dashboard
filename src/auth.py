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
    return render_template("login.html", var1='Testing variable') #"<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    print(form.password.data, form.validate_on_submit())
    #flash(form.errors)
    if form.validate_on_submit():
        print('dfdssd', form.username.data)
        new_user=User(username=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('views.home'))
    return render_template("register.html", title='Register', form=form) #"<p>Sign Up</p>"
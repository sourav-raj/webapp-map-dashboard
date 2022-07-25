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
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form) #"<p>Sign Up</p>"
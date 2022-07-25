# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
to create all routes for webpage login module

'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

from flask import Blueprint, render_template
auth=Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", var1='Testing variable') #"<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup')
def signup():
    return render_template("signup.html") #"<p>Sign Up</p>"
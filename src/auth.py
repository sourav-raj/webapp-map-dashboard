# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
to create all routes for webpage login module

'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

from flask import Blueprint
auth=Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup')
def signup():
    return "<p>Sign Up</p>"
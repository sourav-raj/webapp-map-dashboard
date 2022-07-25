# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
to create all routes for the webpage except login module

'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

from flask import Blueprint, render_template
views=Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")  #'<h1>Test</h1>'

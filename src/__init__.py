# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
initial setup

'''

__version__ = '1.0.1'
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import imp
from flask import Flask
def create_app():
    app=Flask(__name__)
    app.config['SECRET-KEY']='f4ed13e80a7276c8501a6fc19291ad38'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app
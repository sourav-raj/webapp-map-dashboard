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
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'f4ed13e80a7276c8501a6fc19291ad38'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    create_database(app)

    return app

def create_database(app):
    '''
    if database don't exist, create one
    '''
    if not path.exists('src/'+DB_NAME):
        db.create_all(app=app)
        print('Database Created!')
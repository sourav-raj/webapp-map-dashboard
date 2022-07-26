# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
for database connection

'''

__version__ = '1.0.1'
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

from . import db
from flask_login import UserMixin
from sqlalchemy import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f"User:'{self.username}'"



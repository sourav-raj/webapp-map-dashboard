# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
main file
'''

__version__ = '1.0.0'
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

from src import create_app

app=create_app()
if __name__=='__main__':
    app.run(debug=True)
    
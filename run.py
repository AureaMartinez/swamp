# -*- coding: utf-8 -*-
#!flask/bin/python

#Launches the app

from app import app
app.run(debug=True) #This would be false when we don't want people to make changes to our code/website


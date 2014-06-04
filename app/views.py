#-*-coding: utf-8-*-

from app import app, db
from flask import Flask, render_template, redirect 
from models import Post, User
from forms import NewUserForm


@app.route('/')
def what():           
	all_users=User.query.all()
	posts = Post.query.all()
	return render_template("what.html", users= all_users, posts = posts)

@app.route('/add_user', methods = ['GET','POST'])
def add_user():
		form=NewUserForm () #creating a new user
		if form.validate_on_submit(): #if all the areas in the form that NEED to be complete are go ahead and submit form 
			user=User() #setting up the database to receive the user
			form.populate_obj(user) #inserting the user info into the data
			db.session.add(user) #add
			db.session.commit() #commit
			return redirect('/') #go back to the page
		return render_template('add_user.html', form = form)

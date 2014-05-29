#-*-coding: utf-8-*-

from app import app
from flask import render_template
from models import Post


@app.route('/')
def what():           
	first_post = Post("Thursday came way too soon.", "Aurea", "I can't believe it's June!")
	second_post = Post ("Tomorrow I will cook","Aurea", "Food is important.")

	return render_template("what.html", posts = [first_post, second_post])
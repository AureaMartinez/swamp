from flask.ext.wtf import Form #calling to use form
from wtforms import TextField #calling to use textfield to input user info
from wtforms.validators import Required

class NewUserForm (Form):
	firstname = TextField('firstname') #wants for user to input stated info
	lastname= TextField('lastname')
	username=TextField('username', validators=[Required()]) #this means that inorder for the form to be submitted you MUST fill this out!
#This file actually creates the database with models we have defined in models.py


from config import SQLALCHEMY_DATABASE_URI
from app import db
db.create_all() 


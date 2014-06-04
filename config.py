import os 
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/swampdb"

CSRF_ENABLED = True #session will be timed out if user doesn't use it for a period of time (like on-line banking)

SECRET_KEY = 'big-secret' #a password for you to go back and edit the code (rarely happens)
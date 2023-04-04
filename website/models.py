# Create database models

# When importing from . it is importing from the package (website). It can access anything defined in the __init__.py, where db is defined

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # Func gets current date and time and stores it as default
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # One to many relationship
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    # primary key which is unique, typically an integer
    id = db.Column(db.Integer, primary_key=True)

    # When defining a string one needs to pick a maximum length (150 here)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    # Every time creating a note this list stores all notes
    notes = db.relationship("Note")
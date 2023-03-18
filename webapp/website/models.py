from . import db 
#custom class to give user object specific for our flask login
from flask_login import UserMixin
from sqlalchemy.sql import func



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    #Linking Note(child) and User(parent) information through a foreign key
    #Referencing User class (small letter in sql) and referencing the id variable
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    #When referencing class using relationship use capital letters
    notes = db.relationship('Note')


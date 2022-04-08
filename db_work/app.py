from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def create():
    with app.app_context():
        db.create_all()

def add():
    user = Users(username="Aliev", password="qwerty")

    with app.app_context():
        db.session.add(user)
        db.session.commit()

def get():

    with app.app_context():

        user = Users.query.all()

        user = Users.query.filter_by(username="Aliev").all() # .first() \ .count() \

        user = Users.query.order_by(Users.username).all()

        user = Users.query.order_by(Users.username.desc()).all()    # сортировка списка

        user = Users.query.filter(Users.id != 1).all()

        user = Users.query.filter(
            Users.username.in_(
                ["Aliev"]
            )
        ).all()

        # JOIN = db.session.query(Flight, Passenger).filter(
        #     Flight.id == Passenseg.flight_id).all()

    print(user)

def set():
    with app.app_context():

        user = Users.query.filter_by(username="Aliev").first()
        user.password = "NewPassword"
        db.session.commit()

def delete():

    with app.app_context():
        user = Users.query.get(1)
        db.session.delete(user)
        db.session.commit()

get()
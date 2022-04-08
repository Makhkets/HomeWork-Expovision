import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}:{self.username}:{self.password}:{self.date}"

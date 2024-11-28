"""CRUD operations."""

from model import User, Sport, Athlete, QuizAnswer
from model import db, connect_to_db
from flask import render_template

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()

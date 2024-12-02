"""CRUD operations."""

from model import User, Sport, Athlete, QuizAnswer
from model import db, connect_to_db
from flask import render_template

def create_user(username, email, password):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_username(username):
    """Return a user by username."""
    return User.query.filter(User.username == username).first()

def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by id."""
    return User.query.filter(User.user_id == user_id).first()

def get_sports():
    """Return all sports."""
    return Sport.query.all()

def get_sport_by_id(sport_id):
    """Return a sport by id."""
    return Sport.query.filter(Sport.sport_id == sport_id).first()

def get_athletes():
    """Return all athletes."""
    return Athlete.query.all()

def get_athlete_by_id(athlete_id):
    """Return an athlete by id."""
    return Athlete.query.filter(Athlete.athlete_id == athlete_id).first()

def get_quiz_answers():
    """Return all quiz answers."""
    return QuizAnswer.query.all()

def get_quiz_answer_by_id(quiz_answer_id):
    """Return a quiz answer by id."""
    return QuizAnswer.query.filter(QuizAnswer.quiz_answer_id == quiz_answer_id).first()

def create_quiz_answer(user_id, sport_id, quiz_responses, match_percentage):
    """Create and return a new quiz answer."""
    quiz_answer = QuizAnswer(user_id=user_id, sport_id=sport_id, quiz_responses=quiz_responses, match_percentage=match_percentage)
    db.session.add(quiz_answer)
    db.session.commit()
    return quiz_answer



if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()

"""Models for Odyssey website."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    quiz_answers = db.relationship("QuizAnswer", back_populates="user", lazy=True)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Sport(db.Model):
    """A sport."""

    __tablename__ = "sports"

    sport_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sport_name = db.Column(db.String, unique=True)
    sport_description = db.Column(db.String)

    athletes = db.relationship("Athlete", back_populates="sport", lazy=True) 
    quiz_answers = db.relationship("QuizAnswer", back_populates="sport", lazy=True)
    
    def __repr__(self):
        return f"<Sport sport_id={self.sport_id} sport_name={self.sport_name}>"

class Athlete(db.Model):
    """An athlete."""

    __tablename__ = "athletes"

    athlete_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    athlete_name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=True)
    socials = db.Column(db.String, nullable=True)
    diet = db.Column(db.String, nullable=True) 

    sport_id = db.Column(db.Integer, db.ForeignKey("sports.sport_id"), nullable=False)
    sport = db.relationship("Sport", back_populates="athletes", lazy=True)

    def __repr__(self):
        return f"<Athlete athlete_id={self.athlete_id} athlete_name={self.athlete_name}>"

class QuizAnswer(db.Model):
    """Quiz answers for a user."""

    __tablename__ = "quiz_answers"  

    answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.sport_id"), nullable=False)
    quiz_answers = db.Column(db.JSON, nullable=False)

    user = db.relationship("User", back_populates="quiz_answers", lazy=True)
    sport = db.relationship("Sport", back_populates="quiz_answers", lazy=True)

    def __repr__(self):
        return f"<QuizAnswer quiz_answer_id={self.quiz_answer_id} user_id={self.user_id}>"

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///activities"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to the db!")
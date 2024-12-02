"""Server for Odyssey app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, url_for 
from model import connect_to_db, db 
from model import User, Sport, Athlete, QuizAnswer
from jinja2 import StrictUndefined 
import crud
from question_mapping import question_mapping

app = Flask(__name__)  
app.app_context().push()  

app.secret_key = "Rita" 
app.jinja_env.undefined = StrictUndefined  

@app.route('/')
def homepage():
    """Say something like Start the quizz"""
    return render_template('homepage.html')

@app.route('/quiz')
def quiz():
    """Display the quiz questions."""
    return render_template('quiz.html')

@app.route('/quiz-results')
def quiz_results():
    """Display the quiz results."""
    return render_template('quiz_results.html')

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
   
   user_answers = request.form
   sport_scores = {}

   for sport in ["MMA", "Muay_Thai", "Boxing", "Wrestling", "Jiu_Jitsu", "Basketball", "Soccer", "Volleyball", "Baseball", "Football", "Running", "Biking", "Swimming", "Triathlon", "Tennis", "Rock_Climbing", "Yoga", "Crossfit", "Powerlifting", "Gymnastics"]:
      sport_scores[sport] = 0

    for question, answer, in user_answers.items():
        if question in question_mapping:
            if answer.lower() == "yes":
                for sport in question_mapping[question]["yes"]:
                    sport_scores[sport] += 1
            else:
                for sport in question_mapping[question]["no"]:
                    sport_scores[sport] -= 1
    
    # Calculate the total score for each sport
    sorted_sports = sorted(sport_scores.items(), key=lambda x: x[1], reverse=True)

    # Get the top 3 sports
    top_sports = [sport for sport, score in sorted_sports[:3]]

    return render_template('quiz_results.html', sports=sorted_sports)

if __name__ == "__main__":
    connect_to_db(app) 
    app.run(host="0.0.0.0", debug=True, port=6060)
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

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Display the quiz questions or process the answers."""

    if request.method == 'POST':
        print(request.form) 
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        user_answers = request.form

        sport_scores = {sport: 0 for sport in question_mapping.values()}

        for question, answer in user_answers.items():
            if question in question_mapping:
                if answer.lower() == "yes":
                    for sport in question_mapping[question]["yes"]:
                        sport_scores[sport] += 1
                elif answer in question_mapping[question]:
                    for sport in question_mapping[question][answer]:
                        sport_scores[sport] += 1

        sorted_sports = sorted(sport_scores.items(), key=lambda x: x[1], reverse=True)
        top_sports = [sport for sport, score in sorted_sports[:3]]

        return render_template('quiz_results.html', sports=top_sports, name=user_name, email=user_email)

    return render_template('quiz.html', question_mapping=question_mapping)

@app.route('/quiz-results', methods=['GET'])
def quiz_results():
    """Display the quiz results."""
    sports = request.args.getlist('sports').split(',')   
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('quiz_results.html', sports=sports, name=name, email=email)

@app.route('/sports-page')
def sports_page():
    """Display the sports page."""
    return render_template('sports_page.html')

@app.route('/athletes-page')
def athletes_page():
    """Display the athletes page."""
    return render_template('athletes_page.html')

@app.route('/calorie-calculator')
def calorie_calculator():
    """Display the calorie calculator page."""
    return render_template('calorie_calculator.html')

if __name__ == "__main__":
    connect_to_db(app) 
    app.run(host="0.0.0.0", debug=True, port=6060)

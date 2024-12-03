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

        sport_scores = {sport: 0 for sport in set(
            sport for question in question_mapping.values()
            for sport_list in question.values() for sport in sport_list
        )}

        for question, answer in user_answers.items():
            if question in question_mapping:
                if answer.lower() == "yes":
                    for sport in question_mapping[question]["yes"]:
                        sport_scores[sport] += 1
                elif answer.lower() == "no":
                    for sport in question_mapping[question]["no"]:
                        sport_scores[sport] -= 1
                else:
                    if answer in question_mapping[question]:
                        for sport in question_mapping[question][answer]:
                            sport_scores[sport] += 1

        sorted_sports = sorted(sport_scores.items(), key=lambda x: x[1], reverse=True)
        top_sports = [sport for sport, score in sorted_sports[:3]]

        sports_data = {}
        for sport in top_sports:
            sports_obj = Sport.query.filter_by(sport_name=sport).first()
            athletes = Athlete.query.filter_by(sport_id=sports_obj.sport_id).all()
            sports_data[sport] = {
                'description': sports_obj.description,
                'athletes': athletes
            }

        return render_template('quiz_results.html', sports=top_sports, name=user_name, email=user_email, sports_data=sports_data)

    return render_template('quiz.html', question_mapping=question_mapping)

@app.route('/quiz-results', methods=['GET', 'POST'])
def quiz_results():
    """Display the quiz results."""
    if request.method == 'POST':
        sports = request.form.getlist('sports') 
        name = request.form.get('name')
        email = request.form.get('email')
    else:
        # Handle the GET request
        sports = request.args.getlist('sports')   
        name = request.args.get('name')
        email = request.args.get('email')

    return render_template('quiz_results.html', sports=sports, name=name, email=email)

if __name__ == "__main__":
    connect_to_db(app) 
    app.run(host="0.0.0.0", debug=True, port=6060)

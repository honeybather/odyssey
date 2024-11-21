"""Server for Odyssey app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify, url_for ) 
from model import connect_to_db, db 
#from model import db, User, Category, Activity, Event, BucketList, ExpertAdvice
from jinja2 import StrictUndefined 
import crud

app = Flask(__name__) # Create an instance of Flask with the name of the module
app.app_context().push() # Push the application context to be able to use Flask extensions outside of request handlers

app.secret_key = "Rita" # for session management 
app.jinja_env.undefined = StrictUndefined  
# Ensure undefined variables in Jinja templates trigger errors (helps debugging)

@app.route('/')
def homepage():
    """Say something like Start the quizz"""
    return render_template('homepage.html')

"""
# i think i want it to be one page
# click, screen changes, click, screen changes, you can go back if made a mistake
# and when you get your final answer, it would say, want to share w a friend?
# or take me back home (start quiz) 
"""

if __name__ == "__main__":
    connect_to_db(app) # Connect to the database using the app instance
    app.run(host="0.0.0.0", debug=True, port=6060)
    # Run the Flask application on the specified host, enable debugging, and set the port number
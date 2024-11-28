"""Script to seed database with sports and athletes data."""

from model import db, connect_to_db 
from sport_seed_data import MMA, Muay_Thai, Boxing, Wrestling, Jiu_Jitsu, Basketball, Soccer, Volleyball, Baseball, Football, Running, Biking, Swimming, Triathlon, Tennis, Rock_Climbing, Yoga, Crossfit, Powerlifting, Gymnastics
from athletes_seed_data import create_athletes
from server import app 

def seed_sports():
    db.create_all()

    db.session.add_all([MMA, Muay_Thai, Boxing, Wrestling, Jiu_Jitsu, Basketball, Soccer, Volleyball, Baseball, Football, Running, Biking, Swimming, Triathlon, Tennis, Rock_Climbing, Yoga, Crossfit, Powerlifting, Gymnastics])
    db.session.commit()

def seed_athletes():
    create_athletes()

if __name__ == "__main__":
    connect_to_db(app)
    seed_sports()
    seed_athletes()


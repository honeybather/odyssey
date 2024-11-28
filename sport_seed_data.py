from flask import Flask
from model import db, Sport, connect_to_db

app = Flask(__name__)

MMA = Sport(
    sport_name="MMA",
    sport_description="Mixed Martial Arts is the ultimate battlefield where fighters blend brutal strikes, intense grappling, and tactical submissions in an electrifying contest of skill and power.",
    intensity_level="high",
    environment="cage, ring, gym", 
    sport_type="solo",
    primary_focus="skill",
    is_combat=True,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Muay_Thai = Sport(
    sport_name="Muay Thai",
    sport_description="Muay Thai, the art of eight limbs, is a ferocious striking art that utilizes punches, kicks, elbows, and knees in a seamless blend of power, precision, and timing.",
    intensity_level="high",
    environment="ring",
    sport_type="solo",
    primary_focus="skill",
    is_combat=True,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Boxing = Sport(
    sport_name="Boxing",
    sport_description="Boxing is a brutal yet elegant combat sport that centers on precision punches, footwork, and the mental fortitude required to outlast your opponent.",
    intensity_level="high",
    environment="ring",
    sport_type="solo",
    primary_focus="skill",
    is_combat=True,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Wrestling = Sport(
    sport_name="Wrestling",
    sport_description="Wrestling is a contest of sheer power, balance, and technique where every move and counter tests endurance, flexibility, and brute force.",
    intensity_level="high",
    environment="mat",
    sport_type="solo",
    primary_focus="strength, technique, endurance",
    is_combat=True,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Jiu_Jitsu = Sport(
    sport_name="Jiu-Jitsu",
    sport_description="Jiu-Jitsu is the chess match of combat sports, where technique overpowers brute strength, allowing smaller fighters to outmaneuver larger opponents with precision and fluidity.",
    intensity_level="medium",
    environment="mat",
    sport_type="solo",
    primary_focus="skill",
    is_combat=True,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Basketball = Sport(
    sport_name="Basketball",
    sport_description="Basketball is a fast-paced, high-flying spectacle where agility, strategy, and teamwork collide in a race down the court for electrifying points.",
    intensity_level="high",
    environment="court",
    sport_type="team",
    primary_focus="endurance",
    is_combat=False,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Soccer = Sport(
    sport_name="Soccer",
    sport_description="Soccer is the world's most beloved sport, where every pass, dribble, and goal shifts the tide of a match through speed, endurance, and tactical brilliance.",
    intensity_level="high",
    environment="field",
    sport_type="team",
    primary_focus="agility",
    is_combat=False,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Volleyball = Sport(
    sport_name="Volleyball",
    sport_description="Volleyball is a high-flying, fast-paced game where reflexes and teamwork come together to create magical moments of spiking, serving, and blocking.",
    intensity_level="medium",
    environment="court",
    sport_type="team",
    primary_focus="agility",
    is_combat=False,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=False,
)

Baseball = Sport(
    sport_name="Baseball",
    sport_description="Baseball is a fast-paced team sport involving hitting, pitching, and fielding, where strategy and precision are key to scoring runs and defending bases.",
    intensity_level="moderate",
    environment="field",
    sport_type="team",
    primary_focus="agility",
    is_combat=False,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=True,
)

Football = Sport(
    sport_name="Football",
    sport_description="Football is a high-intensity team sport where strategy, speed, and strength combine in a battle for the end zone, with thrilling tackles and passes defining the game.",
    intensity_level="high",
    environment="field",
    sport_type="team",
    primary_focus="strength",
    is_combat=False,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=True,
)

Running = Sport(
    sport_name="Running",
    sport_description="Running is a versatile, straightforward sport focused on endurance and speed, challenging athletes to go further and faster, whether in sprints or marathons.",
    intensity_level="medium",
    environment="outdoor",
    sport_type="solo",
    primary_focus="endurance",
    is_combat=False,
    is_strategic=False,
    is_competitive=True,
    is_outdoor=True,
)

Biking = Sport(
    sport_name="Biking",
    sport_description="Biking is an exhilarating outdoor activity that combines endurance and speed, with cycling competitions challenging athletes to conquer tough terrains and race against the clock.",
    intensity_level="medium",
    environment="outdoor",
    sport_type="solo",
    primary_focus="endurance",
    is_combat=False,
    is_strategic=False,
    is_competitive=True,
    is_outdoor=True,
)

Swimming = Sport(
    sport_name="Swimming",
    sport_description="Swimming is a refreshing yet demanding sport that tests endurance and technique as athletes race through water in individual and relay events.",
    intensity_level="high",
    environment="pool",
    sport_type="solo",
    primary_focus="endurance",
    is_combat=False,
    is_strategic=False,
    is_competitive=True,
    is_outdoor=False,
)

Triathlon = Sport(
    sport_name="Triathlon",
    sport_description="Triathlon is the ultimate test of endurance, combining swimming, biking, and running over long distances in one grueling race that pushes athletes to their physical and mental limits.",
    intensity_level="very high",
    environment="outdoor",
    sport_type="solo",
    primary_focus="endurance",
    is_combat=False,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=True,
)

Tennis = Sport(
    sport_name="Tennis",
    sport_description="Tennis is an exciting individual or team sport where precision, speed, and strategy define the game, with players competing to outwit each other in fast-paced rallies.",
    intensity_level="high",
    environment="court",
    sport_type="solo or team",
    primary_focus="agility",
    is_combat=False,
    is_strategic=True,
    is_competitive=True,
    is_outdoor=True,
)

Rock_Climbing = Sport(
    sport_name="Rock Climbing",
    sport_description="Rock climbing is a physically and mentally demanding sport that requires strength, endurance, and problem-solving skills to ascend vertical rock faces or indoor walls.",
    intensity_level="high",
    environment="gym",
    sport_type="solo",
    primary_focus="strength",
    is_combat=False,
    is_strategic=False,
    is_competitive=False,
    is_outdoor=True,
)

Yoga = Sport(
    sport_name="Yoga",
    sport_description="Yoga is a holistic practice combining breath control, flexibility, and mindfulness, offering a calming yet challenging experience to strengthen both body and mind.",
    intensity_level="low",
    environment="studio",
    sport_type="solo",
    primary_focus="flexibility",
    is_combat=False,
    is_strategic=False,
    is_competitive=False,
    is_outdoor=True,
)

Powerlifting = Sport(
    sport_name="Powerlifting",
    sport_description="Powerlifting is a raw display of strength, focusing on the squat, bench press, and deadlift to challenge the limits of human power and technique.",
    intensity_level="high",
    environment="gym",
    sport_type="solo",
    primary_focus="strength",
    is_combat=False,
    is_strategic=False,
    is_competitive=True,
    is_outdoor=False,
)

Crossfit = Sport(
    sport_name="Crossfit",
    sport_description="Crossfit is a high-intensity workout combining weightlifting, cardio, and bodyweight exercises designed to push athletes to their peak fitness and endurance levels.",
    intensity_level="very high",
    environment="gym",
    sport_type="solo",
    primary_focus="endurance",
    is_combat=False,
    is_strategic=False,
    is_competitive=True,
    is_outdoor=False,
)

Gymnastics = Sport(
    sport_name="Gymnastics",
    sport_description="Gymnastics is a dynamic and graceful sport requiring strength, flexibility, and precision to perform routines on various apparatus and floor exercises.",
    intensity_level="high",
    environment="gym",
    sport_type="solo",
    primary_focus="coordination",
    is_combat=False,
    is_strategic=False,
    is_competitive=True,
    is_outdoor=False,
)

if __name__ == "__main__":
    connect_to_db(app)
    # clear existing data
    db.drop_all()
    db.create_all()
    
    # add all sport objects to the session and commit
    db.session.add_all([MMA, Muay_Thai, Boxing, Wrestling, Jiu_Jitsu, Basketball, 
                       Soccer, Volleyball, Baseball, Football, Running, Biking, 
                       Swimming, Ironman, Tennis, Rock_Climbing, Yoga, Powerlifting, 
                       Crossfit, Gymnastics])
    db.session.commit()


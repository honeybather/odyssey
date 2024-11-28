from flask import Flask
from model import db, Sport, Athlete, connect_to_db
from sport_seed_data import MMA, Muay_Thai, Boxing, Wrestling, Jiu_Jitsu, Basketball, Soccer, Volleyball, Baseball, Football, Running, Biking, Swimming, Triathlon, Tennis, Rock_Climbing, Yoga, Crossfit, Powerlifting, Gymnastics

app = Flask(__name__)

def clear_database():
    """Clear existing data from tables."""
    # clear tables in reverse order of dependencies
    Athlete.query.delete()
    Sport.query.delete()
    db.session.commit()

def create_athletes():

    mma = Sport.query.filter_by(sport_name="MMA").first()

    viviane_araujo = Athlete(
        athlete_name="Viviane Araújo",
        sport_id=mma.sport_id,
        bio="A passionate and resilient fighter, blending grit and grace with an unwavering dedication to her craft and a deep connection to her Brazilian roots.",
        socials="@viviaraujomma",
        diet="Clean eating, high protein"
    )
    john_jones = Athlete(
        athlete_name="Jon Jones",
        sport_id=mma.sport_id,
        bio="A fiercely competitive and unapologetically bold fighter, combining unmatched skill with a larger-than-life personality that keeps fans and rivals on edge.",
        socials="@jonnybones",
        diet="Balanced diet with a focus on lean protein and healthy fats"
    )
    khabib_nurmagomedov = Athlete(
        athlete_name="Khabib Nurmagomedov",
        sport_id=mma.sport_id,
        bio="A humble yet relentless warrior, grounded in discipline and faith, who dominates with precision and unshakable determination.",
        socials="@khabib_nurmagomedov",
        diet="Traditional Dagestani diet, high in protein and low in processed foods"
    )
    israel_adesanya = Athlete(
        athlete_name="Israel Adesanya",
        sport_id=mma.sport_id,
        bio="A charismatic and creative powerhouse, blending striking artistry with a confident, playful swagger that captivates fans worldwide.",
        socials="@stylebender",
        diet="Focus on clean, whole foods with an emphasis on lean proteins and vegetables"
    )

    muay_thai = Sport.query.filter_by(sport_name="Muay Thai").first()

    rodtang = Athlete(
        athlete_name="Rodtang Jitmuangnon",
        sport_id=muay_thai.sport_id,
        bio="A fearless and electrifying Muay Thai phenom, known for his aggressive fighting style, unbreakable spirit, and infectious charisma.",
        socials="@rodtang_jimungnon",
        diet="High-carb, protein-packed meals to fuel intense training sessions"
    )

    tawanchai_pk_saenchai = Athlete(
        athlete_name="Tawanchai PK Saenchai",
        sport_id=muay_thai.sport_id,
        bio="A rising Muay Thai star with a calm and composed demeanor, pairing technical brilliance with sharp precision in the ring.",
        socials="@tawanchay_pk",
        diet="Traditional Thai meals balanced with lean proteins and fresh vegetables"
    )

    jackie_buntan = Athlete(
        athlete_name="Jackie Buntan",
        sport_id=muay_thai.sport_id,
        bio="A determined and focused striker, blending Filipino-American heritage with dynamic techniques and an unrelenting drive to excel.",
        socials="@jackiebuntan",
        diet="Clean, whole foods with an emphasis on recovery and performance"
    )

    janet_todd = Athlete(
        athlete_name="Janet Todd",
        sport_id=muay_thai.sport_id,
        bio="A disciplined and versatile champion, known for her sharp combinations, mental toughness, and inspiring work ethic both inside and outside the ring.",
        socials="@jmcoakle",
        diet="Balanced diet with an emphasis on hydration and nutrient timing"
    )

    boxing = Sport.query.filter_by(sport_name="Boxing").first()
    
    amanda_serrano = Athlete(
        athlete_name="Amanda Serrano",
        sport_id=boxing.sport_id,
        bio="A trailblazing champion with unmatched versatility and relentless determination, combining humility with a fierce passion for breaking barriers in women's boxing.",
        socials="@serranosisters",
        diet="Focused on lean protein and nutrient-rich foods to maintain peak performance"
    )

    ryan_garcia = Athlete(
        athlete_name="Ryan Garcia",
        sport_id=boxing.sport_id,
        bio="A charismatic and lightning-fast fighter, blending sharp technique with a social media-savvy personality that redefines boxing stardom.",
        socials="@kingryan",
        diet="High-protein meals with clean carbs for sustained energy"
    )

    canelo_alvarez = Athlete(
        athlete_name="Canelo Álvarez",
        sport_id=boxing.sport_id,
        bio="A disciplined and powerful icon of boxing, celebrated for his unparalleled work ethic, tactical brilliance, and relentless pursuit of greatness.",
        socials="@canelo",
        diet="Tailored diet focused on precision nutrition and peak conditioning"
    )

    katie_taylor = Athlete(
        athlete_name="Katie Taylor",
        sport_id=boxing.sport_id,
        bio="A humble yet tenacious trailblazer, combining unparalleled skill with a quiet confidence that has revolutionized women's boxing.",
        socials="@katie_t86",
        diet="Balanced meals emphasizing recovery and sustainable energy"
    )

    wrestling = Sport.query.filter_by(sport_name="Wrestling").first()

    amit_elor = Athlete(
        athlete_name="Amit Elor",
        sport_id=wrestling.sport_id,
        bio="A rising wrestling sensation known for her technical brilliance, calm composure, and relentless drive to make history on the mat.",
        socials="@amit.elor",
        diet="High-protein meals with nutrient-dense foods to fuel intense training and recovery"
    )

    roman_reigns = Athlete(
        athlete_name="Roman Reigns",
        sport_id=wrestling.sport_id,
        bio="A commanding and charismatic WWE superstar, blending raw power with unmatched presence as ‘The Tribal Chief’ in sports entertainment.",
        socials="@romanreigns",
        diet="Meticulous meal planning with an emphasis on lean proteins and performance-focused nutrition"
    )

    cody_rhodes = Athlete(
        athlete_name="Cody Rhodes",
        sport_id=wrestling.sport_id,
        bio="A passionate and resilient professional wrestler, combining legacy with a unique flair as ‘The American Nightmare,’ captivating fans worldwide.",
        socials="@americannightmarecody",
        diet="Balanced nutrition with a focus on muscle-building and sustained energy"
    )

    jordan_burroughs = Athlete(
        athlete_name="Jordan Burroughs",
        sport_id=wrestling.sport_id,
        bio="A legendary freestyle wrestler, revered for his explosive double-leg takedowns, unwavering dedication, and leadership on and off the mat.",
        socials="@alliseeisgold",
        diet="Clean eating with strategic carb-loading for high-intensity performance"
    )

    bjj = Sport.query.filter_by(sport_name="Jiu Jitsu").first()

    taelornmoore = Athlete(
        athlete_name="Taelorn Moore",
        sport_id=bjj.sport_id,
        bio="A passionate Brazilian Jiu-Jitsu practitioner blending creativity and resilience, known for inspiring others with unique perspectives on the art.",
        socials="@taelornmoore",
        diet="Balanced meals with an emphasis on recovery-focused nutrition"
    )

    isa_scheidt = Athlete(
        athlete_name="Isa Scheidt",
        sport_id=bjj.sport_id,
        bio="A rising star in the BJJ community, Isa is known for her dynamic techniques, infectious energy, and commitment to advancing women's grappling.",
        socials="@isa.scheidtbjj",
        diet="Nutrient-rich meals with a focus on endurance and energy"
    )

    john_danaher = Athlete(
        athlete_name="John Danaher",
        sport_id=bjj.sport_id,
        bio="A legendary coach and philosopher in Brazilian Jiu-Jitsu, renowned for his methodical teaching style and revolutionary approach to grappling.",
        socials="@danaherjohn",
        diet="High-protein, low-carb meals with meticulous attention to health and energy"
    )

    mikey_musumeci = Athlete(
        athlete_name="Mikey Musumeci",
        sport_id=bjj.sport_id,
        bio="A five-time world champion, celebrated for his technical mastery, humility, and dedication to elevating Brazilian Jiu-Jitsu globally.",
        socials="@mikeymusumeci",
        diet="High-protein and plant-based meals tailored for optimal performance and recovery"
    )

    basketball = Sport.query.filter_by(sport_name="Basketball").first()

    lebron_james = Athlete(
        athlete_name="LeBron James",
        sport_id=basketball.sport_id,
        bio="A basketball legend known for his leadership, versatility, and unmatched basketball IQ, inspiring generations on and off the court.",
        socials="@kingjames",
        diet="Lean proteins, complex carbs, and a focus on hydration for peak performance"
    )

    stephen_curry = Athlete(
        athlete_name="Stephen Curry",
        sport_id=basketball.sport_id,
        bio="A sharpshooting phenomenon revolutionizing basketball with his long-range accuracy and relentless work ethic.",
        socials="@stephencurry30",
        diet="Clean eating with an emphasis on energy-dense meals and recovery-focused nutrition"
    )

    maya_moore = Athlete(
        athlete_name="Maya Moore",
        sport_id=basketball.sport_id,
        bio="A trailblazing athlete and advocate, celebrated for her athleticism, leadership, and impact on and off the court.",
        socials="@mooremaya",
        diet="Whole foods with a focus on balance and energy for endurance"
    )

    aja_wilson = Athlete(
        athlete_name="A'ja Wilson",
        sport_id=basketball.sport_id,
        bio="A dominant force in women's basketball, known for her athleticism, leadership, and dedication to elevating the game.",
        socials="@ajawilson22",
        diet="Balanced meals with an emphasis on lean protein and healthy fats for strength and recovery"
    )

    soccer = Sport.query.filter_by(sport_name="Soccer").first()

    cristiano_ronaldo = Athlete(
        athlete_name="Cristiano Ronaldo",
        sport_id=soccer.sport_id,
        bio="One of the greatest footballers of all time, known for his incredible work ethic, athleticism, and numerous records in European football.",
        socials="@cristiano",
        diet="High-protein, low-carb diet with an emphasis on hydration and muscle recovery"
    )

    kylian_mbappe = Athlete(
        athlete_name="Kylian Mbappé",
        sport_id=soccer.sport_id,
        bio="A young football sensation known for his explosive speed, dribbling, and goal-scoring ability, Mbappé is a future star of world football.",
        socials="@k.mbappe",
        diet="Carb-rich meals for energy and muscle recovery, with a focus on hydration"
    )

    marta = Athlete(
        athlete_name="Marta",
        sport_id=soccer.sport_id,
        bio="Widely regarded as the greatest female footballer, known for her exceptional technique, vision, and leadership on the field.",
        socials="@martavsilva10",
        diet="A well-balanced diet rich in complex carbohydrates, lean protein, and healthy fats"
    )

    alexia_putellas = Athlete(
        athlete_name="Alexia Putellas",
        sport_id=soccer.sport_id,
        bio="A dynamic midfielder and captain for FC Barcelona, Putellas is known for her technical skills, vision, and leadership in women's football.",
        socials="@alexiaputellas",
        diet="Balanced diet focused on fueling performance and enhancing recovery"
    )

    volleyball = Sport.query.filter_by(sport_name="Volleyball").first()

    alana_walker = Athlete(
        athlete_name="Alana Walker",
        sport_id=volleyball.sport_id,
        bio="A talented volleyball player and social media influencer, known for blending athleticism with relatable and motivational TikTok content.",
        socials="@alana.walker",
        diet="Balanced meals with an emphasis on hydration and sustainable energy"
    )
    ella_may_powell = Athlete(
        athlete_name="Ella May Powell",
        sport_id=volleyball.sport_id,
        bio="Young American volleyball star combining her setting skills and social media presence to grow the sport’s popularity.",
        socials="@ellamaypowell",
        diet="Clean eating with a mix of carbs, proteins, and healthy fats to fuel competitive play"
    )
    matt_anderson = Athlete(
        athlete_name="Matt Anderson",
        sport_id=volleyball.sport_id,
        bio="A celebrated American volleyball star known for his versatility, incredible spiking, and leadership on and off the court.",
        socials="@mja504",
        diet="Balanced diet rich in lean protein, whole grains, and vegetables for peak performance"
    )
    aleksandar_nikolov = Athlete(
        athlete_name="Aleksandar Nikolov",
        sport_id=volleyball.sport_id,
        bio="A rising Bulgarian volleyball talent, showcasing his skills and training journey to inspire fans on TikTok.",
        socials="@aleksandar.nikolov",
        diet="Carb-heavy meals for energy, with a focus on lean proteins for muscle recovery"
    )

    baseball = Sport.query.filter_by(sport_name="Baseball").first()

    shohei_ohtani = Athlete(
        athlete_name="Shohei Ohtani",
        sport_id=baseball.sport_id,
        bio="A once-in-a-generation player, excelling as both a pitcher and hitter, Ohtani is redefining what's possible in modern baseball.",
        socials="@shoheiohtani",
        diet="High-protein meals with carbs for energy, focusing on post-game recovery"
    )

    mookie_betts = Athlete(
        athlete_name="Mookie Betts",
        sport_id=baseball.sport_id,
        bio="A dynamic outfielder known for his speed, precision, and leadership on the field, Betts inspires with his all-around excellence.",
        socials="@mookiebetts",
        diet="Clean eating with a focus on endurance and agility"
    )

    aj_andrews = Athlete(
        athlete_name="A.J. Andrews",
        sport_id=baseball.sport_id,
        bio="A groundbreaking athlete in softball, known for her fearless play and advocacy for women in sports.",
        socials="@aj_andrews",
        diet="Nutrient-dense meals that prioritize recovery and sustained energy"
    )

    olivia_pichardo = Athlete(
        athlete_name="Olivia Pichardo",
        sport_id=baseball.sport_id,
        bio="A groundbreaking American baseball player, recognized for being the first woman to make a Division I varsity baseball roster, inspiring future generations.",
        socials="@oliviapichardo",
        diet="Energy-packed meals with an emphasis on protein for strength and endurance"
    )
    
    football = Sport.query.filter_by(sport_name="Football").first()

    patrick_mahomes = Athlete(
        athlete_name="Patrick Mahomes",
        sport_id=football.sport_id,
        bio="An electrifying quarterback known for his incredible arm strength, creativity on the field, and ability to lead his team to victory under pressure.",
        socials="@patrickmahomes",
        diet="Lean proteins, vegetables, and healthy carbs to fuel game-day performance and recovery"
    )

    jalen_hurts = Athlete(
        athlete_name="Jalen Hurts",
        sport_id=football.sport_id,
        bio="A rising star quarterback celebrated for his dual-threat ability, mental toughness, and relentless dedication to improving his craft.",
        socials="@jalenhurts",
        diet="High-protein and nutrient-dense meals with a focus on endurance and energy"
    )

    haley_van_voorhis = Athlete(
        athlete_name="Haley Van Voorhis",
        sport_id=football.sport_id,
        bio="The first woman to play in a Division III men's football game, Van Voorhis is breaking barriers and inspiring women in football.",
        socials="@haleyvanvoorhis",
        diet="Nutrient-rich foods focused on maintaining strength, endurance, and overall fitness"
    )

    ilona_maher = Athlete(
        athlete_name="Ilona Maher",
        sport_id=football.sport_id,
        bio="A dominant force in women's rugby and American football, Maher is recognized for her versatility, strength, and leadership on the field.",
        socials="@ilonamaher",
        diet="Whole foods with a strong emphasis on protein, carbs, and hydration to maximize performance"
    )

    running = Sport.query.filter_by(sport_name="Running").first()

    usain_bolt = Athlete(
        athlete_name="Usain Bolt",
        sport_id=running.sport_id,
        bio="The fastest man in the world, Bolt is a legendary Jamaican sprinter known for his dominance in the 100m and 200m events.",
        socials="@usainbolt",
        diet="High-protein meals with a focus on recovery, supplemented by carbs to fuel sprints"
    )

    elyud_kipchoge = Athlete(
        athlete_name="Eliud Kipchoge",
        sport_id=running.sport_id,
        bio="A Kenyan long-distance runner, Kipchoge is regarded as the greatest marathoner of all time, having set the world record for the marathon.",
        socials="@kipchogeeliud",
        diet="A balanced diet rich in carbohydrates, proteins, and micronutrients to support endurance"
    )

    sifan_hassan = Athlete(
        athlete_name="Sifan Hassan",
        sport_id=running.sport_id,
        bio="A Dutch-Ethiopian long-distance runner, Hassan is known for her versatility, winning gold in the 5000m, 10000m, and the 1500m at the Tokyo Olympics.",
        socials="@sifanhassan",
        diet="Focused on plant-based, nutrient-dense meals to support stamina and recovery"
    )

    sha_carri_richardson = Athlete(
        athlete_name="Sha'Carri Richardson",
        sport_id=running.sport_id,
        bio="A bold and electrifying American sprinter known for her fierce competitiveness and charismatic personality, Richardson is a force to be reckoned with in the 100m and 200m.",
        socials="@itsmesha",
        diet="A combination of lean protein, carbs for energy, and healthy fats to maintain speed and strength"
    )

    biking = Sport.query.filter_by(sport_name="Biking").first()

    tadej_pogacar = Athlete(
        athlete_name="Tadej Pogačar",
        sport_id=biking.sport_id,
        bio="A Slovenian professional cyclist, Pogačar is a two-time winner of the Tour de France and known for his dominance in stage races and one-day classics.",
        socials="@pogacar_tadej",
        diet="High-energy meals with a mix of carbohydrates and proteins to support endurance and recovery during long stages"
    )

    van_der_poel = Athlete(
        athlete_name="Mathieu van der Poel",
        sport_id=biking.sport_id,
        bio="A Dutch professional cyclist, Van der Poel is a force in road racing, cyclocross, and mountain biking, known for his aggressive riding style and versatility.",
        socials="@mathieuvanderpoel",
        diet="Focus on high-carb meals for energy, along with protein-rich foods to aid in recovery and muscle building"
    )

    marianne_vos = Athlete(
        athlete_name="Marianne Vos",
        sport_id=biking.sport_id,
        bio="A Dutch professional cyclist, Vos is regarded as one of the greatest female cyclists in history, with numerous World Championship titles and Olympic medals.",
        socials="@mariannevosofficial",
        diet="A balance of carbohydrates, proteins, and fats, with emphasis on fueling long rides and ensuring recovery post-race"
    )

    kate_courtney = Athlete(
        athlete_name="Kate Courtney",
        sport_id=biking.sport_id,
        bio="An American professional mountain biker, Courtney is known for her world championship title and consistent success in cross-country mountain biking events.",
        socials="@kate_courtney",
        diet="Focused on maintaining a healthy balance of carbs, proteins, and hydration for peak performance in mountain biking"
    )

    swimming = Sport.query.filter_by(sport_name="Swimming").first()

    pan_zhanle = Athlete(
        athlete_name="Pan Zhanle",
        sport_id=swimming.sport_id,
        bio="A rising Chinese swimmer known for his impressive performances in freestyle sprint events, Pan Zhanle is setting new benchmarks in international swimming.",
        socials="@panzhanle",
        diet="A mix of carbs for energy and lean protein to build strength and recover after high-intensity training"
    )

    thomas_ceccon = Athlete(
        athlete_name="Thomas Ceccon",
        sport_id=swimming.sport_id,
        bio="An Italian swimmer and world champion in backstroke and medley events, Ceccon is celebrated for his versatility and record-breaking performances.",
        socials="@thomas_ceccon",
        diet="Balanced meals emphasizing protein, whole grains, and vegetables to maintain endurance and power"
    )

    summer_mcintosh = Athlete(
        athlete_name="Summer McIntosh",
        sport_id=swimming.sport_id,
        bio="A Canadian swimming prodigy, McIntosh has already shattered multiple world records and is known for her dominance in freestyle and individual medley events.",
        socials="@summermcintosh",
        diet="Focused on nutrient-dense foods with plenty of carbs, protein, and hydration to fuel her rapid growth and performance"
    )

    katie_ledecky = Athlete(
        athlete_name="Katie Ledecky",
        sport_id=swimming.sport_id,
        bio="An American swimming legend, Ledecky dominates long-distance freestyle events with multiple Olympic golds and world records to her name.",
        socials="@katieledecky",
        diet="A well-balanced diet centered on lean proteins, complex carbs, and healthy fats to support her incredible endurance and recovery"
    )

    triathlon = Sport.query.filter_by(sport_name="Triathlon").first()

    jan_frodeno = Athlete(
        athlete_name="Jan Frodeno",
        sport_id=triathlon.sport_id,
        bio="A German triathlete and Olympic gold medalist, Frodeno is a three-time Ironman World Champion, renowned for his exceptional endurance and consistency.",
        socials="@janfrodeno",
        diet="Balanced meals with a focus on lean protein, complex carbs, and hydration for peak endurance and recovery"
    )

    lucy_charles_barclay = Athlete(
        athlete_name="Lucy Charles-Barclay",
        sport_id=triathlon.sport_id,
        bio="A British triathlete and multiple-time Ironman World Championship runner-up, Charles-Barclay is celebrated for her dominance in the swimming leg and her strong all-round abilities.",
        socials="@lucycharles93",
        diet="High-carb meals with lean proteins and plenty of hydration to fuel her intense training and competition"
    )

    patrick_lange = Athlete(
        athlete_name="Patrick Lange",
        sport_id=triathlon.sport_id,
        bio="A German triathlete and two-time Ironman World Champion, Lange is known for his exceptional running leg and mental toughness in long-distance races.",
        socials="@patricklange1",
        diet="Carbohydrate-focused meals with adequate protein and electrolytes to sustain energy during long races"
    )

    laura_philipp = Athlete(
        athlete_name="Laura Philipp",
        sport_id=triathlon.sport_id,
        bio="A German triathlete and Ironman champion, Philipp is known for her powerful bike and run performances, as well as her consistent podium finishes in long-distance events.",
        socials="@laura_philipp_tri",
        diet="A carefully balanced diet focused on carbohydrates for energy, protein for recovery, and healthy fats to sustain endurance during training and racing"
    )

    tennis = Sport.query.filter_by(sport_name="Tennis").first()

    coco_gauff = Athlete(
        athlete_name="Coco Gauff",
        sport_id=tennis.sport_id,
        bio="An American tennis prodigy and Grand Slam champion, Gauff inspires with her powerful athleticism, mental maturity, and passion for the game.",
        socials="@cocogauff",
        diet="Healthy mix of proteins, carbs, and hydration to fuel her intense training and youthful energy"
    )

    serena_williams = Athlete(
        athlete_name="Serena Williams",
        sport_id=tennis.sport_id,
        bio="An American tennis icon and 23-time Grand Slam champion, Williams is celebrated for her power, resilience, and influence on and off the court.",
        socials="@serenawilliams",
        diet="Balanced meals rich in lean protein, vegetables, and whole grains to maintain strength and energy"
    )

    matteo_berrettini = Athlete(
        athlete_name="Matteo Berrettini",
        sport_id=tennis.sport_id,
        bio="An Italian tennis star known for his booming serve and powerful forehand, Berrettini is one of the most exciting players in the sport.",
        socials="@matberrettini",
        diet="Carb-focused meals with lean proteins and healthy fats to support strength and endurance on the court"
    )

    novak_djokovic = Athlete(
        athlete_name="Novak Djokovic",
        sport_id=tennis.sport_id,
        bio="A Serbian tennis legend and multiple Grand Slam champion, Djokovic dominates the game with his incredible flexibility, focus, and unmatched consistency.",
        socials="@djokernole",
        diet="Gluten-free, plant-rich diet emphasizing whole foods for optimal energy and recovery"
    )

    rock_climbing = Sport.query.filter_by(sport_name="Rock Climbing").first()

    natalia_grossman = Athlete(
        athlete_name="Natalia Grossman",
        sport_id=rock_climbing.sport_id,
        bio="An American climbing sensation, Grossman excels in bouldering and lead climbing, showcasing her strength, precision, and passion on the global stage.",
        socials="@natalia_grossman",
        diet="A protein-rich diet with plenty of healthy carbs to maintain energy and build strength for intense climbing sessions"
    )

    janja_garnbret = Athlete(
        athlete_name="Janja Garnbret",
        sport_id=rock_climbing.sport_id,
        bio="A Slovenian climbing legend and Olympic gold medalist, Garnbret is known for her dominance in competition climbing and graceful, fluid style.",
        socials="@janja_garnbret",
        diet="Balanced meals rich in protein, whole grains, and vegetables to sustain her high-intensity training and recovery"
    )

    toby_roberts = Athlete(
        athlete_name="Toby Roberts",
        sport_id=rock_climbing.sport_id,
        bio="A rising British climber, Roberts has impressed the world with his technical skills and fearless attitude in bouldering and lead climbing.",
        socials="@tobyrobertsclimbing",
        diet="Energy-dense meals focusing on carbs and proteins to fuel his dynamic climbing performance"
    )

    sorato_anraku = Athlete(
        athlete_name="Sorato Anraku",
        sport_id=rock_climbing.sport_id,
        bio="A young Japanese climbing prodigy, Anraku is celebrated for his remarkable composure, agility, and creativity in tackling challenging routes.",
        socials="@soratoanraku",
        diet="A nutrient-dense diet with a mix of carbs, proteins, and hydration to support his rapid growth and climbing stamina"
    )

    yoga = Sport.query.filter_by(sport_name="Yoga").first()

    adriene_mishler = Athlete(
        athlete_name="Adriene Mishler",
        sport_id=yoga.sport_id,
        bio="A global yoga icon and founder of 'Yoga with Adriene,' Mishler promotes mindfulness, self-care, and inclusivity through her approachable teaching style.",
        socials="@adrienelouise",
        diet="Whole-food, plant-focused diet, emphasizing balance and nourishment for the mind and body"
    )

    koya_webb = Athlete(
        athlete_name="Koya Webb",
        sport_id=yoga.sport_id,
        bio="A holistic health coach and yoga teacher, Webb inspires with her focus on mental clarity, self-love, and embracing life's challenges through yoga.",
        socials="@koyawebb",
        diet="Plant-based meals rich in greens, fruits, and healthy fats to align body and mind"
    )

    luke_kory = Athlete(
        athlete_name="Luke Kory",
        sport_id=yoga.sport_id,
        bio="An international yoga teacher and fitness expert, Kory is renowned for combining yoga with functional fitness to achieve holistic health and resilience.",
        socials="@lukekory",
        diet="Protein-rich and high-fiber meals designed to fuel physical and mental endurance"
    )

    raghunath_cappo = Athlete(
        athlete_name="Raghunath (Ray) Cappo",
        sport_id=yoga.sport_id,
        bio="Former punk rock musician turned yoga teacher, Ray Cappo blends his passion for spirituality and physical practice to make yoga accessible, transformative, and healing for all, especially men.",
        socials="@raghunathcappo",
        diet="Whole-food, plant-based diet, focused on simplicity and nourishment to support his yoga and spiritual practices."
    )

    powerlifting = Sport.query.filter_by(sport_name="Powerlifting").first()

    russel_orhii = Athlete(
        athlete_name="Russel Orhii",
        sport_id=powerlifting.sport_id,
        bio="A top-tier powerlifter known for his incredible strength and precision, Russel Orhii has set numerous records in the sport, particularly in the 83kg weight class.",
        socials="@russel_orhii",
        diet="A high-protein diet tailored to maximize strength and performance, with a focus on nutrient timing around training sessions."
    )

    giulia_imperio = Athlete(
        athlete_name="Giulia Imperio",
        sport_id=powerlifting.sport_id,
        bio="One of the top female powerlifters in the world, Giulia Imperio is known for her impressive strength in the squat and deadlift, as well as her incredible work ethic.",
        socials="@giulia_imperio",
        diet="A balanced diet rich in lean proteins and whole foods to maintain strength while focusing on recovery and performance."
    )

    joey_shaw = Athlete(
        athlete_name="Joey Shaw",
        sport_id=powerlifting.sport_id,
        bio="Joey Shaw has made a name for himself in the powerlifting world with his dominating performance in the 100kg+ weight class and his dedication to improving in every aspect of the sport.",
        socials="@joeyshaw_pwr",
        diet="High-calorie, nutrient-dense meals to fuel intense training sessions and muscle growth."
    )

    aylin_cuevas = Athlete(
        athlete_name="Aylin Cuevas",
        sport_id=powerlifting.sport_id,
        bio="Aylin Cuevas is a rising star in the powerlifting community, known for her strength and focus in the deadlift and squat, with a relentless pursuit of improvement in every competition.",
        socials="@aylin_cuevas",
        diet="Plant-based diet rich in proteins, healthy fats, and whole grains to maintain strength and recovery for powerlifting."
    )

    crossfit = Sport.query.filter_by(sport_name="Crossfit").first()

    
    mat_fraser = Athlete(
        athlete_name="Mat Fraser",
        sport_id=crossfit.sport_id,
        bio="A dominant force in the CrossFit world, Mat Fraser is a 5-time CrossFit Games Champion known for his work ethic, consistency, and unmatched strength across all areas of the sport.",
        socials="@mathewfras",
        diet="A high-protein, nutrient-dense diet focused on fueling his intense training and recovery, prioritizing balance and performance."
    )

    tia_clair_toomey = Athlete(
        athlete_name="Tia-Clair Toomey",
        sport_id=crossfit.sport_id,
        bio="Tia-Clair Toomey, a 6-time CrossFit Games Champion, is known for her versatility, strength, and ability to excel across all disciplines of CrossFit, both in individual and team competitions.",
        socials="@tiaclair1",
        diet="Whole-food, high-protein meals designed to fuel her performance in all CrossFit workouts, emphasizing recovery and strength."
    )

    jeffrey_adler = Athlete(
        athlete_name="Jeffrey Adler",
        sport_id=crossfit.sport_id,
        bio="Jeffrey Adler is a rising star in the CrossFit world, known for his consistent performance and impressive skills in both strength and endurance. He is quickly becoming a formidable competitor at the CrossFit Games.",
        socials="@jeffreyadler",
        diet="Balanced and clean eating approach, focused on fueling his body for optimal performance in high-intensity training and competition."
    )

    laura_horvath = Athlete(
        athlete_name="Laura Horvath",
        sport_id=crossfit.sport_id,
        bio="Laura Horvath is a top-tier CrossFit athlete who has made a name for herself with her explosive power and mental toughness. A CrossFit Games podium finisher, she continues to push the limits of what is possible in the sport.",
        socials="@laurahorvath",
        diet="A performance-driven diet, with a focus on nutrient-dense foods to support strength and endurance for CrossFit training and recovery."
    )

    gymnastics = Sport.query.filter_by(sport_name="Gymnastics").first()

    sunisa_lee = Athlete(
        athlete_name="Sunisa Lee",
        sport_id=gymnastics.sport_id,
        bio="Sunisa Lee made history by winning gold at the Tokyo 2020 Olympics in the all-around gymnastics competition. Known for her exceptional skills and composure under pressure, Lee continues to inspire the gymnastics world.",
        socials="@sunisalee_",
        diet="A well-rounded diet that includes lean proteins, fruits, vegetables, and complex carbs to fuel her intense training and support her recovery."
    )

    simone_biles = Athlete(
        athlete_name="Simone Biles",
        sport_id=gymnastics.sport_id,
        bio="Simone Biles is widely regarded as one of the greatest gymnasts of all time. With multiple Olympic gold medals and world championships under her belt, Biles has set the standard for excellence in gymnastics.",
        socials="@simonebiles",
        diet="A nutritious, well-balanced diet with a focus on fueling her demanding training sessions and ensuring optimal recovery for peak performance."
    )

    felix_dolci = Athlete(
        athlete_name="Felix Dolci",
        sport_id=gymnastics.sport_id,
        bio="Felix Dolci is a rising star in the gymnastics world, known for his impressive performances in men's artistic gymnastics. He has quickly made a name for himself with his fluid routines and incredible strength.",
        socials="@felixdolci",
        diet="A balanced diet that emphasizes protein for muscle growth, along with complex carbohydrates and healthy fats to maintain energy levels for high-performance training."
    )

    stephen_nedoroscik = Athlete(
        athlete_name="Stephen Nedoroscik",
        sport_id=gymnastics.sport_id,
        bio="Stephen Nedoroscik is an elite gymnast specializing in the pommel horse. He gained attention after winning the 2020 Olympic gold medal in this event, showcasing his extraordinary skill and balance.",
        socials="@stephen_nedoroscik",
        diet="A diet rich in lean proteins, healthy fats, and whole grains to optimize strength and flexibility for his demanding gymnastics routines."
    )

    return [viviane_araujo, john_jones, khabib_nurmagomedov, israel_adesanya, 
            rodtang, tawanchai_pk_saenchai, jackie_buntan, janet_todd, 
            amanda_serrano, ryan_garcia, canelo_alvarez,  katie_taylor, 
            amit_elor, roman_reigns, cody_rhodes, jordan_burroughs, taelornmoore, 
            isa_scheidt, john_danaher, mikey_musumeci, lebron_james, stephen_curry, 
            maya_moore, aja_wilson, cristiano_ronaldo, kylian_mbappe, marta, 
            alexia_putellas, alana_walker, ella_may_powell, matt_anderson, aleksandar_nikolov, 
            shohei_ohtani, mookie_betts, aj_andrews, olivia_pichardo, patrick_mahomes, 
            jalen_hurts, haley_van_voorhis, ilona_maher, usain_bolt, elyud_kipchoge, sifan_hassan, 
            sha_carri_richardson, tadej_pogacar, van_der_poel, marianne_vos, kate_courtney, 
            pan_zhanle, thomas_ceccon, summer_mcintosh, katie_ledecky, jan_frodeno, 
            lucy_charles_barclay, patrick_lange, laura_philipp, coco_gauff, serena_williams, 
            matteo_berrettini, novak_djokovic, natalia_grossman, janja_garnbret, toby_roberts, 
            sorato_anraku, adriene_mishler, koya_webb, luke_kory, raghunath_cappo, russel_orhii, 
            giulia_imperio, joey_shaw, aylin_cuevas, mat_fraser, tia_clair_toomey, jeffrey_adler, 
            laura_horvath, sunisa_lee, simone_biles, felix_dolci, stephen_nedoroscik]

if __name__ == "__main__":
    connect_to_db(app)
    with app.app_context():
        clear_database()
        athletes = create_athletes()  
        db.session.add_all(athletes) 
        db.session.commit()

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Juan", color='#9933ff')
define x = Character("???", color='#9933ff')
define p = Character("[pname]", color="#067aa1")
image astronaut = At("images/astronaut.png", astronaut)

define planets = {
    "pcb": {
        "planet_name": "Proxima Centauri b",
        "coords": "4.24 light-years away",
        "star": "Proxima Centauri",
    },
    "Exoplanet B": {
        "planet_name": "Exoplanet B",
        "coords": "10 light-years away",
        "star": "Unknown",
    },
    "Exoplanet C": {
        "planet_name": "Exoplanet C",
        "coords": "15 light-years away",
        "star": "Unknown",
    }
}

transform facing_left:
    xpos 1000 ypos 100
    xzoom -1.0

transform hover:
    xpos 0.0 xanchor 0.0 ypos 0.0 yanchor 0.0
    linear 2.0 zoom 1.05
    linear 2.0 xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 1.0
    linear 2.0 zoom 1.0
    xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 1.0
    linear 2.0 zoom 1.05
    linear 2.0 xpos 0.0 xanchor 0.0 ypos 0.0 yanchor 0.0
    linear 2.0 zoom 1.0
    repeat

transform astronaut:
    zoom 0.5

transform sopa_de_letras_position:
    xpos 300
    ypos 300

transform anagram_position:
    xpos 1200
    ypos 500

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg alley with fade

    play music "office_amb.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "First day at NASA..."
    "I’m so excited to start my first mission as an astronaut!"

    camera:
        xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
        linear 0.1 zoom 1.01
        linear 0.1 zoom 1.0
        repeat 3

    x "Hello! You there!"

    show astronaut at center with moveinleft

    a "Hello! My name is Juan. I’m the lead astronaut here at the NASA base on Earth."

    python:
        pname = renpy.input("¿What’s your name astronaut?")
        pname = pname.strip() or "Astronaut"

    a "Welcome [pname], glad to see you here!"
    a "Now, here at NASA we do exciting work regarding all of space."
    a "We investigate space, stars, and even planets beyond our own solar system!"
    a "We call these {b}exoplanets{/b}."
    a "On this mission, we’re going to explore some of the most interesting exoplanets and investigate more information about them!"
    
    menu:
        "Are you ready, astronaut [pname]?"
        
        "Yes!":
            "Awesome! Then let us prepare."

        "Yes, of course!":
            "Awesome! Then let us prepare."
    
    scene black
    with fade

    "We prepare our things and get ready to explore the cosmos."

    jump planet_selection

    return

label planet_selection:

    scene bg spaceship with fade

    play music "repair.mp3" 

    camera:
        xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0
        ease 1.0 zoom 1.75
        ease 1.5 ypos 0.0 yanchor 0.0
        ease 1.0 zoom 1.0

    pause 4.0

    show astronaut at center

    a "Now, we have to choose which exoplanet to explore first."

    menu:
        "Which exoplanet do you wish to know more about?"

        "Proxima Centauri b":

            $ planet = "pcb"

            a "Great choice! Let me tell you more about Proxima Centauri b."
            a "Proxima Centauri b is an exoplanet orbiting the star Proxima Centauri."
            a "It is located in the habitable zone of its star, which means it could have liquid water on its surface."
            a "Isn't that exciting?"

            menu:
                "Do you want to explore Proxima Centauri b?"

                "Yes!":
                    a "Great! Let's prepare for the mission to Proxima Centauri b."
                    jump liftoff

                "No, I want to explore another exoplanet.":
                    jump planet_selection 

        "Exoplanet B":
            "Interesting choice! Let me tell you more about Exoplanet B."

        "Exoplanet C":
            "Exciting choice! Let me tell you more about Exoplanet C."

label liftoff:
    
    scene bg cockpit with fade

    play music "countdown.mp3"
    
    $ planet_name = planets[planet]["planet_name"]
    $ coords = planets[planet]["coords"]
    $ star = planets[planet]["star"]

    a "Starting liftoff sequence..."
    a "Destination: [planet_name]."
    a "Location: [coords]."
    a "Star: [star]."

    camera:
        xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
        linear 0.1 zoom 1.01
        linear 0.1 zoom 1.0
        repeat

    a "Preparing for liftoff..."
    a "Engines ready..."

    camera:
        xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
        linear 0.1 zoom 1.03
        linear 0.1 zoom 1.0
        repeat

    a "Preparing for launch..."

    camera:
        xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
        linear 0.1 zoom 1.05
        linear 0.1 zoom 1.0
        repeat

    a "3..."
    a "2..."
    a "1..."

    camera:
        xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
        linear 0.5 zoom 50
    
    scene black

    a "Liftoff!"
    
    camera:
        xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
        linear 0.1 zoom 1.0

    "We start the engines and lift off into space."

    if planet == "pcb":

        jump pcb

    

label pcb:

    play music exogenesis
    
    scene bg pcb at hover
    show spaceship overlay
    with fade

    show astronaut at left with moveinleft

    a "We have arrived at Proxima Centauri b."
    a "The planet looks beautiful from here."
    a "Let's begin our exploration."

    menu:
        "What do you want to do?"

        "Analyze the atmosphere":
            a "Let's analyze the atmosphere of the planet from orbit."
            jump analyze_atmosphere

        "Explore the surface":
            a "Let's land on the surface and explore the planet."
            jump explore_surface

        "Return to Earth":
            a "Let's return to Earth and prepare for the next mission then."
            jump planet_selection

label explore_surface:

    scene bg pcb_surface with fade

    camera:
        xpos 0.0 xanchor 0.0 ypos 0.5 yanchor 0.5
        ease 1.0 zoom 1.75
        ease 1.5 xpos 1.0 xanchor 1.0
        ease 1.0 zoom 1.0

    pause 4.0

    show astronaut at facing_left with moveinright

    a "We have landed on the surface of Proxima Centauri b."
    a "The landscape is fascinating."
    a "Let's explore and collect samples."

    # show sopa_de_letras at sopa_de_letras_position

    show text "T E S T\nT E S T" at sopa_de_letras_position

    p "Retrieving samples... \[Press space for hints\]"
    p "Hints: YELLOW, ROCKY, PROXIMA, LIQUID, CENTAURI"

    hide sopa_de_letras

    a "Wow! Seems like we found some interesting samples."
    a "Seems like we found a yellowy, rocky surface."
    a "We also found signs liquid water! This is an amazing discovery."
    a "Let's head back to the spaceship and analyze these samples."

    jump pcb

label analyze_atmosphere:

    a "We'll use a method called spectroscopy to analyze the gases in the atmosphere."
    a "Spectroscopy is a powerful tool that allows us to determine the composition of a planet
    by analyzing how light interacts with its atmosphere."
    a "Let's start the analysis."
    "Running analysis..."
    a "Seems like we got the data back, but appears to be encrypted."
    a "We managed to decypher the first and last part... but not the rest."

    show text "W N I D\nM G A E N T\nD U I F F L C I T\nR A I I T A D O N" at anagram_position

    a "Can you help us solve the rest of the data?"

    # anagram puzzle

    $ answer = renpy.input("Word #1: ").strip().lower()

    while answer != "wind":
        p "Almost."
        $ answer = renpy.input("Word #1: ").strip().lower()

    p "Nice!"

    $ answer = renpy.input("Word #2: ").strip().lower()

    while answer != "magnet":
        p "Hmm, not quite."
        $ answer = renpy.input("Word #2: ").strip().lower()

    p "Great!"

    $ answer = renpy.input("Word #3: ").strip().lower()

    while answer != "difficult":
        p "Not quite."
        $ answer = renpy.input("Word #3: ").strip().lower()

    p "Awesome!"
    p "Now... last one."

    $ answer = renpy.input("Word #4: ").strip().lower()

    while answer != "radiation":
        p "This is a tricky one."
        $ answer = renpy.input("Word #4: ").strip().lower()

    p "Awesome!"

    hide anagram

    a "Wow! This data is fascinating."
    a "We found huge signs of {i}radiation{/i} and strong {i}winds{/i} from its parent star."
    a "These conditions have destroyed the planet's {i}magnetic{/i} field, making it very {i}difficult{/i} for life to thrive."
    a "This is an important discovery for our research."

    jump pcb
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("José", color='#9933ff')
define x = Character("???", color='#9933ff')
define p = Character("[pname]", color="#067aa1")
image astronaut = At("images/astronaut.png", astronaut)

define planets = {
    "pcb": {
        "planet_name": "Proxima Centauri b",
        "coords": "4.24 light-years away",
        "star": "Proxima Centauri",
    },
    "w80b": {
        "planet_name": "WASP-80 b",
        "coords": "10 light-years away",
        "star": "Unknown",
    }
}

transform facing_left:
    xpos 1000 ypos 100
    xzoom -1.0

transform facing_right:
    xpos 100 ypos 100
    xzoom 1.0

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

    a "Hello! My name is José. I’m the lead astronaut here at the NASA base on Earth."

    python:
        pname = renpy.input("¿What’s your name astronaut?")
        pname = pname.strip() or "Astronaut"

    a "Welcome [pname], glad to see you here!"
    a "Now, here at NASA we do exciting work regarding all of space."
    a "We investigate space, stars, and even planets beyond our own solar system!"
    a "We call these {i}exoplanets{/i}."
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

        "Wasp-80 b":
            a "Interesting choice! Let me tell you more about Exoplanet B."
            a "It has a mass similar to that of Jupiter, but it orbits its star much closer than Jupiter does to the Sun."
            a "Its temperature is approximately 825 kelvins, wich is around 550 degrees Celsius! Scorching hot."
            
            jump planet_selection 


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

    play music space_bgm
    
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

    show astronaut at facing_right with move

    show text """{b}P{/b}  {b}Y{/b}  {b}Y{/b}  E  {b}L{/b}  {b}L{/b}  O  W  {b}P{/b}  D
{b}R{/b}  Z  F  {b}R{/b}  N  U  B  U  W  E
O  {b}L{/b}  {b}Y{/b}  I  {b}L{/b}  {b}C{/b}  U  {b}R{/b}  T  {b}P{/b}
X  I  M  {b}P{/b}  Q  E  N  O  K  H
I  Q  G  {b}L{/b}  T  N  W  {b}C{/b}  A  H
M  U  E  {b}P{/b}  H  T  I  K  Q  O
A  I  K  X  {b}Y{/b}  A  V  {b}Y{/b}  O  {b}C{/b}
V  D  V  O  T  U  S  A  {b}Y{/b}  Z
N  E  F  O  {b}P{/b}  R  {b}C{/b}  T  E  X
M  Q  C  {b}P{/b}  B  I  K  K  S  {b}L{/b}""" at anagram_position

    play sound interface

    p "Retrieving samples..."
    p "Hmm... I'm looking at 5 samples starting with Y, R, P, L, and C."

    # sopa de letras puzzle

    $ words = ["yellow", "rocky", "liquid", "proxima", "centauri"]
    $ words_found = []

    while words:
        $ word = renpy.input("Word found:").strip().lower()

        while word not in words:
            p "I don't think I found that word."
            p "Hmm... I'm looking at 5 samples starting with Y, R, P, L, and C."
            p "Words found: [words_found]"
            $ word = renpy.input("Word found:").strip().lower()
        
        p "Great! I found that word."
        $ words_found.append(word)
        $ words.remove(word)
        p "Words found: [words_found]"

    hide sopa_de_letras

    a "Wow! Seems like we found some interesting samples."
    a "Seems like we found a {i}yellowy{/i}, {i}rocky{/i} surface."
    a "The heat from {i}Proxima Centauri{/i} is also intense..."
    a "We also found signs {i}liquid{/i} water! This is an amazing discovery."
    a "Let's head back to the spaceship and analyze these samples."

    jump pcb

label analyze_atmosphere:

    a "We'll use a method called spectroscopy to analyze the gases in the atmosphere."
    a "Spectroscopy is a powerful tool that allows us to determine the composition of a planet
    by analyzing how light interacts with its atmosphere."
    a "Let's start the analysis."

    play sound interface

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
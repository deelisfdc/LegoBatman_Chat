#With each response, Lego Batman acknowleges the answer with, "Cool!" and spins off with adding something about his own favorite color or where he lives.
#2. Lego Batman will then go off on a tangent about himself and then says ok, time for the Q&A. Ask me anything you want.
#3. From here: and a short list of 3 topics comes up. User selects a topic, and three questions pop up. User selects a question for Lego Batman to ask.
#4. Lego Batman answers, sometimes ending his response by asking the user another question depending on the selection.
# 5. Depending on the question selected, the Bat Signal will go off and lego batman will have to split and the theme song background is splayed (repeats) across the screen and opens a closing image thanking the user for being a super fan.

#Nice to have: when time is up, Lego Batman cuts off the chat with something snarky and says Time's Up. Bye! and opens an image thanking the super duper fan.

#introduces lego Batman, Askes for user name and information

#My code is not working :( Help!


my_guest_list = []


def theme_song():
    print "Na-nuh " *8
    print "Batman Out!"


def Lego_Batman_chat_start():

#1. Lego Batman asks user: name, favorite color, where do you live?

    """ Lego Batman introduces himself and starts background check"""

    guest_intro = """
    \n Hey, You! Computer randomly picked you for this week's chat. 
    My favorite dinner's heating up,
    so we have 90 seconds to get to know more about ME.
    First, we're gonna have to do a background check on you
    to make sure you're not on my wanted list.
    Tell the truth, or get booted! 

    Ready?
    
    Type "Y" to start.
    If you wanna skip this part and stay anonymous, type "N"
    If you've got something to hide, start running now!!>>>
    """

    start_chat = raw_input(guest_intro)

    if start_chat == "Y":
        
        start_background_check()

    elif start_chat == "N":
        print """
        \n Hmmm...Sounds sneaky.
        Looks like you've got something to hide.
        I'm gonna go eat my Lobster Thermidor now. Good bye!
        """

        print "Batman Out!"
        print theme_song()

    else:
        #This person is suspicious!
        print "\nRun! Computer is tracing your location, and Gotham Police will be there is 30 seconds!"

        print theme_song()



def start_background_check():
    """Get guest background info"""

    guest_name = raw_input("What's your first name? >>> ")

    guest_name.upper()

    return guest_name

    print guest_name

    my_guest_list.append(guest_name)

    if guest_name == "JOKER":
        
        print "Ah ha! My arch nemesis and Frenemy. Alright, I'll give you a minute."

        guest_lives_here()
    
    elif guest_name != "JOKER":
        print guest_name, "Hmmm. I once caught a villian with that name. Caught 'em on the FIRST TRY!"

        guest_lives_here()


def guest_lives_here():
    """Find out guest's hometown"""
    guest_hometown = raw_input(" Where are you from?>>> ")
    
    return guest_hometown

    print "\nHuh. What a coincidence. I have (ahem), I HEARD that Wayne Enterprises owns most of the land out there... Interesting."

    guest_favorite_superhero()


def guest_favorite_superhero():
    """Who is our guest's favorite superhero?"""

    favorite_superhero = raw_input("So...Who is your favorite super hero? Of all time?>>> ")

    return favorite_superhero

    if favorite_superhero == "Superman":

        print "What? Oh hey, lookit that Bat Signal! Gotta go!"

        print theme_song()

    elif favorite_superhero == "Wonderwoman":

        print "Yeah! Mine too! Ahem, I mean: On to Q&A!"

    elif favorite_superhero == "Batman" or "you":
        
        print "Wow. Yeah! All right! Let's move on to Q&A!"

    elif favorite_superhero == "Robin":
        
        print "\nWhat?! ...Ok. Yeah! Me and Robin - we make a good team! I'm so proud of him! Next is Q&A!"

    else:
        print "Wait, now. Those are not even superheroes! I think our time is up!"

        print theme_song()


#-----------------------------------------------
Lego_Batman_chat_start()
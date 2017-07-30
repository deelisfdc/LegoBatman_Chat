#With each response, Lego Batman acknowleges the answer with, "Cool!" and spins off with adding something about his own favorite color or where he lives.
#2. Lego Batman will then go off on a tangent about himself and then says ok, time for the Q&A. Ask me anything you want.
#3. From here: and a short list of 3 topics comes up. User selects a topic, and three questions pop up. User selects a question for Lego Batman to ask.
#4. Lego Batman answers, sometimes ending his response by asking the user another question depending on the selection.
# 5. Depending on the question selected, the Bat Signal will go off and lego batman will have to split and the theme song background is splayed (repeats) across the screen and opens a closing image thanking the user for being a super fan.

#Nice to have: when time is up, Lego Batman cuts off the chat with something snarky and says Time's Up. Bye! and opens an image thanking the super duper fan.

#introduces lego Batman, Askes for user name and information


# ideas for pulling random questions for second section
    # #import random
    # #d = {'Key':'---', '  ':'  ''}
    # #random.choice(d.keys())

    # import random
    # di = {'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
    # random.choice(di['a'])
    # // returns a random value from the list

    #def ask(question):
    #answer = input(question + " [y/n]")
    #return answer in ['y', 'Y', 'Yes', 'YES', 'yes']

        #if ask("Do you like ?"):

        #def print_pause(lines):
            #for line, pause in lines:
                #print line
                #time.sleep(pause)

        #print_pause([
            #("What's your name", 2),
            #("Where do you live", 1),
            #("T!", 0)
            #])


my_guest_list = []
# start_choice = 

#guest_name = {'enemy': JOKER, CATWOMAN, RIDDLER, 'ally': DICK GRAYSON, RICHARD GRAYSON, BARBARA GORDON, DIANA PRINCE}

#superhero = [Batman, Batgirl, Bat Girl, Wonder Woman, Superman, Robin]



# def start_background_check():
        
    #"""Get guest background info"""

#     guest_name = raw_input("What's your first name? >>> ")

#     guest_name = guest_name.upper()

#     if guest_name == "JOKER":
        
#         print "Ah ha! My arch nemesis and Frenemy. Alright, I'll give you a minute."

#         guest_lives_here()
    
#     elif guest_name != "JOKER":

#         print "All right {}. Hmmm. I once battled a villian with that *same* name. Caught 'em on the FIRST TRY!".format(guest_name.upper())

#         my_guest_list.append
        
#         guest_lives_here()

#     else:

#         print "Hmm. Not answering sounds pretty suspicious. Computer, home in on the location!"


def start_background_check():
        
    """Get guest background info"""

    guest_name = raw_input("What's your first name? >>> ")

    guest_name = guest_name.upper()

    if guest_name == "JOKER":
        
        print "Ah ha! My arch nemesis and Frenemy. What evil trick do you have up your sleeve now?"
    
    elif guest_name != "JOKER":

        print "\n{}. Hmmm. I once battled a villian with that *same* name.\nCaught 'em on the FIRST TRY!\nOK Next question while Computer traces this call:\n".format(guest_name.upper())

        my_guest_list.append
        
        guest_lives_here()

    else:

        catch_suspicious_person()


def guest_lives_here():
    """Find out guest's hometown"""

    guest_hometown = raw_input(" Where are you from?>>> ")

    guest_hometown = guest_hometown.title()
    
    print """
    \nHuh. What a coincidence. I have (ahem) -- 
    \nI mean, I HEARD that Wayne Enterprises owns most of the land out there...
    \n...Interesting.
    """

    guest_favorite_superhero()


def guest_favorite_superhero():

    """Who is our guest's favorite superhero?"""

    favorite_superhero = raw_input("So...Who is your favorite super hero? Of all time?>>> ")
    #Create random list of Batman asking this question in a few different ways. (?)

    favorite_superhero = favorite_superhero.upper()

    if favorite_superhero == "SUPERMAN":

        print "What? Oh hey, lookit that Bat Signal!\nInterview's over!\nGotta go!"

        print theme_song()

    elif favorite_superhero == "WONDER WOMAN" or "WONDERWOMAN":

        print "Yeah! Mine too! Ahem, I mean: On to Q&A!"

    elif favorite_superhero == "BATMAN" or "YOU":

        print "Wow. Yeah! All right!\nNow it's YOUR turn for Q&A!"

    elif favorite_superhero == "ROBIN" or "BOY WONDER":

        print "\nWhat?! ...Ok. Yeah!\nMe and Robin - we make a good team!\nI'm so proud of him!\nNow it's YOUR turn for Q&A!"

    else:
        print "Wait, now.\nWho??\nThose are NOT even superheroes!\nName someone else!"
#       Ask favorite super hero question again - random question)
            
        guest_favorite-superhero()

    return favorite_superhero


def theme_song():

    print "\n\tNa-nuh Na-nuh!" * 4 "\t***Batman!***\t*** Ka Pow! ***"


def catch_suspicious_person():

    print "\n\tHmmm. Not answering is super suspicious.\n\tWe'd better bring you in for questioning.\n\tComputer has traced your location.\n\tBetter run! Gotham Police will be there is 30 seconds!"\n\t"
        
    print theme_song()


def Lego_Batman_chat_start():

#1. Lego Batman asks user: name, favorite color, where do you live?

    """Get Start Chat Permission"""

    print """
    \n\tHey, Bat-tastic Fan! Welcome to this week's chat.
    \tWe have 2 minutes til my favorite dinner's heated up,
    \tSo What do you want to know about me?
    \t...
    \tHmmm... Computer just flagged you for a random background check
    \tto make sure you're not on my wanted list.
    \tTell the truth, or get booted!
    \n\tReady?
    \n\tType "Y" to start.
    \tIf you wanna skip this part and stay anonymous, type "N"
    \tIf you've got something to hide, start running now!!>>>
    """

    start_choice = raw_input("")

    start_choice = start_choice.upper()

    if start_choice == "Y":

        print "All right! Let's get started."

        start_background_check()

    elif start_choice == "N":

        print """
        \nHmmm...Sounds sneaky.
        \nLooks like you've got something to hide.
        \nI'm gonna go eat my Lobster Thermidor now.
        \nGood bye!
        """

        print ""

        print theme_song()

    else:
        #This person is suspicious!

        print """
        \n\tHmmm. Not answering is super suspicious.
        \n\tWe'd better bring you in for questioning.
        \n\tComputer has traced your location.
        \n\tBetter run! Gotham Police will be there is 30 seconds!"\n\t
        """

        print theme_song()

#-----------------------------------------------
Lego_Batman_chat_start()

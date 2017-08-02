#This Q&A game was created to help me and my child learn Python with a favorite subject.
#Chat introduces lego Batman, Asks for user name and information. With each response, Lego Batman acknowleges the answer with, "Cool!" and spins off with adding something about his own favorite color or where he lives.
#2. Lego Batman will then go off on a tangent about himself and then says ok, time for the Q&A. Ask me anything you want.
#3. From here: and a short list of 3 topics comes up. User selects a topic, and three questions pop up. User selects a question for Lego Batman to ask.
#4. Lego Batman answers, sometimes ending his response by asking the user another question depending on the selection.
# 5. Depending on the question selected, the Bat Signal will go off and lego batman will have to split and the theme song background is splayed (repeats) across the screen and opens a closing image thanking the user for being a super fan.
#Nice to have: when time is up, Lego Batman cuts off the chat with something snarky and says Time's Up. Bye! and opens an image thanking the super duper fan.

#Some language, trivia and quotes are borrowed from "The Lego Batman Movie Essential Guide" and "Batman's Guide to Being Cool"

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

#import random
# import turtle

# # def open_turtle():
# #     window = turtle.Screen()
# #     window.bgcolor("black")
# #     window.title("Draw Your Logo Here")
# #     #window.showturtle()
   
# window = turtle.Screen()

# window.bgcolor("black")

# window.title("Draw Your Logo Here")

# logo = turtle.Turtle()


# def draw_turtle(newturtle):

#     turtle.ondrag(turtle.goto)

#     turtle.listen()
    

# def drawing_preference():
#     """Open turtle screen for logo drawing"""

#     logo.shape('classic')
#     logo.color("green", "yellow")
#     logo.pencolor("white")
#     logo.width("10")


# def draw():
#     """draw turtle"""

#     drawing_preference()

#     draw_turtle(logo)

#     window.exitonclick()


my_guest_list = []

#guest_name = {'enemy': JOKER, CATWOMAN, RIDDLER, 'ally': DICK GRAYSON, RICHARD GRAYSON, BARBARA GORDON, DIANA PRINCE}

favorite_hero = {
    "BATMAN": "\n\tWow. Yeah! All right! Now it's YOUR turn for Q&A!",
    "YOU": "\n\tWow. Yeah! All right! Now it's YOUR turn for Q&A!",
    "WONDER WOMAN": "\n\tYeah! Mine too! Ahem, I mean: On to Q&A!",
    "WONDERWOMAN": "\n\tYeah! Mine too! Ahem, I mean: On to Q&A!",
    "SUPERMAN": "\n\tWhat?! Oh hey, lookit that - The Bat Signal!\n\tInterview's over! Gotta go!",
    "ROBIN": "\n\tYeah! Me and Robin - we make a good team!\n\tI'm so proud of him!\n\tNow it's YOUR turn for Q&A!\n\t"
    }

batman_response = {
    "weapon": "\n\tBatmobile, because my current model can turn into a Monster Truck!",
    "wisdom": "\n\tBe Cool. Always stand up for what's right.\n\tTreat your friends like the super heroes they are!"
    }

#More weapons and wisdom="Batarang, because it's shaped like a bat!", "\n\tI am MEGA Cool.\n\tThis Coolness didn't happen overnight.\n\tIt takes time and practice to build your cool superpower.\n\tAnd Great Things are worth the wait!"
#superhero_keys = {"BATMAN": "Batman", "YOU": "Batman"}
#favorite_hero=raw_input('whosyourfavorite hero').upper()
#hero_key = superhero_keys[favorite_hero]
#print superhero[hero_key]


def start_background_check():
    """Get guest background info"""

    guest_name = raw_input("\nWhat's your first name? ")

    guest_name = guest_name.upper()

    if guest_name == "JOKER":
        
        print """
        \n\tAh ha! JOKER!! You are my arch nemesis and Frenemy.
        \n\tWhat evil trick do you have up your sleeve now? Ready to battle?
        """
    
    elif guest_name != "JOKER":

        print "\n\t{}... Hmmm. I once battled a villian with that *same* name.\n\tCaught 'em on the FIRST TRY!\n\tOK Next question while Computer traces this call...\n\t".format(guest_name.upper())

        my_guest_list.append
        
        guest_lives_here()

    else:

        catch_suspicious_person()


def guest_lives_here():
    """Find out guest's hometown"""

    guest_hometown = raw_input(" Where are you from? ")

    guest_hometown = guest_hometown.title()
    
    print """
    \n\tHuh. {}. What a coincidence. I have (ahem)...
    \n\tI MEAN, I HEARD that Uhhh.. WAYNE ENTERPRISES owns most of the land out there...
    \n\t...Interesting. OK next question!
    """.format(guest_hometown)

    guest_favorite_superhero()


def guest_favorite_superhero():

    """Ask for guest's favorite superhero"""

    favorite_superhero = raw_input("So...Who is your favorite super hero? Of all time? ")
    #Create random list of Batman asking this question in a few different ways. (?)

    favorite_superhero = favorite_superhero.upper()

    if favorite_superhero == "SUPERMAN":

        print favorite_hero["SUPERMAN"]
        #"What? Oh hey, lookit that Bat Signal!\nInterview's over!\nGotta go!"

        print theme_song()

    elif favorite_superhero == "WONDER WOMAN" or "WONDERWOMAN":
        
        print favorite_hero["WONDER WOMAN"]
        #print "Yeah! Mine too! Ahem, I mean: On to Q&A!"
        
        ask_batman()

    elif favorite_superhero == "BATMAN" or "YOU":

        print favorite_hero["BATMAN"]
        #print "Wow. Yeah! All right!\nNow it's YOUR turn for Q&A!"

        ask_batman()

    elif favorite_superhero == "ROBIN" or "BOY WONDER":

        print favorite_hero["ROBIN"]
        #print "\nWhat?! ...Ok. Yeah!\nMe and Robin - we make a good team!\nI'm so proud of him!\nNow it's YOUR turn for Q&A!"

        ask_batman()

    else:
        
        print "Wait, now.\nWho??\nThose are NOT even superheroes!\nName someone else!"
#       Ask favorite super hero question again - random question)

        guest_favorite_superhero()

    # return favorite_superhero


def ask_batman():

    print """"
    \nOK. Now your turn.
    \nWe have one minute til my Lobster Thermidor is ready to eat!
    \nWhat do you want to know about me?
    \n
    \n\tA - My favorite Bat weapon
    \n\tB - My greatest Fears
    \n\tC - Random bits of Bat Wisdom
    """

    batman_question = raw_input("Choose A, B or C: ")
    
    batman_question = batman_question.upper()

    if batman_question == "A":

        print "\n\tHa! Easy question!\n\tAnything with a Bat shape on it!\n\tRight now I'm working on jazzing up my", batman_response["weapon"]

    elif batman_question == "B":

        print "\n\tYeah, that's a tough one.\n\tIn my last epic movie, I learned that didn't have to fight the bad guys all by myself.\n\tI have friends.\n\tThat scared me."

    elif batman_question == "C":

        print "\n\tHere's my favorite:", batman_response["wisdom"]

    else:

        catch_suspicious_person()


def theme_song():

    """print theme song string. Exit."""

    print "\n\tNa-nuh Na-nuh!" * 4 + "\n\t***Batman!***\n\t*** Ka Pow! ***\n\n"


def catch_suspicious_person():
    """print warning and theme song. Exit."""

    print "\n\tHmmm. Not answering is super suspicious.\n\tI'm going to bring you in for questioning.\n\tComputer has a lock on your location.\n\tBetter run! Gotham Police will be there is 30 seconds!\n\t"

    print theme_song()


def Bye():
    """Final goodbye and open turtle to close"""

    # print """
    #     # \n\tThanks for chatting! One last word of wisdom!
    #     # \n\tYou know MY logo. It's sleek and chic and TRADEMARKED,
    #     # \n\tand never goes out of style!
    #     # \n\tWhat's your cool symbol?
    #     # \n\tNow it's your turn to draw your own symbol!
    #     \n\tThanks for playing!
    #     """
    
    print ""
    
    print "\n\tThanks for playing!\n\t"
    # draw()


def lego_batman_chat_start():

#1. Lego batman asks user: name, favorite color, where do you live?

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
    \n\tType 'Y' to start.
    \tIf you wanna skip this part and stay anonymous, type 'N'
    \tIf you've got something to hide, start running now!!
    """

    start_choice = raw_input("\t>>>")

    start_choice = start_choice.upper()

    if start_choice >= "Y":

        print "\nAll right! Let's get started."

        start_background_check()

    elif start_choice >= "N":

        print """
        \nHmmm...Not answering makes it seem like
        \nyou've got something to hide.
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
        \n\tBetter run! Gotham Police will be there is 30 seconds!
        """
        print theme_song()

    #turtle.mainloop()

    Bye()    

#-----------------------------------------------
lego_batman_chat_start()

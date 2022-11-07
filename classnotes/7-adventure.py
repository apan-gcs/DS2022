
"""
A choose-your-own-adventure series.
Alternatively, a quiz.
"""

from time import sleep

# A function to print one character at a time (simulate typing)
def print_slow(text):
    for x in text:                    # Cycle through the text
        print(x, end='', flush=True)  # Print, no new line, flush buffer
        sleep(0.01)                   # Delay between characters
    print()                           # New line
    sleep(0.2)

# A function to test the player's input
def make_choice(possible_choices):
    """
    Asks for player input for a choice from a list of possible_choices.
    If the choice is invalid, reprompt the player.
    By default, the program will reprompt up to 5 times before cancelling.
    
    """
    for i in range(3):
        choice = input("Your choice: ")
        if choice == str(1) or choice == str(2):
            print()
            return int(choice)
        else:
            print("Your choice couldn't be recognized.")
    else:
        print("You put in the wrong choice too many times.")
        print("GAME OVER.")
        quit()


score = 0         # Optional: Keep track of score throughout a quiz.
choices = [1, 2]  # Valid choices for the make_choice function


# BEGINNING: Initial setup / name.
print_slow("Welcome to a new school adventure!")
sleep(1)

name = input("Please enter your name: ")

print_slow(f"Your name is {name}.\n")


# ADVENTURE: Decision tree of choices.

print_slow("You wake up in the morning and check your phone, only to find out"
       " that you're late for school!")
print_slow("What do you do?")
print_slow("1: Give up on going to school and sleep in.")
print_slow("2: Rush to get ready.")
sleep(0.5)

x = make_choice(choices)

if x == 1:  # Give up (GAME OVER)
    print_slow("You give into your drowsiness and go back to sleep.")
else:       # Get ready
    print_slow("You get ready for school within five minutes and rush out the door.")
    print_slow("You manage to make it to school before 9AM, but you suddenly realize"
          " that you don't have your wallet or your ID!")
    print_slow("What do you do?")
    print_slow("1: Try to sneak into the building.")
    print_slow("2: Tell the security guard that you forgot your ID.")
    sleep(0.5)
    
    x = make_choice(choices)

    if x == 1:  # Sneak (GAME OVER)
        print_slow("You try to sneak in through the front door, but you get caught!")
        print_slow("Now you're in trouble.")
    else:       # Forgot ID
        print_slow("You tell the security guard that you left your ID at home. "
                   "You get a scolding, but you manage to get in.")
        print()
        print_slow("You got to your first class, but you forgot your homework, too!")
        print_slow("What do you do?")
        print_slow("1: Lie and say your dog ate your homework.")
        print_slow("2: Apologize and promise to email it later today.")
        
        x = make_choice(choices)
        
        if x == 1:  # Lying dog (GAME OVER)
            print_slow("You give your excuse, but your teacher doesn't believe you.")
            print_slow("Now you're missing a homework, and you also feel bad.")
        else:       # Apologize
            print_slow("You apologize for forgetting your homework. Your teacher "
                       "is nice and tells you to hand it in next class.")
            print_slow("Now you pay attention in class and hope there are no more "
                       "ordeals in your day.")
            sleep(1)
            print_slow("THE END. \U0001F642")
            quit()

# Default ending for any of the GAME OVERs.
sleep(1)
print_slow("THE END. \U0001F643")


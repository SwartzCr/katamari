from __future__ import print_function
import os
import random

class PColors:
    """Define some colors up in this piece."""

    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    ENDC = '\033[0m'

    def disable(self):
        """Disable colorization and revert to plain text."""
        self.RED = ''
        self.YELLOW = ''
        self.GREEN = ''
        self.BLUE = ''
        self.PURPLE = ''
        self.ENDC = ''

def banner():
    """Welcome banner."""
    banner_file = os.getcwd() + '/banner.dat'
    with open(banner_file, 'r') as b:
        for l in b:
            print(l.format(PColors, PColors), end='')
        print('\n')

def prompt(actions):
    acts = ", ".join(actions)
    print("I'm sorry I didn't understand that, valid actions are: {0}".format(acts))

def pickup(item):
    print("Nice! You now have a {0} stuck to your katamari!".format(item))

def fail(item):
    print("You slam your katamari into the {0} and bounce right back off losing some items! Oh no!".format(item))

def royal_rainbow():
    """Royal Rainbow."""
    rainbow_file = os.getcwd() + '/royal_rainbow.dat'
    with open(rainbow_file, 'r') as r:
        for l in r:
            print(l.format(PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors), end='')
        print('\n')

def bid_adieu():
    print("sorry to see you go, play again soon!")

def welcome():
    banner()
    print("Na na nanana na na Katamari Damacy!")

def move(direction):
    print("You push hard and roll your katamari {0}".format(direction))

def status(size):
    print("Your katamari is {0}cm".format(str(size)))

def bump(item):
    status=["bumps and","rubs and","wiggles then","stalls then"]
    verb = status[random.randrange(len(status))]
    print("Your katamari {0} rolls back from the {1} before slowing".format(verb, item))

def lose(item):
    print("Oh No! A {0} flies off of your katamari!".format(item))

def welcome_level(level):
    print("Welcome to {0}! You have {1} minutes to get your katamari from {2}cm to {3}cm, better hurry!".format(level["name"], level["time"]/60, level["katamari"], level["goal"]))

def minute_warning():
    print("Only one minute left! Better hurry!")

def times_up():
    print("That's all the time you have, time to see how you did")

def win():
    print("My what a beautiful katamari! I am very pleased with you")

def failure():
    print("NOT BIG ENOUGH! I AM VERY DISAPPOINTED")

def final_size(size):
    print("Your final katamari size is {0}cm".format(str(size)))

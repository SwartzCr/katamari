from __future__ import print_function
import os

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
    print "I'm sorry I didn't understand that, valid actions are: {0}".format(acts)

def pickup(item):
    print "Nice! You now have a {0} stuck to your katamari!".format(item)

def fail(item):
    print "You slam your katamari into the {0} and bounce right back off losing some items! Oh no!".format(item)

def royal_rainbow():
    print "{.RED}R{.ENDC}{.RED}O{.ENDC}{.YELLOW}Y{.ENDC}{.YELLOW}A{.ENDC}{.GREEN}L{.ENDC} {.GREEN}R{.ENDC}{.GREEN}A{.ENDC}{.BLUE}I{.ENDC}{.BLUE}N{.ENDC}{.PURPLE}B{.ENDC}{.PURPLE}O{.ENDC}{.PURPLE}W{.ENDC}".format(PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors, PColors)

def bid_adieu():
    print "sorry to see you go, play again soon!"

def welcome():
    banner()
    print "Na na nanana na na Katamari Damacy!"

def move(direction):
    print "You push hard and roll your katamari {0}".format(direction)

def status(size):
    print "Your katamari is {0}cm".format(str(size))

def lose(item):
    print "Oh No! A {0} flies off of your katamari!".format(item)

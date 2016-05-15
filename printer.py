
def prompt(actions):
    acts = ", ".join(actions)
    print "I'm sorry I didn't understand that, valid actions are: {0}".format(acts)

def pickup(item):
    print "Nice! You now have a {0} stuck to your katamari!".format(item)

def fail(item):
    print "You slam your katamari into the {0} and bounce right back off losing some items! Oh no!".format(item)

def royal_rainbow():
    print "ROYAL RAINBOW"

def bid_adieu():
    print "sorry to see you go, play again soon!"

def welcome():
    print "Na na nanana na na Katamari Damacy!"

def move(direction):
    print "You push hard and roll your katamari {0}".format(direction)

def status(size):
    print "Your katamari is {0}cm".format(str(size))

def lose(item):
    print "Oh No! A {0} flies off of your katamari!".format(item)

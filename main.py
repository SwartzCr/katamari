
# each level is a grid of grids, maybe 3d

# you are a size, in each area there are objects that have size, if you're large enough you absorb them

# NSEW looks that direction 1-2 squares and describes objects

# maybe there are also events? Like steep slopes or things that bump you?

# small objects can be clustered

# you can enter spin mode and move multiple squares?

# time limit??

# royal rainbow ascii art to playo
import gen_game
import printer
import play
import json
import readline

try:
    input = raw_input
except NameError:
    pass

def load_game():
    with open("data.json", 'r') as f:
        data = json.load(f)
    return data

def load_level(level):
    file_name = level + ".json"
    with open(file_name, 'r') as f:
        out = json.load(f)
    return out

class actionCompleter(object):

    def __init__(self):
        return

    def set_actions(self, actions):
        self.actions = sorted(actions)

    def complete(self, action, index):
        buf = readline.get_line_buffer()
        if index == 0:
            if buf != "":
                self.matches = [a for a in self.actions if a.startswith(buf)]
            else:
                self.matches = self.actions[:]
            response = self.matches[index]
            if response:
                if action != buf:
                    response = response[len(buf)-len(action):]
                return response

def try_level(data):
    levels = [level for level in data["levels"] if level["number"] <= data["progress"]]
    names = [level["name"] for level in levels]
    data["completer"].set_actions(names)
    print("available levels are: {0}".format(", ".join(names)))
    inp = input("which level would you like to play? ").lower().strip()
    if inp in names:
        level = [level for level in levels if level["name"] == inp][0]
        data["level"] = load_level(inp)
        print("Transporting you to {0}".format(inp))
        printer.royal_rainbow()
        play.play_level(level, data)
    else:
        print("I'm sorry that's not an available level")

def progress(data):
    print("You're on level {0}, keep going! You can do it!".format(data["progress"]))

def save(data):
    del data["completer"]
    gen_game.save_game(data)

def quit(data):
    data["playing"] = False
    save(data)
    printer.bid_adieu()

def main():
    data = load_game()
    data["playing"] = True
    printer.welcome()
    data["completer"] = actionCompleter()
    readline.set_completer(data["completer"].complete)
    readline.parse_and_bind('tab: complete')
    actions = {"play": try_level,
               "progress": progress,
               "save": save,
               "quit": quit}
    print("Time to start playing, what would you like to do? Valid commands are {0}".format(", ".join(actions.keys())))
    while data["playing"]:
        data["completer"].set_actions(actions.keys())
        try:
            inp = input("> ").lower().strip()
            if inp in actions.keys():
                actions[inp](data)
                continue
            else:
                printer.prompt(actions.keys())
        except EOFError:
            quit(data)


if __name__ == "__main__":
    main()


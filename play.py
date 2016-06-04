import printer
import random

try:
    input = raw_input
except NameError:
    pass

def play_level(level, data):
    data["katamari"] = {"size": level["katamari"],
                        "items": []}
    data["playing_level"] = True
    data["level"] = level
    actions = {"north": north,
               "south": south,
               "east": east,
               "west": west,
               "look": look,
               "time left": time,
               "roll up": roll,
               "quit": quit}
    alt_actions = {"n": north,
                   "s": south,
                   "e": east,
                   "w": west,
                   "roll": roll,
                   "pick": roll,
                   "pick up": roll,
                   "time": time,
                   "t": time,
                   "q": quit,
                   "r": roll,
                   "l": look,
                   "examine": look}
    printer.welcome_level(level)
    while data["playing_level"]:
        data["completer"].set_actions(actions.keys())
        inp = input("> ").lower().strip()
        if inp in actions.keys():
            actions[inp](data)
            continue
        elif inp in alt_actions.keys():
            alt_actions[inp](data)
            continue
        else:
            printer.prompt(actions.keys())

def quit(data):
    announce_win(data)
    print("exiting level")
    printer.royal_rainbow()
    data["playing_level"] = False
    data["level"] = {}
    data["katamari"] = {}

def tick_time(data):
    data["level"]["time"] -= 1
    if data["level"]["time"] == 60:
        printer.minute_warning()
    elif data["level"]["time"] == 0:
        printer.times_up()
        quit(data)

def announce_win(data):
    size = recalc_katamari(data)
    printer.final_size(size)
    if check_win(data):
        printer.win()
        if data["progress"] == data["level"]["number"]:
            data["progress"] += 1
    else:
        printer.failure()

def check_win(data):
    size = recalc_katamari(data)
    if size > data["level"]["goal"]:
        return True
    else:
        return False


def move_to(place, data):
    katamari = data["katamari"]
    if in_bounds(place, data):
        data["level"]["location"] = place
        look_at((0, 0), data)
        tick_time(data)
    else:
        print("Ahh but you can't move there! Sorry, that's not in bounds")

def time(data):
    time_left = data["level"]["time"]
    goal = data["level"]["goal"]
    if check_win(data):
        print("You're over your goal of {0}cm, phew! But you still have {1}m{2}s to make your Katamari as big as possible! Get to it!".format(goal, time_left/60, time_left%60))
    else:
        print("You have {0}m{1}s left to get your katamari up to {2}cm, better hurry!".format(time_left/60, time_left%60, goal))

def roll(data):
    place = data["level"]["location"]
    items = data["level"]["grid"][place[1]][place[0]]
    item_names = [item["name"].lower() for item in items]
    data["completer"].set_actions(item_names)
    to_roll = input("Roll what? ").lower().strip()
    targets = [item for item in items if item["name"].lower() == to_roll]
    if len(targets) > 0:
        item = targets[0]
        if item["size"] <= recalc_katamari(data) / 2.0:
            items.remove(item)
            data["katamari"]["items"].append(item)
            printer.pickup(item["name"])
            printer.status(recalc_katamari(data))
        elif item["size"] <= recalc_katamari(data) / 1.9:
            printer.bump(item["name"])
        else:
            printer.fail(item["name"])
            smash_katamari(data)
        tick_time(data)
    else:
        print("I'm sorry, I don't see that item here")

def recalc_katamari(data):
    katamari = data["katamari"]
    sizes = [(4.19 * (item["size"]/2.0)**3) for item in katamari["items"]]
    sizes.append((4.1887 * (data["level"]["katamari"]/2.0) ** 3))
    volume = sum(sizes)
    size = ((volume / 4.1887) ** (1.0/3.0))*2
    return size

def smash_katamari(data):
    katamari = data["katamari"]
    for i in range(random.randint(0,min(3, len(katamari["items"])))):
        item = random.choice(katamari["items"])
        printer.lose(item["name"])
        katamari["items"].remove(item)
        loc = data["level"]["location"]
        data["level"]["grid"][loc[1]][loc[0]].append(item)
    printer.status(recalc_katamari(data))

def north(data):
    printer.move("north")
    loc = data["level"]["location"]
    place = (loc[0], loc[1] - 1)
    move_to(place, data)

def south(data):
    printer.move("south")
    loc = data["level"]["location"]
    place = (loc[0], loc[1] + 1)
    move_to(place, data)

def east(data):
    printer.move("east")
    loc = data["level"]["location"]
    place = (loc[0] + 1, loc[1])
    move_to(place, data)

def west(data):
    printer.move("west")
    loc = data["level"]["location"]
    place = (loc[0] - 1, loc[1])
    move_to(place, data)

def desc_katamari(data):
    katamari = data["katamari"]
    print("What a beautiful katamari!")
    print("Your katamari is {0}cm".format(str(recalc_katamari(data))))
    if len(katamari["items"]):
        print("Your katamari is made up of {0}".format(", ".join([item["name"] for item in katamari["items"]])))
    else:
        print("Your katamari is totally empty! It's a blank slate!")
    goal = data["level"]["goal"]
    if katamari["size"] < goal:
        print("Your katamari needs to be {0}cm before the end of the round, better hurry!".format(goal))
        print("Move with N, S, E, W, and use Roll Up to add items to your Katamari")

def look(data):
    options = {"n": (0, -1),
               "s": (0, 1),
               "e": (1, 0),
               "w": (-1, 0),
               "here": (0,0)}
    alt_options = {"north": (0, -1),
                   "south": (0, 1),
                   "east": (1, 0),
                   "west": (-1, 0),
                   "h": (0, 0)}
    katamari = {"katamari" : ""}
    prompt = "N, S, E, W, Here, or Katamari"
    data["completer"].set_actions(options.keys())
    inp = input("look which direction? ({0}) ".format(prompt)).lower().strip()
    if inp in options.keys():
        look_at(options[inp], data)
    elif inp in alt_options.keys():
        look_at(alt_options[inp], data)
    elif inp in katamari.keys():
        desc_katamari(data)
    else:
        print("Please choose a valid option, options are {0}".format(prompt))

def look_at(transform, data):
    loc = data["level"]["location"]
    place = (loc[0] + transform[0], loc[1] + transform[1])
    if in_bounds(place, data):
        space = data["level"]["grid"][place[1]][place[0]]
        if transform == (0, 0):
            print("You're standing firmly on the ground, with {0} items around you".format(str(len(space))))
        else:
            print("When you look that direction you see {0} items".format(str(len(space))))
        for item in space:
            print("You see a {0}".format(item["name"]))

def in_bounds(place, data):
    if 0 <= place[0] < data["level"]["dimensions"][0] and 0 <= place[1] < data["level"]["dimensions"][1]:
        return True
    else:
        return False

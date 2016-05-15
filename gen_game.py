import json

test_level = {"dimensions": (6, 6),
              "items": [{"name": "banana",
                         "size": 10,
                         "location": (2,2)},
                        {"name": "eraser",
                         "size": 3,
                         "location": (4,4)}],
              "name": "test_level",
              "number": 0,
              "status": "unbeaten",
              "location": (3,3),
              "goal": 15,
              "katamari": 10}

def write_level(level, level_name):
    file_name = level_name + ".json"
    with open(file_name, 'w') as f:
        json.dump(level, f)

def save_game(data):
    with open("data.json", 'w') as f:
        json.dump(data, f)

def construct_level(level):
    grid = []
    dimensions = level["dimensions"]
    for i in range(dimensions[1]):
        row = []
        for i in range(dimensions[0]):
            row.append([])
        grid.append(row)
    for item in level["items"]:
        loc = item["location"]
        grid[loc[0]][loc[1]].append({"name": item["name"],
                                     "size": item["size"]})
    level["grid"] = grid
    write_level(level, level["name"])
    return level

def create_data():
    data = {"playing": False,
            "playing_level": False,
            "level": {},
            "progress": 0,
            "katamari": {},
            "levels": [test_level]}
    for idx, level in enumerate(data["levels"]):
        data["levels"][idx] = construct_level(level)
    save_game(data)

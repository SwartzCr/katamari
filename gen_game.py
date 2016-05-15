import json
import levels

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
    for item_tup in level["items"]:
        item, loc = item_tup
        grid[loc[0]][loc[1]].append(item)
    level["grid"] = grid
    write_level(level, level["name"])
    return level

def create_data():
    data = {"playing": False,
            "playing_level": False,
            "level": {},
            "progress": 1,
            "katamari": {},
            "levels": []}
    for level in levels.levels:
        data["levels"].append(construct_level(level))
    save_game(data)

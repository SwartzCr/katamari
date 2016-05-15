

banana = {"name": "banana",
          "size": 10,
          "description": "A bright yellow banana, not too ripe"}
eraser = {"name": "eraser",
          "size": 3,
          "description": "A small eraser for a pencil"}

test_level = {"dimensions": (6, 6),
              "name": "test_level",
              "number": 0,
              "status": "unbeaten",
              "location": (3, 3),
              "goal": 15,
              "katamari": 10,
              "items" : [(banana, (2,2)),
                         (eraser, (3,3))]}

starter_house = {"dimensions": (10, 10),
                 "name": "starter_house",
                 "number": 1,
                 "status": "unbeaten",
                 "location": (4, 4),
                 "goal": 20,
                 "katamari": 10,
                 "items": []}

levels = [test_level, starter_house]

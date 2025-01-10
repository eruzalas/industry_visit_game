from graphics import window
import pyglet
import road
import random
import collision_preset

class Game_Map(object):
    def __init__(self, filename):
        self.filename = filename.rstrip()
        self.player_xpos = 0
        self.player_ypos = 0
        self.roads = []
        self.presets = []

        self.car_limit = 0

        self.left_traffic_spawns = []
        self.right_traffic_spawns = []

        self.text = []

        self.reading_text = False

        self.process_filename()

    def process_filename(self):
        filename = "game_files/maps/" + self.filename
        f = open(filename, "r")
        lines = f.readlines()

        xpos = 0
        ypos = 0

        index = 0
        for line in lines:
            if len(line) == 0 or line[0] == "#":
                continue

            if index == 0:
                if line.rstrip() != "FIN":
                    self.car_limit = int(line.rstrip())
                    index += 1
                    continue

                else:
                    self.reading_text = True
                    index += 1
                    continue

            if not self.reading_text:
                line = line.split(',')
                entity = line[0]

                if len(line) == 2:
                    if entity == "+":
                        self.left_traffic_spawns.append(int(line[1]))
                        
                    else:
                        self.right_traffic_spawns.append(int(line[1]))

                    continue

                else:
                    xpos = int(line[1])
                    ypos = int(line[2])

                if entity == "player":
                    self.player_xpos = xpos
                    self.player_ypos = ypos
                    continue

                elif "road" in entity:
                    genroad = road.Road(xpos, ypos, entity)
                    self.roads.append(genroad)
                    continue

                else:
                    shape = collision_preset.Collision_Preset(xpos, ypos, entity)
                    self.presets.append(shape)

            else:
                self.text.append(line.rstrip())

        f.close()


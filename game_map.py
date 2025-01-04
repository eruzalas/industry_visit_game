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

        self.process_filename()

    def process_filename(self):
        filename = "game_files/maps/" + self.filename
        f = open(filename, "r")
        lines = f.readlines()

        index = 0
        for line in lines:
            if len(line) == 0 or line[0] == "#":
                continue

            if index == 0:
                self.car_limit = int(line.rstrip())
                index += 1
                continue

            line = line.split(',')
            entity = line[0]
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

        f.close()
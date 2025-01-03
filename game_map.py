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

        self.process_filename()

    def process_filename(self):
        filename = "game_files/maps/" + self.filename
        f = open(filename, "r")
        lines = f.readlines()

        for line in lines:
            if len(line) == 0 or line[0] == "#":
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
                result = self.process_road(entity)
                genroad = road.Road(xpos, ypos, result[0], result[1])
                self.roads.append(genroad)
                continue

            else:
                preset = self.process_preset(entity)
                shape = collision_preset.Collision_Preset(xpos, ypos, preset[0], preset[1], preset[2])
                self.presets.append(shape)

        f.close()

    def process_road(self, roadfile):
        filename = "game_files/maps/presets/" + roadfile
        f = open(filename, "r")
        lines = f.readlines()

        length = 0
        width = 0

        for line in lines:
            if len(line) == 0 or line[0] == "#":
                continue
            
            split = line.split(',')
            
            if len(split) == 2:
                length = split[0]
                width = split[1]

        f.close()
        return [int(length), int(width)]


    def process_preset(self, presetname):
        filename = "game_files/maps/presets/" + presetname
        f = open(filename, "r")
        lines = f.readlines()

        length = 0
        width = 0
        color = []
        is_random = True

        for line in lines:
            if len(line) == 0 or line[0] == "#":
                continue

            if line.rstrip() == "NO":
                is_random = False
                continue
            
            split = line.split(',')
            
            if len(split) == 2:
                length = split[0]
                width = split[1]

            else:
                if is_random:
                    color = []
                    i = 0
                    while i < 3:
                        rand_val = random.randint(int(split[i]) - 10, int(split[i]) + 10)
                        if rand_val < 0:
                            rand_val = 0
                        elif rand_val > 255:
                            rand_val = 255
                        color.append(rand_val)
                        i += 1
                else:
                    color = [int(split[0]), int(split[1]), int(split[2])]

        f.close()
        return [int(length), int(width), color]

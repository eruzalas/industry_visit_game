from graphics import window
import pyglet
import road

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
        preset = []

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
                preset.extend([xpos, ypos])
                preset.extend(self.process_preset(entity))

            self.presets.append(preset)

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

        return [int(length), int(width)]


    def process_preset(self, presetname):
        filename = "game_files/maps/presets/" + presetname
        f = open(filename, "r")
        lines = f.readlines()

        length = 0
        width = 0
        color = []

        for line in lines:
            if len(line) == 0 or line[0] == "#":
                continue
            
            split = line.split(',')
            
            if len(split) == 2:
                length = split[0]
                width = split[1]

            else:
                color = [int(split[0]), int(split[1]), int(split[2])]

        return [int(length), int(width), color]

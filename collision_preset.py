import pyglet
import game
from graphics import COLOUR_NAMES, window
import random

class Collision_Preset(object):
    def __init__(self, x, y, filename):
        self.filename = filename
        self.xpos = x
        self.ypos = y
        self.width = 0
        self.height = 0
        self.colliding = True
        self.process_preset()
        self.display = pyglet.shapes.Rectangle(x, y, self.width, self.height, self.color)

    def request_collision_state(self, xpos, ypos):
        if self.colliding:
            if (self.xpos + self.width <= xpos):
                return False
            
            if (self.xpos >= xpos + 20):
                return False
            
            if (self.ypos + self.height <= ypos):
                return False
            
            if (self.ypos >= ypos + 20):
                return False
            
            return True
    

    def process_preset(self):
        filename = "game_files/maps/presets/" + self.filename
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
        self.width = int(length)
        self.height = int(width)
        self.color = color
        self.colliding = is_random
import pyglet
import game
import random
from graphics import COLOUR_NAMES, window

class GameObject(object):
    def __init__(self, x, y, filename):
        self.xpos = x
        self.ypos = y
        self.width = 0
        self.length = 0
        self.display = []
        self.filename = filename

        if "COL" not in self.filename:
            if "txt" in self.filename:
                self.process_textbased_preset()

            else:
                self.process_image()

    def process_image(self):
        filename = "game_files/maps/presets/" + self.filename
        f = open(filename, "rb")
        image = pyglet.image.load(self.filename, file=f)
        self.display.append(pyglet.sprite.Sprite(image, self.xpos, self.ypos))


    def process_textbased_preset(self):
        filename = "game_files/maps/presets/" + self.filename
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
        self.length = int(length)
        self.width = int(width)
import pyglet
import game
from graphics import COLOUR_NAMES, window

class Road(object):
    def __init__(self, x, y, filename):
        self.xpos = x
        self.ypos = y
        self.length = 0
        self.width = 0
        self.display = []
        self.filename = filename

        if "txt" in self.filename:
            self.process_road_preset()
            self.generate_road()

        else:
            self.process_road_image()


    def generate_road(self):
        self.display.append(pyglet.shapes.Rectangle(self.xpos, self.ypos - 30, self.length, self.width + 60, (75, 75, 75)))
        self.display.append(pyglet.shapes.Rectangle(self.xpos, self.ypos, self.length, self.width, (0, 0, 0)))
        calc = self.ypos + (self.width / 2) - 2
        self.display.append(pyglet.shapes.Rectangle(self.xpos, calc, self.length, 4, (235, 235, 52)))


    def process_road_image(self):
        filename = "game_files/maps/presets/" + self.filename
        f = open(filename, "rb")
        image = pyglet.image.load(self.filename, file=f)
        self.display.append(pyglet.sprite.Sprite(image, self.xpos, self.ypos))


    def process_road_preset(self):
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
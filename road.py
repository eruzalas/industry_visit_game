import pyglet
import game
from graphics import COLOUR_NAMES, window

class Road(object):
    def __init__(self, x, y, length, width):
        self.xpos = x
        self.ypos = y
        self.length = length
        self.width = width
        self.display = []
        self.generate_road()

    def generate_road(self):
        self.display.append(pyglet.shapes.Rectangle(self.xpos, self.ypos - 40, self.length, self.width + 80, (55, 55, 55)))
        self.display.append(pyglet.shapes.Rectangle(self.xpos, self.ypos, self.length, self.width, (0, 0, 0)))
        calc = self.ypos + (self.width / 2) - 2
        self.display.append(pyglet.shapes.Rectangle(self.xpos, calc, self.length, 4, (235, 235, 52)))
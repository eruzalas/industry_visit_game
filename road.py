import pyglet
import game
from gameobject import GameObject
from graphics import COLOUR_NAMES, window

class Road(GameObject):
    def __init__(self, x, y, filename):
        super().__init__(x, y, filename)
        if "txt" in self.filename:
            self.generate_road()


    def generate_road(self):
        self.display.append(pyglet.shapes.Rectangle(self.xpos, self.ypos - 30, self.length, self.width + 60, (75, 75, 75)))
        self.display.append(pyglet.shapes.Rectangle(self.xpos, self.ypos, self.length, self.width, (0, 0, 0)))
        calc = self.ypos + (self.width / 2) - 2
        self.display.append(pyglet.shapes.Rectangle(self.xpos, calc, self.length, 4, (235, 235, 52)))

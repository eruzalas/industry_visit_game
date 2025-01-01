import pyglet
import game
from graphics import COLOUR_NAMES, window

class Player(object):
    def __init__(self, stress, money, x, y):
        self.stress = stress
        self.money = money
        self.xpos = x
        self.ypos = y
        self.color = COLOUR_NAMES['PURPLE']
        self.display = pyglet.shapes.Rectangle(self.xpos, self.ypos, 20, 20, self.color, batch=window.get_batch("gui"))

    def update(self, delta):
        if window.keys[pyglet.window.key.W]:
            self.display.y += 10
            
        if window.keys[pyglet.window.key.A]:
            self.display.x -= 10
            
        if window.keys[pyglet.window.key.S]:
            self.display.y -= 10
            
        if window.keys[pyglet.window.key.D]:
            self.display.x += 10
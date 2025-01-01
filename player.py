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
        self.display = pyglet.shapes.Rectangle(self.xpos, self.ypos, 100, 100, self.color, batch=window.get_batch("gui"))
        self.keys_pressed = {
			pyglet.window.key.W: False,
			pyglet.window.key.A: False,
			pyglet.window.key.S: False,
			pyglet.window.key.D: False
		}

    def update(self, delta):
        #noth
        self.money += 1

    def input_keyboard(self, symbol, modifiers):
        if symbol in self.keys_pressed:
            self.keys_pressed[symbol] = True
            
	def	input_keyboard_release(self, symbol, modifiers):
        # Stop moving when the key is released
        if symbol in self.keys_pressed:
            self.keys_pressed[symbol] = False
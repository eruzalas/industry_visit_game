import pyglet
import game
from graphics import COLOUR_NAMES, window

class Phone(object):
    def __init__(self, player):
        self.player = player
        self.cars_ordered = 0
        self.display = []
        self.generate_static_display()
        
    def generate_static_display(self):
        self.display.append(pyglet.shapes.Rectangle(0, 0, 320, window.size[1], (0, 0, 0), batch=window.get_batch("gui")))
        self.display.append(pyglet.text.Label('Interface', font_size=20, x = 160, y = window.size[1] - 40, anchor_x='center', anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255, 255)))



# check player input and affect player status
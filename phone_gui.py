import pyglet
import game
from graphics import COLOUR_NAMES, window

class Phone(object):
    def __init__(self, player):
        self.player = player
        self.cars_ordered = 0
        
        self.display_gui = pyglet.shapes.Rectangle(0, 0, 320, window.size[1], (0, 0, 0), batch=window.get_batch("gui"))
        label = pyglet.text.Label('TESTING PHONE OUTPUT???', font_size=36, x = 0, y = 0, anchor_x='center', anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255))


# check player input and affect player status
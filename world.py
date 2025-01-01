import pyglet
from graphics import window
from matrix33 import Matrix33
from vector2d import Vector2D
import player

class World(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy

        # enable pause
        self.paused = True

        self.player = None

        # set world increment timer
        self.timer = 0
        self.game_maps = []
        self.process_file()

    def process_file(self):
        self.player = player.Player(100, 100, 100, 100)
        
    def update(self, delta):
        if not self.paused:
            self.player.update(delta)

    def input_keyboard(self, symbol, modifiers):
        if symbol == pyglet.window.key.P:
            self.paused = not self.paused

        else:
            self.player.input_keyboard(symbol, modifiers)

    def timer_increment(self, delta):
        if not self.paused:
            self.timer += 1

    def reset(self):
        self.timer = 0
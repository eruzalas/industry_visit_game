import pyglet
from graphics import window
from matrix33 import Matrix33
from vector2d import Vector2D

class World(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        # enable pause
        self.paused = True
        # set world increment timer
        self.timer = 0
        self.game_maps = []
        self.process_file()
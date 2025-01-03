import pyglet
import game
from graphics import COLOUR_NAMES, window

class Player(object):
    def __init__(self, stress, money, x, y, cx, cy):
        self.stress = stress
        self.money = money
        self.worldx = cx
        self.worldy = cy
        self.color = COLOUR_NAMES['PURPLE']
        self.display = pyglet.shapes.Rectangle(x, y, 20, 20, self.color, batch=window.get_batch("gui"))
        self.collision_presets = []

    def update(self, delta):
        if window.keys:
            self.movement()

    def movement(self):
        if window.keys[pyglet.window.key.W] and self.display.y <= self.worldy - 25:
            self.display.y += 5
            
        if window.keys[pyglet.window.key.A] and self.display.x >= 5:
            self.display.x -= 5
            
        if window.keys[pyglet.window.key.S] and self.display.y >= 5:
            self.display.y -= 5
            
        if window.keys[pyglet.window.key.D] and self.display.x <= self.worldx - 25:
            self.display.x += 5

    def request_if_colliding(self):
        is_collided = False
        for object in self.collision_presets:
            is_collided = object.request_collision_state(self.display.x, self.display.y)

        return is_collided
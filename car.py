import pyglet
import game
import random
from gameobject import GameObject
from graphics import COLOUR_NAMES, window

class Car(GameObject):
    def __init__(self, x, y, filename, is_special):
        super().__init__(x, y, filename)
        self.roads = []
        self.player = None
        self.direction = random.randrange(0, 2)
        self.is_special = is_special
        self.colors = ["RED", "BLUE", "GREEN", "PINK", "GREY", "YELLOW"]
        self.color = COLOUR_NAMES[self.colors[random.randrange(0, len(self.colors))]]
        if is_special:
            self.color = COLOUR_NAMES["AQUA"]
        self.display = pyglet.shapes.Rectangle(0, 620, 50, 20, self.color, batch=window.get_batch("car"))

        if self.direction == 0:
            self.display.x = 270
            self.display.y = 660
        
        else:
            self.display.x = window.size[0]


    def input_to_car(self, roads, player):
        self.roads = roads
        self.player = player


    def update(self, delta):
        if self.direction == 0:
            self.display.x += 10

        else:
            self.display.x -= 10

        if self.display.x < 270 or self.display.x > window.size[0]:
            return False
            
        return True
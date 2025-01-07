import pyglet
import game
import random
from gameobject import GameObject
from graphics import COLOUR_NAMES, window

class Car(GameObject):
    def __init__(self, x, y, filename, is_special, roads, player):
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
        
        self.roads = roads
        self.player = player

        if self.direction == 0:
            self.display.x = 270
            self.display.y = 660
        
        else:
            self.display.x = window.size[0]


    def update(self, delta):
        if self.direction == 0:
            self.display.x += 10

        else:
            self.display.x -= 10

        if self.display.x < 270 or self.display.x > window.size[0]:
            return False
            

        return True


    def check_collision_with_player(self):
        pl_xpos = self.player.display.x
        pl_ypos = self.player.display.y

        ca_xpos = self.display.x
        ca_ypos = self.display.y

        if ca_xpos + self.display.width <= pl_xpos or ca_xpos >= pl_xpos + 20 or ca_ypos + self.display.height <= pl_ypos or ca_ypos >= pl_ypos + 20:
            return "no_collision"
        
        if self.is_special:
            return "special"
        else:
            return "collision"
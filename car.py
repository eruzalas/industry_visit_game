import pyglet
import random
from gameobject import GameObject
from graphics import COLOUR_NAMES, window

# car entity inheriting from game object
class Car(GameObject):
    def __init__(self, x, y, filename, is_special, roads, player, left_spawns, right_spawns, special_color):
        # use super to get x, y and filename preset from game object parent
        super().__init__(x, y, filename)

        # set spawns for car entity
        self.left_spawns = left_spawns
        self.right_spawns = right_spawns

        # set other local variables
        self.roads = []
        self.player = None
        self.direction = random.randrange(0, 2)
        self.is_special = is_special
        self.non_colors = ["RED", "BLUE", "GREEN", "PINK", "GREY", "WHITE"]
        self.color = COLOUR_NAMES[self.non_colors[random.randrange(0, len(self.non_colors))]]

        # change colour to special colour if car is designated as "ordered" by the player
        if is_special == 0 and special_color != None:
            self.color = special_color
        self.display = pyglet.shapes.Rectangle(0, 0, 50, 20, self.color, batch=window.get_batch("car"))
        
        self.roads = roads
        self.player = player

        # set location based off direction generated
        if self.direction == 0:
            self.display.x = 270
            calc_rand = 0
            if len(self.left_spawns) > 1:
                calc_rand = random.randrange(0, len(self.left_spawns))
            self.display.y = self.left_spawns[calc_rand]
        
        else:
            self.display.x = window.size[0]
            calc_rand = 0
            if len(self.right_spawns) > 1:
                calc_rand = random.randrange(0, len(self.right_spawns))
            self.display.y = self.right_spawns[calc_rand]

    # check collision with outer walls and run movement
    def update(self, delta):
        if self.direction == 0:
            self.display.x += 10

        else:
            self.display.x -= 10

        # return info based off car status in terms of position
        if self.display.x < 270 or self.display.x > window.size[0]:
            if self.is_special == 0:
                return "special_offscreen"
            
            return "offscreen"
        
        return "onscreen"

    # check collision with player entity and return status
        # THIS IS DONE IN CAR AND NOT IN PLAYER TO HELP REDUCE NUMBER OF ITERATIONS
    def check_collision_with_player(self):
        pl_xpos = self.player.display.x
        pl_ypos = self.player.display.y

        ca_xpos = self.display.x
        ca_ypos = self.display.y

        if ca_xpos + self.display.width <= pl_xpos or ca_xpos >= pl_xpos + 20 or ca_ypos + self.display.height <= pl_ypos or ca_ypos >= pl_ypos + 20:
            return "no_collision"
        
        if self.is_special == 0:
            return "special"
        else:
            return "collision"
import pyglet
from graphics import COLOUR_NAMES, window
import phone_gui

# player entity (which is what the person playing controls and can interact using)
class Player(object):
    def __init__(self, money, x, y, cx, cy):
        # assign initialised variables
        self.stress = 0
        self.money = money
        self.worldx = cx
        self.worldy = cy
        # player colour is purple for contrast
        self.color = COLOUR_NAMES['PURPLE']
        self.display = pyglet.shapes.Rectangle(x, y, 20, 20, self.color, batch=window.get_batch("gui"))
        self.collision_presets = []
        # player possesses interface of phone to allow for environment interactivity
        self.phone = phone_gui.Phone(self)
        self.immunity_frames = 0

    # update check movement and update text depending on status
    def update(self, delta):
        if window.keys:
            self.movement()

        self.phone.display_stress.text = 'Current Stress Level: ' + str(self.stress)
        self.phone.display_money.text = 'Money Remaining: ' + str(self.money)

    # movement uses the graphics.py key check
        # basically this just runs the movement designated by the key and then checks its own status - if movement has resulted in collision then it reverses and removes that key input movement
    def movement(self):
        if window.keys[pyglet.window.key.W] and self.display.y <= self.worldy - 25:
            self.display.y += 5

            if self.request_if_colliding():
                self.display.y -= 5
            
        if window.keys[pyglet.window.key.A] and self.display.x >= 325 and not self.request_if_colliding():
            self.display.x -= 5

            if self.request_if_colliding():
                self.display.x += 5
            
        if window.keys[pyglet.window.key.S] and self.display.y >= 5 and not self.request_if_colliding():
            self.display.y -= 5

            if self.request_if_colliding():
                self.display.y += 5
            
        if window.keys[pyglet.window.key.D] and self.display.x <= self.worldx - 25 and not self.request_if_colliding():
            self.display.x += 5

            if self.request_if_colliding():
                self.display.x -= 5


    # ask objects if player is currently in a collision status with them
    def request_if_colliding(self):
        is_collided = False
        for object in self.collision_presets:
            check = object.request_collision_state(self.display.x, self.display.y)

            if check:
                is_collided = True

        return is_collided
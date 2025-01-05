import pyglet
import game
from graphics import COLOUR_NAMES, window

class Phone(object):
    def __init__(self, player):
        self.player = player
        self.cars_ordered = 0
        self.display = []
        self.order_button = None
        self.generate_static_display()
        
    def generate_static_display(self):
        self.display.append(pyglet.shapes.Rectangle(0, 0, 320, window.size[1], (0, 0, 0), batch=window.get_batch("gui")))
        self.display.append(pyglet.text.Label('Interface', font_size=20, x = 160, y = window.size[1] - 40, anchor_x='center', anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255, 255)))
        self.order_button = pyglet.shapes.Rectangle(0, 0, 320, 40, (50, 0, 0), batch=window.get_batch("gui"))
        self.display.append(self.order_button)
        self.display.append(pyglet.text.Label('ORDER CAR', font_size=10, x = 160, y = 20, anchor_x='center', anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255, 255)))
        
    def check_mouse(self, x, y, button):
        if button == 1:
            print(x, y)
            return self.check_click_with_button(x, y, self.order_button)
        

    def check_click_with_button(self, ix, iy, button):
        ex = button.x
        ey = button.y

        if ix >= ex and ix <= ex + button.width and iy >= ey and iy <= ey + button.height:
            return True
        
        return False

# check player input and affect player status
import pyglet
from graphics import window

# this phone object loads information for display and to allow the player to interact with the cars (in terms of ordering)
class Phone(object):
    def __init__(self, player):
        # set local variables
        self.player = player
        self.cars_ordered = 0
        self.display = []
        self.order_button = None
        self.order_text = None
        # generate basis for display
        self.generate_static_display()

        # initialise text objects
        self.car_color_text = pyglet.text.Label('Loading...', font_size=10, x = 160, y = 300, anchor_x='center', anchor_y='center', color = (255, 255, 255, 255))
        self.display_stress = pyglet.text.Label('Loading...', font_size=16, x = 20, y = window.size[1] - 110, anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255, 255))
        self.display_money = pyglet.text.Label('Loading...', font_size=16, x = 20, y = window.size[1] - 160, anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255, 255))
        
    # set basic display for the black window, interface text and ordering text/button
    def generate_static_display(self):
        self.display.append(pyglet.shapes.Rectangle(0, 0, 320, window.size[1], (0, 0, 0), batch=window.get_batch("gui")))
        self.display.append(pyglet.text.Label('Interface', font_size=20, x = 160, y = window.size[1] - 40, anchor_x='center', anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255, 255)))
        self.order_button = pyglet.shapes.Rectangle(0, 180, 320, 80, (128, 0, 0), batch=window.get_batch("gui"))
        self.order_text = pyglet.text.Label('Loading...', font_size=16, x = 160, y = 220, anchor_x='center', anchor_y='center', batch=window.get_batch("gui"), color = (255, 255, 255, 255))
        
    # check position of mouse
    def check_mouse(self, x, y, button):
        if button == 1:
            return self.check_click_with_button(x, y, self.order_button)
        
    # reset by ensuring objects stop rendering
    def reset(self):
        self.display_stress.batch = None
        self.display_money.batch = None
        for display in self.display:
            display.batch = None
        self.order_button.batch = None
        self.order_text = None
        self.car_color_text.batch = None

    # if mouse click is within button zone then return true
    def check_click_with_button(self, ix, iy, button):
        ex = button.x
        ey = button.y

        if ix >= ex and ix <= ex + button.width and iy >= ey and iy <= ey + button.height:
            return True
        
        return False
    
    # update the display based off progress of car which was scheduled 
        # this just impacts text and colour of the order button
    def update_display(self, car_scheduling):
        if car_scheduling == -1:
            self.order_text.text = 'ORDER CAR ($10)'
            self.order_button.color = (128, 0, 0, 255)
            self.car_color_text.batch = None

        elif car_scheduling <= 0:
            self.order_text.text = 'CAR HAS ARRIVED'
            self.order_button.color = (0, 128, 0, 255)

        else:
            self.order_text.text = 'CAR ARRIVING IN: ' + str(car_scheduling)
            self.order_button.color = (179, 71, 0, 255)

        if self.player.money < 10 and car_scheduling == -1:
            self.order_text.text = "INSUFFICIENT FUNDS"
            self.order_button.color = (128, 0, 0, 255)
            self.car_color_text.batch = None


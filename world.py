import pyglet
from graphics import window, COLOUR_NAMES
import player
import random
import car

# define world object which controls updating of entities
class World(object):
    def __init__(self, cx, cy):
        # set variables
        self.cx = cx
        self.cy = cy
        self.paused = True
        self.player = None

        self.initial_pos = []
        self.initial_money = 0

        self.timer = 0
        self.game_state = "running"
        self.car_limit = 0

        self.game_obj = []
        self.roads = []
        self.existing_cars = []
        
        self.special_car_scheduled = -1
        self.select_color = None

        self.display_text = []
        
    # run update if not paused
    def update(self, delta):
        if not self.paused:
            # check player immunity frames and alter them based off number
            if self.player.immunity_frames > 0:
                self.player.immunity_frames -= 1

            # run player update
            self.player.update(delta)

            # run car update
            for car in self.existing_cars:
                status = car.update(delta)

                # check collision and alter based off collision
                if car.check_collision_with_player() == "collision":
                    if self.player.immunity_frames == 0:
                        self.player.immunity_frames = 5

                elif car.check_collision_with_player() == "special":
                    self.game_state = "passed"

                # check car status and alter based off this
                if status == "offscreen":
                    self.existing_cars.remove(car)
                
                elif status == "special_offscreen":
                    self.special_car_scheduled = -1
                    self.existing_cars.remove(car)

            self.check_cars(delta)

            # reduce car scheduled timer
            if self.special_car_scheduled > 0:
                self.special_car_scheduled -= 1

            # request update of display
            self.player.phone.update_display(self.special_car_scheduled)

            # increase player stress based off immunity frames
            if self.player.immunity_frames == 5:
                self.player.stress += 10
                #print("PLAYER STRESS HAS INCREASED TO " + str(self.player.stress))

    # check cars and add a new one if there are not enough cars on screen (in terms of map pre-set car limit)
    def check_cars(self, delta):
        if len(self.existing_cars) < self.car_limit and self.timer > 1:
            color = self.select_color

            # add car
            self.existing_cars.append(car.Car(0, 0, "car.txt", self.special_car_scheduled, self.roads, self.player, self.left_car_spawn, self.right_car_spawn, color))
            
            # remove scheduling if scheduled car has been loaded
            if self.special_car_scheduled == 0:
                self.special_car_scheduled = -2
                self.select_color = None

            self.reset()

    # check mouse input
    def input_mouse(self, x, y, button, modifiers):
        result = self.player.phone.check_mouse(x, y, button)
        # if mouse input was in terms of ordering a car, then change values to allow for ordering of a car
        if result and self.special_car_scheduled == -1 and self.player.money >= 10:
            self.special_car_scheduled = random.randrange(100, 300)
            self.player.money -= 10
            special_colors = ["YELLOW", "AQUA", "ORANGE", "DARK_GREEN", "LIGHT_GREEN", "LIGHT_BLUE"]
            precolor = special_colors[random.randrange(0, len(special_colors))]
            color = COLOUR_NAMES[precolor]
            self.player.phone.car_color_text.text = "ORDERED CAR COLOUR IS: " + precolor
            self.player.phone.car_color_text.batch = window.get_batch("gui")
            self.select_color = color

    # increment timer
    def timer_increment(self, delta):
        if not self.paused:
            self.timer += 1

    # reset timer
    def reset(self):
        self.timer = 0

    # check game state based off player stress
    def check_game_state(self):
        if not self.paused:
            if self.player.stress >= 100:
                self.game_state = "failed"

        return self.game_state
    
    # reset map
    def reset_current_map(self):
        self.start()

    # reset player
    def reset_player(self):
        self.player.display.x = self.initial_pos[0]
        self.player.display.y = self.initial_pos[1]
        self.player.stress = 0
        self.player.money = self.initial_money
        self.special_car_scheduled = -1
        
        self.existing_cars.clear()

    # start map (via first resetting)
    def start(self, gamemap):
        if self.player != None:
            self.player.phone.reset()
            self.player.display.batch = None
        self.player = None
        self.special_car_scheduled = -1
        self.roads.clear()
        self.game_obj.clear()
        self.existing_cars.clear()

        # assign values based off gamemap loaded
        if not gamemap.reading_text:
            self.initial_pos = [gamemap.player_xpos, gamemap.player_ypos]
            self.initial_money = 50

            # generate player
            self.player = player.Player(50, gamemap.player_xpos, gamemap.player_ypos, self.cx, self.cy)

            # assign car spawns
            self.left_car_spawn = gamemap.left_traffic_spawns
            self.right_car_spawn = gamemap.right_traffic_spawns

            # if roads/preset then set batch to appropriate batch (allowing for rendering)
            if len(gamemap.roads) > 0:
                self.roads = gamemap.roads
                for road in self.roads:
                    for disp in road.display:
                        disp.batch = window.get_batch("world")

            if len(gamemap.presets) > 0:
                self.game_obj = gamemap.presets
                for obj in self.game_obj:
                    obj.display.batch = window.get_batch("main")

            # set car limit and collision objects
            self.car_limit = gamemap.car_limit
            self.player.collision_presets = self.game_obj

        else:
            # generate winning screen
            offset = window.size[1] - 50
            self.display_text.append(pyglet.shapes.Rectangle(0, 0, window.size[0], window.size[1], (0, 0, 0), batch=window.get_batch("gui")))

            for text in gamemap.text:
                self.display_text.append(pyglet.text.Label(text, font_size=20, x = 50, y = offset, anchor_y='center', color = (255, 255, 255, 255), batch=window.get_batch("gui")))
                offset -= 50

            self.paused = True
import pyglet
from graphics import window, COLOUR_NAMES
from matrix33 import Matrix33
from vector2d import Vector2D
import player
import random
import car

class World(object):
    def __init__(self, cx, cy):
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
        
    def update(self, delta):
        if not self.paused:
            if self.player.immunity_frames > 0:
                self.player.immunity_frames -= 1

            self.player.update(delta)
            for car in self.existing_cars:
                status = car.update(delta)

                if car.check_collision_with_player() == "collision":
                    if self.player.immunity_frames == 0:
                        self.player.immunity_frames = 5

                elif car.check_collision_with_player() == "special":
                    self.game_state = "passed"

                if status == "offscreen":
                    self.existing_cars.remove(car)
                
                elif status == "special_offscreen":
                    self.special_car_scheduled = -1
                    self.existing_cars.remove(car)

            self.check_cars(delta)

            if self.special_car_scheduled > 0:
                self.special_car_scheduled -= 1

            self.player.phone.update_display(self.special_car_scheduled)

            if self.player.immunity_frames == 5:
                self.player.stress += 10
                print("PLAYER STRESS HAS INCREASED TO " + str(self.player.stress))


    def check_cars(self, delta):
        if len(self.existing_cars) < self.car_limit and self.timer > 1:
            color = self.select_color

            self.existing_cars.append(car.Car(0, 0, "car.txt", self.special_car_scheduled, self.roads, self.player, self.left_car_spawn, self.right_car_spawn, color))
            if self.special_car_scheduled == 0:
                self.special_car_scheduled = -2
                self.select_color = None

            self.reset()

    def input_mouse(self, x, y, button, modifiers):
        result = self.player.phone.check_mouse(x, y, button)
        if result and self.special_car_scheduled == -1 and self.player.money >= 10:
            self.special_car_scheduled = random.randrange(100, 300)
            self.player.money -= 10
            special_colors = ["YELLOW", "AQUA", "ORANGE", "DARK_GREEN", "LIGHT_GREEN", "LIGHT_BLUE"]
            precolor = special_colors[random.randrange(0, len(special_colors))]
            color = COLOUR_NAMES[precolor]
            self.player.phone.car_color_text.text = "ORDERED CAR COLOUR IS: " + precolor
            self.player.phone.car_color_text.batch = window.get_batch("gui")
            self.select_color = color

    def timer_increment(self, delta):
        if not self.paused:
            self.timer += 1

    def reset(self):
        self.timer = 0

    def check_game_state(self):
        if self.player.stress >= 100:
            self.game_state = "failed"

        return self.game_state
    
    def reset_current_map(self):
        self.start()

    def reset_player(self):
        self.player.display.x = self.initial_pos[0]
        self.player.display.y = self.initial_pos[1]
        self.player.stress = 0
        self.player.money = self.initial_money
        self.special_car_scheduled = -1
        
        self.existing_cars.clear()

    def start(self, gamemap):
        if self.player != None:
            self.player.phone.reset()
            self.player.display.batch = None
        self.player = None
        self.special_car_scheduled = -1
        self.roads.clear()
        self.game_obj.clear()
        self.existing_cars.clear()

        self.initial_pos = [gamemap.player_xpos, gamemap.player_ypos]
        self.initial_money = 100

        self.player = player.Player(50, gamemap.player_xpos, gamemap.player_ypos, self.cx, self.cy)

        self.left_car_spawn = gamemap.left_traffic_spawns
        self.right_car_spawn = gamemap.right_traffic_spawns

        if len(gamemap.roads) > 0:
            self.roads = gamemap.roads
            for road in self.roads:
                for disp in road.display:
                    disp.batch = window.get_batch("world")

        if len(gamemap.presets) > 0:
            self.game_obj = gamemap.presets
            for obj in self.game_obj:
                obj.display.batch = window.get_batch("main")

        self.car_limit = gamemap.car_limit
        
        self.player.collision_presets = self.game_obj
import pyglet
from graphics import window
from matrix33 import Matrix33
from vector2d import Vector2D
import player
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
        
        self.special_car_scheduled = False
        
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

                if not status:
                    self.existing_cars.remove(car)

            self.check_cars(delta)

            if self.player.immunity_frames == 5:
                self.player.stress += 10
                print("PLAYER STRESS HAS INCREASED TO " + str(self.player.stress))


    def check_cars(self, delta):
        if len(self.existing_cars) < self.car_limit and self.timer > 1:
            self.existing_cars.append(car.Car(0, 0, "car.txt", self.special_car_scheduled, self.roads, self.player))
            self.special_car_scheduled = False
            self.reset()

    def input_mouse(self, x, y, button, modifiers):
        result = self.player.phone.check_mouse(x, y, button)
        if result:
            self.special_car_scheduled = True

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
        self.special_car_scheduled = False
        
        self.existing_cars.clear()

    def start(self, gamemap):
        self.player = None
        self.special_car_scheduled = False
        self.roads.clear()
        self.game_obj.clear()
        self.existing_cars.clear()

        self.initial_pos = [gamemap.player_xpos, gamemap.player_ypos]
        self.initial_money = 100

        self.player = player.Player(100, gamemap.player_xpos, gamemap.player_ypos, self.cx, self.cy)

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
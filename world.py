import pyglet
from graphics import window
from matrix33 import Matrix33
from vector2d import Vector2D
import player

class World(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.paused = True
        self.player = None

        self.timer = 0
        self.game_state = "running"

        self.game_obj = []
        self.roads = []
        
    def update(self, delta):
        if not self.paused:
            self.player.update(delta)

    def timer_increment(self, delta):
        if not self.paused:
            self.timer += 1

    def reset(self):
        self.timer = 0

    def check_game_state(self):
        return self.game_state
    
    def reset_current_map(self):
        print("RESETTING")

    def start(self, gamemap):
        self.player = None
        self.roads.clear()
        self.game_obj.clear()

        self.player = player.Player(100, 100, gamemap.player_xpos, gamemap.player_ypos, self.cx, self.cy)

        if len(gamemap.roads) > 0:
            self.roads = gamemap.roads
            for road in self.roads:
                for disp in road.display:
                    disp.batch = window.get_batch("world")

        if len(gamemap.presets) > 0:
            self.game_obj = gamemap.presets
            for obj in self.game_obj:
                obj.display.batch = window.get_batch("main")

        self.player.collision_presets = self.game_obj
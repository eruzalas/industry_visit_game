game = None
from world import World
from graphics import window
import game_map
import pyglet

class Game():
	def __init__(self):
		self.world = World(window.size[0], window.size[1])
		self.world.paused = False
		self.map_stage = 0
		self.game_maps = []
		self.load_maps()

		self.background = pyglet.shapes.Rectangle(0, 0, window.size[0], window.size[1], (71, 117, 66), batch=window.get_batch("main"))

		self.world.start(self.game_maps[self.map_stage])

	def load_maps(self):
		filename = "game_files/maps/map_list.txt"
		f = open(filename, "r")
		map_list = f.readlines()

		for entry in map_list:
			if len(entry) == 0 or entry[0] == "#":
				continue

			generate_map = game_map.Game_Map(entry)

			self.game_maps.append(generate_map)
			
		f.close()
	

	def input_mouse(self, x, y, button, modifiers):
		self.world.input_mouse(x, y, button, modifiers)


	def update(self, delta):
		if window.keys[pyglet.window.key.M]:
			self.update_game_stage()

		self.world.update(delta)
		status = self.world.check_game_state()

		if status == "passed":
			self.update_game_stage()
		
		elif status == "failed":
			self.world.reset_current_map()


	def update_game_stage(self):
		if self.map_stage < len(self.game_maps) - 1:
			self.map_stage += 1
			self.world.start(self.game_maps[self.map_stage])
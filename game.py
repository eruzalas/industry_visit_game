game = None
from world import World
from graphics import window
import game_map
import pyglet

# load the game entity which will host the whole game
class Game():
	def __init__(self):
		# define world for visual rendering and its status as paused or not
		self.world = World(window.size[0], window.size[1])
		self.world.paused = False

		# set map information and load
		self.map_stage = 0
		self.game_maps = []
		self.load_maps()

		# define colour of background (green)
		self.background = pyglet.shapes.Rectangle(0, 0, window.size[0], window.size[1], (71, 117, 66), batch=window.get_batch("main"))

		# if you want to play a certain map, change the "self.map_stage" in the square brackets to a number (0 - 2)
		self.world.start(self.game_maps[self.map_stage])

	# load map using pyglet
	def load_maps(self):
		# get full path, open and read
		filename = "game_files/maps/map_list.txt"
		f = open(filename, "r")
		map_list = f.readlines()

		# loop and generate game map for each line
		# add game map to list
		for entry in map_list:
			if len(entry) == 0 or entry[0] == "#":
				continue

			generate_map = game_map.Game_Map(entry)
			self.game_maps.append(generate_map)
			
		f.close()
	
	# send input to world
	def input_mouse(self, x, y, button, modifiers):
		self.world.input_mouse(x, y, button, modifiers)

	# run update for entities
	def update(self, delta):
		self.world.update(delta)

		# check status of world and react based off this
		status = self.world.check_game_state()
		if status == "passed":
			self.update_game_stage()
		
		elif status == "failed":
			self.world.reset_player()

		self.world.game_state = "running"

		# you can press R to reset character
		if window.keys[pyglet.window.key.R]:
			self.world.reset_player()

	# update game stage code which increments and starts
	def update_game_stage(self):
		if self.map_stage < len(self.game_maps) - 1:
			self.map_stage += 1
			self.world.start(self.game_maps[self.map_stage])
game = None
from world import World
from graphics import window
import pyglet

class Game():
	def __init__(self):
		self.world = World(window.size[0], window.size[1])
		self.world.paused = False

	def update(self, delta):
		self.world.update(delta)
		
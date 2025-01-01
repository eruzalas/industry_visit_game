game = None
from world import World
from graphics import window

class Game():
	def __init__(self):
		self.world = World(window.size[0], window.size[1])
		self.world.paused = False

	def input_keyboard(self, symbol, modifiers):
		self.world.input_keyboard(symbol, modifiers)

	def update(self, delta):
		self.world.update(delta)
		
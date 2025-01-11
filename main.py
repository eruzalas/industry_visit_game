import pyglet
import game

# this is the main file for running the game

if __name__ == '__main__':
	# generate the files for running the game + adding a window etc
	game.game = game.Game()

	# schedule updates to occur
	pyglet.clock.schedule_interval(game.game.update, 1/60.)

	# schedule world timer (decrease this to speed up spawnrate of cars)
	pyglet.clock.schedule_interval(game.game.world.timer_increment, 1/10)

	# run
	pyglet.app.run()
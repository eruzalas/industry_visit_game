import pyglet
import game

if __name__ == '__main__':
	game.game = game.Game(map_choice, is_group)
	pyglet.clock.schedule_interval(game.game.update, 1/60.)
	pyglet.clock.schedule_interval(game.game.world.timer_increment, 1)
	pyglet.app.run()

import pyglet
from pyglet.gl import *
from pyglet.window import key
from system.component import Component
from entities.player import Player
import numpy as np
from entities.ball import Ball
import config
from system.game import Game
from pyglet import clock

conf = pyglet.gl.Config(sample_buffers = 1, samples = 16)
window = pyglet.window.Window(height = config.window_height, width = config.window_width, config = conf)

game1 = Game()
# generate list of numpy arrays (vectors)
ball1 = Ball(mult = 0, radius = 50, vel = np.array([8,6]))
for i in range(20):
    ball1.points.append(np.array([0,0]))

game1.balls.append(ball1)
game1.players.append(Player(vel = np.array([5,0])))

def draw():
    game1.draw_self()

def update(time):
    print('FPS is %f' % clock.get_fps())
    game1.update_self()

def main():
    @window.event
    def on_draw():
        draw()
    dt = clock.tick()
    pyglet.clock.schedule_interval(update, 1/100)
    clock.set_fps_limit(60)
    pyglet.app.run()

main()


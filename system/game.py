import pyglet
from system.component import Component
from pyglet.gl import *
import numpy as np
import config
from pyglet.window import key
from entities.ball import Ball
from pyglet import window
from pyglet import clock
from pyglet import font

class Game(window.Window):
    def __init__(self, *args, **kwargs):
        #self.config = kwargs.get('config', stdConfig)
        #self.window = kwargs.get('window', stdWindow)
        self.balls = kwargs.get('balls', [])
        self.players = kwargs.get('players', [])

    #check if ball has collided
    def collision_check(self):
        for ball in self.balls:
            #Check for ball->game window collision
            if ball.origin[0] + ball.radius >= config.window_height or ball.origin[0]-ball.radius <= 0:
                ball.vel[0] = -ball.vel[0]
            if ball.origin[1] + ball.radius >= config.window_width or ball.origin[1]-ball.radius <= 0:
                ball.vel[1] = -ball.vel[1]
        for player in self.players:
            if player.origin[0]+player.size[0] >= config.window_height or player.origin[0] - player.size[0] <= 0:
                player.vel[0] = -player.vel[0]
            if player.origin[1] + player.size[1] >= config.window_width or player.origin[1] - player.size[1] <= 0:
                player.vel[1]= -player.vel[1]

    def update_self(self):
        #Do some calculations and what not
        self.collision_check()
        #Update all children
        for player in self.players:
            player.update_self()
        for ball in self.balls:
            #ball.vel = ball.vel + np.array([0.001, 0.002])
            #ball.mult += 0.02
            ball.update_self()

    def draw_self(self):
        self.clear()
        for ball in self.balls:
            ball.draw_self()
        for player in self.players:
            player.draw_self()

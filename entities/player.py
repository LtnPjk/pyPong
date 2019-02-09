import pyglet
from pyglet.gl import *
import numpy as np
import config

class Player():

    def __init__(self, *args, **kwargs):
        self.origin = kwargs.get('origin', np.array([config.window_width/2, config.window_height/2]))
        self.vel = kwargs.get('vel', np.array([0, 0]))
        self.scale = kwargs.get('scale', np.array([1, 1]))
        self.size = kwargs.get('size', np.array([50, 30]))
        self.rotation = kwargs.get('rotation', 0)

    def update_self(self):
        self.origin = np.add(self.origin, self.vel)

    def draw_self(self):
        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glColor3d(0.1, 0.6, 0.2)
        glLineWidth(4)
        glBegin(GL_LINES)
        glVertex2d(self.origin[0] - self.size[0]/2, self.origin[1]-self.size[1]/2)
        glVertex2d(self.origin[0], self.origin[1]+self.size[1])
        glVertex2d(self.origin[0], self.origin[1]+self.size[1])
        glVertex2d(self.origin[0]+self.size[0], self.origin[1]-self.size[1]/2)
        glVertex2d(self.origin[0] + self.size[0], self.origin[1] - self.size[1]/2)
        glVertex2d(self.origin[0] - self.size[0]/2, self.origin[1] - self.size[1]/2)
        glEnd()

import pyglet
from system.component import Component
from pyglet.gl import *
import numpy as np
import config

class Ball(Component):

    def __init__(self, *args, **kwargs):
        self.mult = kwargs.get('mult',0)
        self.points = kwargs.get('points', [])
        self.angle = kwargs.get('angle', 0.0)
        self.angVel = kwargs.get('angVel', 0.0)
        self.angAcc = kwargs.get('angAcc', 0.0)
        self.radius = kwargs.get('radius', 10)
        self.vel = kwargs.get('vel', np.array([0,0]))
        self.origin = kwargs.get('origin', np.array([config.window_width/2, config.window_height/2]))

    def update_self(self):
        #Calc new state
        pointLen = len(self.points)
        #new pos
        self.origin = np.add(self.origin, self.vel)
        #new angle
        self.angle = (self.angle + self.angVel)%(np.pi*2)
        #Calc new points
        for i, point in enumerate(self.points):
            point[0] = self.origin[0]+self.radius*np.cos(i/pointLen*np.pi*2+self.angle)
            point[1] = self.origin[1]+self.radius*np.sin(i/pointLen*np.pi*2+self.angle)

    def draw_self(self):
        #plot circle
        for point in self.points:
            glPointSize(2)
            glBegin(GL_POINTS)
            glVertex2d(point[0],point[1])
            glEnd()

        size = len(self.points)
        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glColor3d(0.1, 0.6, 0.2)
        glLineWidth(2)
        glBegin(GL_LINES)
        #draw circle
        for i in range(size):
            glVertex2d(self.points[i][0], self.points[i][1])
            glVertex2d(self.points[(i+1)%size][0], self.points[(i+1)%size][1])
        #draw time-table
        for i in range(size):
            j = int((i*self.mult)%size)
            glVertex2d(self.points[i][0], self.points[i][1])
            glVertex2d(self.points[j][0], self.points[j][1])
        glEnd()




















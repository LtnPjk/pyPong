import pyglet
import config
from pyglet.gl import *
import numpy as np
import abc

ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})

class Component(ABC):

    def __init__(self, **kwargs):
        self.active = kwargs.get('active', True)#if object has to update
        self.render = kwargs.get('render', True)#if object has to render
        self.debug = kwargs.get('debug', False)
        self.origin = kwargs.get('origin', np.array([config.window_width/2, config.window_height/2])) #center pos
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.vel = kwargs.get('vel', np.array([0,0]))
        self.acc = kwargs.get('acc', np.array([0,0]))

    @abc.abstractmethod
    def update_self(self):
        pass

    @abc.abstractmethod
    def draw_self(self):
        pass

from visible_objects import VisibleObjects

from pygame import Surface
from pygame.sprite import Sprite


class Beam(Sprite):
    '''
    A simple beam the players can stand on.
    '''
    def __init__(self, width, height, x=0, y=0):
        '''
        Constructor.
        @param width width of the beam.
        @param height height of the beam.
        '''
        super(Beam, self).__init__()
        self.color = (255, 255, 255)
        self.image = Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        VisibleObjects().register_object('beams', self)

from visible_objects import VisibleObjects
from game_config import GameConfig

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
        self.width = width
        self.height = height
        self.image = Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        VisibleObjects().register_object('beams', self)

    def update(self):
        config = GameConfig()
        self.rect.y -= 1
        if self.rect.y <= 0:
            self.rect.y = int(config.get('screen', 'height'))

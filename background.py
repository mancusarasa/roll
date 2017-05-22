import pygame

from visible_objects import VisibleObjects


class Background(pygame.sprite.Sprite):
    '''
    The screen's background.
    '''
    def __init__(self, width, height):
        super(Background, self).__init__()
        self.image = pygame.Surface([width, height])
        # paint it black
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        VisibleObjects().register_object('background', self)

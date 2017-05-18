import pygame


class Floor(pygame.sprite.Sprite):
    '''
    The floor of this fucking game.
    '''
    def __init__(self, width, height, x=0, y=0):
        '''
        Class constructor.
        '''
        super(Floor, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

import pygame


class Ball(pygame.sprite.Sprite):
    '''
    A bouncing ball, controlable by the player.
    '''
    def __init__(self, radius, x=0, y=0):
        '''
        Ball constructor.
        @param radius radius of the ball.
        @param x initial x position.
        @param y initial y position.
        '''
        super(Ball, self).__init__()
        self.radius = radius
        self.color = (0, 0, 255)
        self.image = pygame.Surface([2*radius, 2*radius], pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect()

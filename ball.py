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
        self.image = pygame.Surface([2*radius, 2*radius])
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect()

    def move_right(self):
        '''
        Moves the ball to the right
        @return None
        '''
        self.rect.x += 1

    def move_left(self):
        '''
        Moves the ball to the left.
        @return None
        '''
        self.rect.x -= 1

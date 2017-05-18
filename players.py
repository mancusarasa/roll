from ball import Ball


class FirstPlayer(object):
    '''
    A class that represents the first player.
    '''
    def __init__(self):
        '''
        Constructor.
        @param ball sprite of the ball.
        '''
        super(FirstPlayer, self).__init__()
        self.ball = Ball(10)

    def move_right(self):
        '''
        Moves the ball to the right
        @return None
        '''
        self.ball.rect.x += 1

    def move_left(self):
        '''
        Moves the ball to the left.
        @return None
        '''
        self.ball.rect.x -= 1

    def move_up(self):
        '''
        Moves the ball up.
        @return None
        '''
        self.ball.rect.y -= 1

    def move_down(self):
        '''
        Moves the ball down.
        @return None
        '''
        self.ball.rect.y += 1

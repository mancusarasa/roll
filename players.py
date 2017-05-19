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
        # idea: to perform a jump, set this (initial) speed to a 
        # convenient value. then, update the speed with this formula:
        # self.__speed_y += GRAVITY
        # self.rect.y += self.__speed_y
        self.__speed_y = 0
        # this boolean indicates if the player is in the middle of a 
        # jump, to avoid jumping twice on the same keystroke. set to
        # True when starting a jump; set to False on collision with something
        self.__midjump = False

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

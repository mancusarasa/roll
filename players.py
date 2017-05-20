from ball import Ball
from common import GRAVITY


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
        self.__speed_y = GRAVITY
        # this boolean indicates if the player is in the middle of a
        # jump, to avoid jumping twice on the same keystroke. set to
        # True when starting a jump; set to False on collision with something
        self.__midjump = False

    def update(self):
        '''
        Method called on each iteration of the main event loop, updating the
        player's option.
        @return None.
        '''
        self.ball.rect.y += self.__speed_y

    def on_right_button(self):
        '''
        Callback for the right button.
        @return None
        '''
        self.ball.rect.x += 1

    def on_left_button(self):
        '''
        Callback for the left button.
        @return None
        '''
        self.ball.rect.x -= 1

    def on_up_button(self):
        '''
        Callback for the up button.
        @return None
        '''
        self.ball.rect.y -= 1

    def on_down_button(self):
        '''
        Callback for the down button.
        @return None
        '''
        self.ball.rect.y += 1

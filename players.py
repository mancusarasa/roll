from ball import Ball
from visible_objects import VisibleObjects
from common import GRAVITY


class FirstPlayer(Ball):
    '''
    A class that represents the first player.
    '''
    def __init__(self):
        '''
        Constructor.
        @param ball sprite of the ball.
        '''
        super(FirstPlayer, self).__init__(10)
        # idea: to perform a jump, set this (initial) speed to a
        # convenient value. then, update the speed with this formula:
        # self.__speed_y += GRAVITY
        # self.rect.y += self.__speed_y
        self.__speed_y = GRAVITY
        # this boolean indicates if the player is in the middle of a
        # jump, to avoid jumping twice on the same keystroke. set to
        # True when starting a jump; set to False on collision with something
        self.__midair = False
        VisibleObjects().register_object('players', self)

    def update(self):
        '''
        Method called on each iteration of the main event loop, updating the
        player's position.
        @return None.
        '''
        if self.__midair is True:
            self.__speed_y += GRAVITY
        self.rect.y += self.__speed_y

    def move_right(self):
        '''
        Callback for the right button.
        @return None
        '''
        self.rect.x += 1

    def move_left(self):
        '''
        Callback for the left button.
        @return None
        '''
        self.rect.x -= 1

    def jump(self):
        '''
        Performs a jump.
        @return None.
        '''
        if self.__midair is False:
            self.__midair = True
            self.__speed_y = -10

    def on_collision_with_floor(self):
        '''
        Callback for the moment when the ball hits the floor.
        @return None.
        '''
        self.__speed_y = 0
        self.__midair = False

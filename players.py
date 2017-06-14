from ball import Ball
from visible_objects import VisibleObjects
from common import GRAVITY, INITIAL_JUMP_SPEED


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
        self.__speed_y = GRAVITY
        self.__midair = True
        # this 'y' is "fake". Since I'm trying to use
        # increments between 0 and 1 for the vertical movement, this
        # will keep the value with decimal positional increments
        self.y = float(self.rect.y)
        VisibleObjects().register_object('players', self)

    def update(self, screen_width):
        '''
        Method called on each iteration of the main event loop,
        updating the player's position.
        @param screen_width screen's width, to correct out of screen positions.
        @return None.
        '''
        if self.__midair is True:
            self.__speed_y += GRAVITY
        self.y += self.__speed_y
        self.rect.y = self.y
        # correct the player's position if it leaves the screen.
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= screen_width:
            self.rect.right = screen_width

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
            self.__speed_y = INITIAL_JUMP_SPEED

    def on_collision_with_floor(self):
        '''
        Callback for the moment when the ball hits the floor.
        @return None.
        '''
        self.__speed_y = 0.0
        self.__midair = False

    def on_collision_with_beam(self, beam):
        '''
        Callback for the moment when the ball hits a beam.
        @return None.
        '''
        if beam.rect.y < self.y:  # if the collision was from below
            self.__speed_y = 0.0
        else:
            self.__speed_y = 0.0
            self.__midair = False

    def resume_drop(self):
        '''
        Resumes the gravity drop.
        @return None.
        '''
        if self.__midair is False:
            self.__midair = True
            self.__speed_y = GRAVITY

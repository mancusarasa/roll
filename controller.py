import pygame
from pygame import locals


class FirstPlayerController(object):
    '''
    An object that maps the pressed keys to the first player's actions.
    '''
    def __init__(self, player):
        '''
        Class constructor.
        @param Player controlling the ball.
        '''
        super(FirstPlayerController, self).__init__()
        self.player = player

    def handle_keys(self):
        '''
        Takes the appropriate actions based on the keys pressed by the player.
        @return None.
        '''
        keys = pygame.key.get_pressed()
        if keys[locals.K_LEFT]:
            self.on_left_button()
        if keys[locals.K_RIGHT]:
            self.on_right_button()
        if keys[locals.K_UP]:
            self.on_up_button()
        if keys[locals.K_DOWN]:
            self.on_down_button()

    def on_left_button(self):
        '''
        Handler for the left button.
        @return None.
        '''
        self.player.move_left()

    def on_right_button(self):
        '''
        Handler for the left button.
        @return None.
        '''
        self.player.move_right()

    def on_up_button(self):
        '''
        Handler for the left button.
        @return None.
        '''
        self.player.jump()

    def on_down_button(self):
        '''
        Handler for the left button.
        @return None.
        '''
        pass

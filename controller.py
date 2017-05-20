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

    def take_action(self, keys):
        '''
        Takes the appropriate actions based on the keys pressed by the player.
        @param keys pressed keys.
        @return None.
        '''
        if keys[locals.K_LEFT]:
            self.player.on_left_button()
        if keys[locals.K_RIGHT]:
            self.player.on_right_button()
        if keys[locals.K_UP]:
            self.player.on_up_button()
        if keys[locals.K_DOWN]:
            self.player.on_down_button()

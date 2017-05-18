from pygame import locals


class FirstPlayerController(object):
    '''
    An object that maps the pressed keys to the first player's actions.
    '''
    def __init__(self, ball):
        '''
        Class constructor.
        @param ball Ball controlled by the player.
        '''
        super(FirstPlayerController, self).__init__()
        self.ball = ball

    def take_action(self, keys):
        '''
        Takes the appropriate actions based on the keys pressed by the player.
        @param keys pressed keys.
        @return None.
        '''
        if keys[locals.K_LEFT]:
            self.ball.move_left()
        elif keys[locals.K_RIGHT]:
            self.ball.move_right()
        else:
            pass

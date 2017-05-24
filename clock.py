import pygame


class Clock(object):
    '''
    A ticking clock. Provides a single method to get
    the elapsed time.
    '''
    def __init__(self):
        '''
        Class constructor.
        '''
        super(Clock, self).__init__()
        self.__clock = pygame.time.Clock()

    def tick(self):
        '''
        Returns the elapsed time between to consecutive calls
        of the tick() method.
        @return ellapsed_time.
        '''
        return self.__clock.tick()

import pygame
from pygame import locals

from controller import FirstPlayerController


class EventHandler(object):
    '''
    Handles all the events of the game.
    '''
    def __init__(self):
        '''
        Class constructor.
        @param screen.
        @param player_one first player.
        '''
        super(EventHandler, self).__init__()

    def handle_events(self):
        '''
        Handles the new events until the game is quit.
        @return None.
        '''
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                raise RuntimeError("quit!")

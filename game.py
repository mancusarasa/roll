import pygame
import sys

from screen import Screen
from event_handler import EventHandler
from ball import Ball


class Game(object):
    '''
    Main Game class.
    '''
    def __init__(self):
        super(Game, self).__init__()
        self.__screen = Screen()
        self.__player = Ball(10)
        self.__handler = EventHandler(self.__screen, self.__player)

    def Run(self):
        '''
        Runs the Game.
        @return None
        '''
        pygame.init()
        self.__handler.handle_events(self.__screen)
        sys.exit(0)

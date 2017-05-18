import pygame
import sys

from screen import Screen
from game_config import GameConfig
from event_handler import EventHandler
from ball import Ball


class Game(object):
    '''
    Main Game class.
    '''
    def __init__(self):
        super(Game, self).__init__()
        width, height, caption = self.__get_screen_config()
        self.__screen = Screen(width, height, caption)
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

    def __get_screen_config(self):
        '''
        Gets the screen configurable options.
        @return tuple with (width, height, caption).
        '''
        config = GameConfig()
        width = int(config.get('screen', 'width'))
        height = int(config.get('screen', 'height'))
        caption = config.get('screen', 'caption')
        return width, height, caption

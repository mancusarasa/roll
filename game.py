import pygame

from screen import Screen
from game_config import GameConfig
from event_handler import EventHandler
from clock import Clock
from players import FirstPlayer


class Game(object):
    '''
    Main Game class.
    '''
    def __init__(self):
        super(Game, self).__init__()
        width, height, caption = self.__get_screen_config()
        self.__screen = Screen(width, height, caption)
        self.__player = FirstPlayer()
        self.__handler = EventHandler(self.__screen, self.__player)
        self.__clock = Clock()

    def Run(self):
        '''
        The game's main loop.
        @return None
        '''
        pygame.init()
        self.__handler.main_loop()

    def __main_loop(self):
        '''
        The ACTUAL game's main loop.
        TODO: move the game's functionality to the
        __process_input, __update and __render methods.
        '''
        while True:
            elapsed_time = self.__clock.tick()
            self.__process_input()
            self.__update()
            self.__render()

    def __process_input(self):
        '''
        Processes the players' input.
        @return None.
        '''
        # here go the controllers' actions over the players
        pass

    def __update(self):
        '''
        Updates the game's state.
        @return None.
        '''
        # here go the time-related updates such as collisions,
        # gravity drops, etc.
        pass

    def __render(self):
        '''
        Renders the game's changes.
        @return None.
        '''
        # here the screen should render the changes made in __update
        pass

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

import pygame

from screen import Screen
from game_config import GameConfig
from event_handler import EventHandler
from clock import Clock
from players import FirstPlayer
from controller import FirstPlayerController


class Game(object):
    '''
    Main Game class.
    '''
    def __init__(self):
        super(Game, self).__init__()
        width, height, caption = self.__get_screen_config()
        self.__screen = Screen(width, height, caption)
        self.__players = [FirstPlayer()]
        self.__controllers = [FirstPlayerController(self.__players[0])]
        self.__handler = EventHandler()
        self.__clock = Clock()

    def Run(self):
        '''
        The game's main loop.
        @return None
        '''
        pygame.init()
        self.__main_loop()

    def __main_loop(self):
        '''
        The ACTUAL game's main loop.
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
        # events generated (such as pygame.quit)
        self.__handler.handle_events()
        # controllers' actions over the players
        for controller in self.__controllers:
            controller.handle_keys()

    def __update(self):
        '''
        Updates the game's state.
        @return None.
        '''
        # time-related updates such as collisions,
        # gravity drops, etc.
        for player in self.__players:
            player.update()

    def __render(self):
        '''
        Renders the game's changes on the screen.
        @return None.
        '''
        # Clear the screen
        self.__screen.clear()
        # Update the objects
        self.__screen.update_objects()
        # Show the updated objects
        self.__screen.flip()

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
